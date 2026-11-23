# coding:utf-8
__author__ = "ila"

import logging, os, json, configparser
import time
import numbers
import requests
from datetime import datetime, timedelta
from werkzeug.utils import redirect

from flask import request, jsonify,session
from sqlalchemy.sql import func,and_,or_,case
from sqlalchemy import cast, Integer,Float
from api.models.brush_model import *
from . import main_bp
from utils.codes import *
from utils.jwt_auth import Auth
from configs import configs
from utils.helper import *
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from utils.baidubce_api import BaiDuBce
from api.models.config_model import config
from api.services.ai_product_service import evaluate_reputation

ORDER_LOCK_MINUTES = 15
AI_SOLD_NOTE = "【AI状态更新】该商品已被出售，当前仅保留为历史记录。"
AI_LOCK_NOTE = "【AI状态更新】该商品正在交易锁定中，若买家超时未支付，库存将自动恢复。"

def _strip_ai_sale_notes(text):
    text = text or ""
    return text.replace(AI_SOLD_NOTE, "").replace(AI_LOCK_NOTE, "").strip()

def _generate_ai_sale_description(item, status):
    base_text = _strip_ai_sale_notes(item.miaoshu)
    note = AI_SOLD_NOTE if status == "sold" else AI_LOCK_NOTE
    if not base_text:
        return note
    return base_text + "\n" + note

def _sync_secondhand_sale_description(item, status):
    if not item:
        return
    item.miaoshu = _generate_ai_sale_description(item, status)

def _release_expired_locked_orders():
    now = datetime.now()
    expired_orders = goumaidingdan.query.filter(
        goumaidingdan.ispay == '未支付',
        goumaidingdan.crossrefid != None,
        goumaidingdan.stockreleased != '是',
        goumaidingdan.lockexpiretime != None,
        goumaidingdan.lockexpiretime < now
    ).all()
    if not expired_orders:
        return
    for order in expired_orders:
        item = ershouliuzhuan.query.filter_by(id=order.crossrefid).first()
        if item:
            item.shuliang = int(item.shuliang or 0) + int(order.shuliang or 0)
            item.miaoshu = _strip_ai_sale_notes(item.miaoshu)
        order.ispay = '已取消'
        order.stockreleased = '是'
    db.session.commit()

def _prepare_locked_order(req_dict):
    if req_dict.get("ispay") in [None, ""]:
        req_dict["ispay"] = "未支付"
    if req_dict.get("ispay") == "未支付":
        if not req_dict.get("lockexpiretime"):
            req_dict["lockexpiretime"] = (datetime.now() + timedelta(minutes=ORDER_LOCK_MINUTES)).strftime("%Y-%m-%d %H:%M:%S")
        if req_dict.get("stockreleased") in [None, ""]:
            req_dict["stockreleased"] = "否"
        item_id = req_dict.get("crossrefid")
        if item_id:
            item = ershouliuzhuan.query.filter_by(id=int(item_id)).first()
            if item and int(item.shuliang or 0) <= 0:
                _sync_secondhand_sale_description(item, "locked")
                db.session.commit()

def _mark_paid_order(req_dict):
    if req_dict.get("ispay") != "已支付" or not req_dict.get("id"):
        return None
    _release_expired_locked_orders()
    order = goumaidingdan.query.filter_by(id=int(req_dict["id"])).first()
    if not order:
        return "订单不存在"
    if order.ispay == "已取消" or order.stockreleased == "是":
        return "订单已超时取消，库存已释放，请重新下单"
    if order.crossrefid:
        item = ershouliuzhuan.query.filter_by(id=int(order.crossrefid)).first()
        if item and int(item.shuliang or 0) <= 0:
            _sync_secondhand_sale_description(item, "sold")
            db.session.commit()
    req_dict["_reputation_account"] = order.zhanghao
    return None

def _refresh_user_reputation(account):
    if not account:
        return
    user = yonghu.query.filter_by(zhanghao=account).first()
    if not user:
        return
    secondhand_items = ershouliuzhuan.query.all()
    paid_orders = goumaidingdan.query.filter_by(ispay="已支付").all()
    sensitive_rows = [row.content for row in sensitivewords.query.all()]
    result = evaluate_reputation(user, secondhand_items, paid_orders, sensitive_rows)
    user.xinyudengji = result.get("level")
    user.xinyufen = result.get("score")
    user.xinyushuoming = result.get("summary")
    db.session.commit()

@main_bp.before_request
def release_expired_secondhand_locks():
    try:
        request__url = session.get('request__url') or ''
        if '/goumaidingdan/' in request__url or '/ershouliuzhuan/' in request__url:
            _release_expired_locked_orders()
    except Exception as e:
        print("release expired secondhand locks failed:", e)

# 注册接口
@main_bp.route("/python7i67w282/goumaidingdan/register", methods=['POST'])
def python7i67w282_goumaidingdan_register():
    if request.method == 'POST':#post请求
        msg = {'code': normal_code, 'message': 'success', 'data': [{}]}
        req_dict = session.get("req_dict")
        _prepare_locked_order(req_dict)


        #创建新用户数据
        error = goumaidingdan.createbyreq(goumaidingdan, goumaidingdan, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = "注册用户已存在"
        else:
            msg['data'] = error
        #返回结果
        return jsonify(msg)

# 登录接口
@main_bp.route("/python7i67w282/goumaidingdan/login", methods=['GET','POST'])
def python7i67w282_goumaidingdan_login():
    if request.method == 'GET' or request.method == 'POST':#get、post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取用户名和密码参数
        req_dict = session.get("req_dict")
        req_model = session.get("req_dict")
        try:
            del req_model['role']
        except:
            pass

        #根据用户名获取用户数据
        datas = goumaidingdan.getbyparams(goumaidingdan, goumaidingdan, req_model)
        if not datas:#如果为空则代表账号密码错误或用户不存在
            msg['code'] = password_error_code
            msg['msg']='密码错误或用户不存在'
            return jsonify(msg)


        req_dict['id'] = datas[0].get('id')
        try:
            del req_dict['mima']
        except:
            pass

        #新建用户缓存数据并返回结果
        return Auth.authenticate(Auth, goumaidingdan, req_dict)


# 登出接口
@main_bp.route("/python7i67w282/goumaidingdan/logout", methods=['POST'])
def python7i67w282_goumaidingdan_logout():
    if request.method == 'POST':#post请求
        msg = {
            "msg": "退出成功",
            "code": 0
        }
        req_dict = session.get("req_dict")

        return jsonify(msg)

# 重置密码接口
@main_bp.route("/python7i67w282/goumaidingdan/resetPass", methods=['POST'])
def python7i67w282_goumaidingdan_resetpass():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success"}
        #获取传递的参数
        req_dict = session.get("req_dict")

        if req_dict.get('mima') != None:
            req_dict['mima'] = '123456'
        #更新重置后的密码
        error = goumaidingdan.updatebyparams(goumaidingdan, goumaidingdan, req_dict)

        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['msg'] = '密码已重置为：123456'
        return jsonify(msg)

# 获取会话信息接口
@main_bp.route("/python7i67w282/goumaidingdan/session", methods=['GET'])
def python7i67w282_goumaidingdan_session():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "data": {}}
        #获取token里的id，查找对应的用户数据返回
        req_dict={"id":session.get('params').get("id")}
        msg['data']  = goumaidingdan.getbyparams(goumaidingdan, goumaidingdan, req_dict)[0]

        return jsonify(msg)

# 分类接口（后端）
@main_bp.route("/python7i67w282/goumaidingdan/page", methods=['GET'])
def python7i67w282_goumaidingdan_page():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        userinfo = session.get("params")
        try:#判断是否有消息
            __hasMessage__=goumaidingdan.__hasMessage__
        except:
            __hasMessage__=None
        if __hasMessage__ and __hasMessage__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None and goumaidingdan!='chat':
                req_dict["userid"]=session.get("params").get("id")

        tablename=session.get("tablename")
        #非管理员账号则需要判断用户的相应权限
        if tablename!="users" :
            mapping_str_to_object = {}
            for model in Base_model._decl_class_registry.values():
                if hasattr(model, '__tablename__'):
                    mapping_str_to_object[model.__tablename__] = model

            try:#是否有管理员权限
                __isAdmin__=mapping_str_to_object[tablename].__isAdmin__
            except:
                __isAdmin__=None
            try:#是否有用户权限
                __authSeparate__ =mapping_str_to_object[tablename].__authSeparate__
            except:
                __authSeparate__ = None

            if __isAdmin__!="是" and __authSeparate__ == "是" and session.get("params")!=None:
                req_dict["userid"]=session.get("params").get("id")
            else:
                try:
                    del req_dict["userid"]
                except:
                    pass

            # 当前表也是有管理员权限的表
            if  __isAdmin__ == "是" and 'goumaidingdan' != 'forum':
                if req_dict.get("userid") and 'goumaidingdan' != 'chat':
                    del req_dict["userid"]
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if tablename!="users" and 'goumaidingdan'[:7]!='discuss'and "userid" in goumaidingdan.getallcolumn(goumaidingdan,goumaidingdan):
                    req_dict["userid"] = session.get("params").get("id")

        clause_args = []
        # 判断用户权限对应字段
        if tablename == 'yonghu':
            clause_args.append(goumaidingdan.zhanghao==userinfo[yonghu.__loginUser__])
            if req_dict.__contains__('zhanghao'):
                del req_dict['zhanghao']
        # 判断用户权限对应字段
        if tablename == 'yonghu':
            clause_args.append(goumaidingdan.goumaihao==userinfo[yonghu.__loginUser__])
            if req_dict.__contains__('goumaihao'):
                del req_dict['goumaihao']
        or_clauses = or_(*clause_args)
        #查询列表数据
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = goumaidingdan.page(goumaidingdan, goumaidingdan, req_dict, or_clauses)
        return jsonify(msg)

# 排序接口
@main_bp.route("/python7i67w282/goumaidingdan/autoSort", methods=['GET'])
def python7i67w282_goumaidingdan_autosort():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        req_dict['sort']='clicktime'
        req_dict['order']='desc'

        try:#获取需要排序的内容
            __browseClick__= goumaidingdan.__browseClick__
        except:
            __browseClick__=None
        #根据排序字段进行排序
        if __browseClick__ =='是':
            req_dict['sort']='clicknum'
        elif __browseClick__ =='时长':
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        #获取排序内容
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = goumaidingdan.page(goumaidingdan, goumaidingdan, req_dict)

        return jsonify(msg)

#查询单条数据
@main_bp.route("/python7i67w282/goumaidingdan/query", methods=['GET'])
def python7i67w282_goumaidingdan_query():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{}}
        #获取传递的参数，根据参数获取单条结果
        req_dict = session.get("req_dict")
        query = db.session.query(goumaidingdan)
        for key, value in req_dict.items():
            query = query.filter(getattr(goumaidingdan, key) == value)
        query_result = query.first()
        query_result.__dict__.pop('_sa_instance_state', None)
        msg['data'] = query_result.__dict__
        return jsonify(msg)

# 分页接口（前端）
@main_bp.route("/python7i67w282/goumaidingdan/list", methods=['GET'])
def python7i67w282_goumaidingdan_list():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']
            
        userinfo = session.get("params")

        try:#判断是否有列表权限
            __foreEndListAuth__=goumaidingdan.__foreEndListAuth__
        except:
            __foreEndListAuth__=None
        #不需要权限判断就去掉userid
        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None:
                req_dict['userid']=session.get("params").get("id")

        tablename=session.get("tablename")

        if 'luntan' in 'goumaidingdan':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]

        if 'discuss' in 'goumaidingdan':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]
        #根据封装的req_dict字典去筛选获取列表数据
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = goumaidingdan.page(goumaidingdan, goumaidingdan, req_dict)
        return jsonify(msg)

# 保存接口（后端）
@main_bp.route("/python7i67w282/goumaidingdan/save", methods=['POST'])
def python7i67w282_goumaidingdan_save():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取传递的参数
        req_dict = session.get("req_dict")
        for key in req_dict:#将空值转为None
            if req_dict[key] == '':
                req_dict[key] = None
        _prepare_locked_order(req_dict)

        #保存数据
        error= goumaidingdan.createbyreq(goumaidingdan, goumaidingdan, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return jsonify(msg)

# 添加接口（前端）
@main_bp.route("/python7i67w282/goumaidingdan/add", methods=['POST'])
def python7i67w282_goumaidingdan_add():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #获取参数
        req_dict = session.get("req_dict")
        #判断用户权限
        try:
            __foreEndListAuth__=goumaidingdan.__foreEndListAuth__
        except:
            __foreEndListAuth__=None
        #不需要权限则去掉userid
        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users":
                req_dict['userid']=session.get("params").get("id")
        _prepare_locked_order(req_dict)

        #保存数据
        error= goumaidingdan.createbyreq(goumaidingdan, goumaidingdan, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
            return jsonify(msg)
        else:
            msg['data'] = error
        return jsonify(msg)

# 踩、赞接口
@main_bp.route("/python7i67w282/goumaidingdan/thumbsup/<id_>", methods=['GET'])
def python7i67w282_goumaidingdan_thumbsup(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        #获取要踩赞的记录
        rets=goumaidingdan.getbyid(goumaidingdan, goumaidingdan,id_)
        update_dict={
            "id":id_,
        }
        #加减数据
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        #更新记录
        error = goumaidingdan.updatebyparams(goumaidingdan, goumaidingdan, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 获取详情信息（后端）
@main_bp.route("/python7i67w282/goumaidingdan/info/<id_>", methods=['GET'])
def python7i67w282_goumaidingdan_info(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #根据id获取对应记录
        data = goumaidingdan.getbyid(goumaidingdan, goumaidingdan, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        #浏览点击次数
        try:
            __browseClick__= goumaidingdan.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__  and  "clicknum"  in goumaidingdan.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}#增加点击次数
            ret=goumaidingdan.updatebyparams(goumaidingdan,goumaidingdan,click_dict)#更新记录
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 获取详情信息（前端）
@main_bp.route("/python7i67w282/goumaidingdan/detail/<id_>", methods=['GET'])
def python7i67w282_goumaidingdan_detail(id_):
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        #根据id获取对应记录
        data = goumaidingdan.getbyid(goumaidingdan, goumaidingdan, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        #浏览点击次数
        try:
            __browseClick__= goumaidingdan.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ and "clicknum" in goumaidingdan.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}#增加点击次数
            ret=goumaidingdan.updatebyparams(goumaidingdan,goumaidingdan,click_dict)#更新记录
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 更新接口
@main_bp.route("/python7i67w282/goumaidingdan/update", methods=['POST'])
def python7i67w282_goumaidingdan_update():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        #如果存在密码或点击次数则不更新
        if req_dict.get("mima") and "mima" not in goumaidingdan.__table__.columns :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in goumaidingdan.__table__.columns :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass
        pay_error = _mark_paid_order(req_dict)
        if pay_error:
            msg['code'] = crud_error_code
            msg['msg'] = pay_error
            return jsonify(msg)
        reputation_account = req_dict.pop("_reputation_account", None)

        #更新记录
        error = goumaidingdan.updatebyparams(goumaidingdan, goumaidingdan, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            _refresh_user_reputation(reputation_account)

        return jsonify(msg)

# 删除接口
@main_bp.route("/python7i67w282/goumaidingdan/delete", methods=['POST'])
def python7i67w282_goumaidingdan_delete():
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        #删除记录
        error=goumaidingdan.delete(
            goumaidingdan,
            req_dict
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 投票接口
@main_bp.route("/python7i67w282/goumaidingdan/vote/<int:id_>", methods=['POST'])
def python7i67w282_goumaidingdan_vote(id_):
    if request.method == 'POST':#post请求
        msg = {"code": normal_code, "msg": "success"}
        #根据id获取记录
        data= goumaidingdan.getbyid(goumaidingdan, goumaidingdan, int(id_))
        for i in data:
            #增加投票数并更新记录
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=goumaidingdan.updatebyparams(goumaidingdan,goumaidingdan,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return jsonify(msg)




#获取所有记录列表
@main_bp.route("/python7i67w282/goumaidingdan/lists", methods=['GET'])
def python7i67w282_goumaidingdan_lists():
    if request.method == 'GET':#get请求
        msg = {"code": normal_code, "msg": "success", "data": []}
        list,_,_,_,_ = goumaidingdan.page(goumaidingdan,goumaidingdan,{})
        msg['data'] = list
        return jsonify(msg)

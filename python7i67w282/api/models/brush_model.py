# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    nicheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='昵称' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    shouji=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='手机' )
    shenfen=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='身份' )
    youxiang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='邮箱' )
    touxiang=db.Column( db.Text, nullable=False, unique=False,comment='头像' )
    xingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='姓名' )
    shenfenzheng=db.Column( db.Text, nullable=False, unique=False,comment='学生证' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )
    xinyudengji=db.Column( db.VARCHAR(255),default='普通', nullable=True, unique=False,comment='信誉等级' )
    xinyufen=db.Column( db.Integer,default=60 ,  nullable=True, unique=False,comment='信誉分' )
    xinyushuoming=db.Column( db.Text,  nullable=True, unique=False,comment='信誉说明' )

class shiwuzhaoling(Base_model):
    __doc__ = u'''shiwuzhaoling'''
    __tablename__ = 'shiwuzhaoling'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    wupinmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='物品名称' )
    wupinleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='物品类型' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    wupinxiangqing=db.Column( db.Text,  nullable=True, unique=False,comment='物品详情' )
    shiqudidian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='拾取地点' )
    zhuangtai=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='状态' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    discussnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )

class renlingshenqing(Base_model):
    __doc__ = u'''renlingshenqing'''
    __tablename__ = 'renlingshenqing'



    __authTables__={'zhanghao':'yonghu','renlinghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    wupinmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='物品名称' )
    wupinleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='物品类型' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    renlinghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='认领号' )
    renlingren=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='认领人' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    dengjishijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='登记时间' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )

class shangpinleixing(Base_model):
    __doc__ = u'''shangpinleixing'''
    __tablename__ = 'shangpinleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinleixing=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='商品类型' )

class ershouliuzhuan(Base_model):
    __doc__ = u'''ershouliuzhuan'''
    __tablename__ = 'ershouliuzhuan'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='否'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='商品名称' )
    shangpinleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='商品类型' )
    pinpai=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='品牌' )
    guige=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='规格' )
    jiage=db.Column( db.Integer, default=0 , nullable=False, unique=False,comment='价格' )
    shuliang=db.Column( db.Integer, default=0 , nullable=False, unique=False,comment='数量' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    miaoshu=db.Column( db.Text, nullable=False, unique=False,comment='描述' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    jiaoyidizhi=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='交易地址' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    clicknum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )

class goumaidingdan(Base_model):
    __doc__ = u'''goumaidingdan'''
    __tablename__ = 'goumaidingdan'



    __authTables__={'zhanghao':'yonghu','goumaihao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    shangpinmingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品名称' )
    shangpinleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='商品类型' )
    pinpai=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='品牌' )
    guige=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='规格' )
    jiage=db.Column( db.Integer, default=0 ,  nullable=True, unique=False,comment='价格' )
    shuliang=db.Column( db.Integer, default=0 ,  nullable=True, unique=False,comment='购买数量' )
    jine=db.Column( db.Integer, default=0 ,  nullable=True, unique=False,comment='金额' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    jiaoyidizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='交易地址' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    goumaihao=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='购买号' )
    goumairen=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='购买人' )
    dianhua=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='电话' )
    dengjishijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='登记时间' )
    ispay=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='是否支付' )
    crossuserid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='关联用户id' )
    crossrefid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='关联商品id' )
    lockexpiretime=db.Column( db.DateTime,  nullable=True, unique=False,comment='库存锁定到期时间' )
    stockreleased=db.Column( db.VARCHAR(255), default='否', nullable=True, unique=False,comment='库存是否已释放' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger, default=0 ,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class sensitivewords(Base_model):
    __doc__ = u'''sensitivewords'''
    __tablename__ = 'sensitivewords'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    content=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='内容' )

class discussshiwuzhaoling(Base_model):
    __doc__ = u'''discussshiwuzhaoling'''
    __tablename__ = 'discussshiwuzhaoling'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )
    isanon = db.Column(db.Integer, default=0, nullable=True, unique=False, comment='匿名(1:匿名,0:非匿名)')

class discussershouliuzhuan(Base_model):
    __doc__ = u'''discussershouliuzhuan'''
    __tablename__ = 'discussershouliuzhuan'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )
    isanon = db.Column(db.Integer, default=0, nullable=True, unique=False, comment='匿名(1:匿名,0:非匿名)')

class discussnews(Base_model):
    __doc__ = u'''discussnews'''
    __tablename__ = 'discussnews'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, default=0 , nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0 ,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )
    isanon = db.Column(db.Integer, default=0, nullable=True, unique=False, comment='匿名(1:匿名,0:非匿名)')

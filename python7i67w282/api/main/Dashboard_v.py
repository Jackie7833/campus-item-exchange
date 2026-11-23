# coding:utf-8
from flask import jsonify
from sqlalchemy import func, or_

from . import main_bp
from api.exts import db
from api.models.brush_model import ershouliuzhuan, goumaidingdan, shiwuzhaoling, renlingshenqing
from utils.codes import normal_code


def _num(value):
    return int(value or 0)


@main_bp.route("/python7i67w282/dashboard/summary", methods=["GET"])
def python7i67w282_dashboard_summary():
    paid_filter = goumaidingdan.ispay == "已支付"
    unpaid_filter = or_(goumaidingdan.ispay != "已支付", goumaidingdan.ispay == None)

    secondhand_stock = db.session.query(func.coalesce(func.sum(ershouliuzhuan.shuliang), 0)).scalar()
    purchase_quantity = db.session.query(func.coalesce(func.sum(goumaidingdan.shuliang), 0)).scalar()
    paid_amount = db.session.query(func.coalesce(func.sum(goumaidingdan.jine), 0)).filter(paid_filter).scalar()

    return jsonify({
        "code": normal_code,
        "msg": "success",
        "data": {
            "secondhandCount": _num(ershouliuzhuan.query.count()),
            "secondhandStock": _num(secondhand_stock),
            "orderCount": _num(goumaidingdan.query.count()),
            "purchaseQuantity": _num(purchase_quantity),
            "paidOrderCount": _num(goumaidingdan.query.filter(paid_filter).count()),
            "unpaidOrderCount": _num(goumaidingdan.query.filter(unpaid_filter).count()),
            "paidAmount": _num(paid_amount),
            "lostfoundCount": _num(shiwuzhaoling.query.count()),
            "pendingClaimCount": _num(renlingshenqing.query.filter(renlingshenqing.sfsh == "待审核").count())
        }
    })

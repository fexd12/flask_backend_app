from . import bp
from app import current_app,cross_origin,db
from flask import jsonify,request
from app.erros import bad_request
from app.authenticate import check_token_dec

@bp.route('/',methods=['GET'])
@check_token_dec
def get_():
   pass
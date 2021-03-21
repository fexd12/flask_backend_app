#import routes blueprint

from flask import Blueprint

bp = Blueprint('teste',__name__)

from . import routes
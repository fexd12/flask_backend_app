from app import db
from app.auxiliar import AutoAttributes

class Test(db.Model,AutoAttributes):
    __tablename__ = 'teste'
    id_teste = db.Column(db.Integer,primary_key=True)
    teste = db.Column(db.Text)
    # acesso = db.relationship('Usuario', backref='acessos', lazy=True)

    attrs = ['id_teste','teste']
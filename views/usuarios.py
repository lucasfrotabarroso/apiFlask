
from flask import jsonify

from models.usuario import bd
from flask import Blueprint

usuario_views = Blueprint("usuario_views", __name__)

@usuario_views.route('/usuarios', methods = ['GET'])
def exibir_usuarios():
    return jsonify(bd["usuarios"])

@usuario_views.route('/usuarios/<string:username>', methods = ['GET'])
def exibir_usuario_por_nome(username):
    for item in bd["usuarios"]:
        if item.get("username") == username:
            return item
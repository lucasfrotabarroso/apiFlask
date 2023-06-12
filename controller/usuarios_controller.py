from flask import request,Blueprint
from models.usuario import *


usuarios_controller = Blueprint("usuarios_controller", __name__)

@usuarios_controller.route('/inserir', methods = ['POST'])
def login():
    for item in bd["usuarios"]:
        if item.get("username") == request.form["username"]:
            for senha in bd["usuarios"]:
                if senha.get("password") == request.form["password"]:
                    return "login ok"
                else:
                    return "senha errada"
        else:
            return "o username nao existe na base de dados"

@usuarios_controller.route('/usuarios/registrar', methods = ['POST'])
def registrar():
    username = request.form["username"]
    senha = request.form["password"]
    novo_user = usuario.adicionar_usuario(username, senha)
    return bd["usuarios"]



@usuarios_controller.route('/usuarios/<string:username>', methods = ['PUT'])
def alterar_usuario(username):
    new_username = request.form["username"]
    new_senha = request.form["password"]
    for item in bd["usuarios"]:
        if item.get("username") == username:
            item.update(usuario(new_username,new_senha).__dict__)
            return bd["usuarios"]

@usuarios_controller.route('/usuarios/<string:username>', methods = ['DELETE'])
def deletar(username):
    for item in bd["usuarios"]:
        if username == item.get("username"):
            bd["usuarios"].remove(item)
            return bd
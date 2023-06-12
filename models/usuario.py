

bd = {"usuarios":[
    {"username": "lucas",
     "password":"123"},
    {"username":"joao",
     "password":"teste"}
]}

class usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def adicionar_usuario(username,password):
        novo_usuario = {"username": username,
                        "password":password}
        bd["usuarios"].append(novo_usuario)


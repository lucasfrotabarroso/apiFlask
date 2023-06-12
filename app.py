from views.usuarios import *
from controller.usuarios_controller import *
from flask import Flask

app = Flask(__name__)


@app.route('/')
def tela():
    return '<h1> Home </h1>'


app.register_blueprint(usuarios_controller, url_prefix='/')
app.register_blueprint(usuario_views, url_prefix='/')

app.run(debug=True)

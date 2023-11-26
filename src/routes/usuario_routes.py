from flask import Blueprint, jsonify,request
from controllers.usuario_controller import userController
from flask_cors import cross_origin
usuario = Blueprint('usuario',__name__ )

@usuario.route('/login', methods=['POST'])
@cross_origin()
def login():
    user=request.json
    response = userController.login(user=user)
    return jsonify(response) 

@usuario.route('/insert', methods=['POST'])
@cross_origin()
def insertUsuario():
    if request.method == 'POST':
        usuario=request.json
        if usuario:
            response = userController.insertar_usuario(usuario=usuario)
            return jsonify(response)
        else:
            return jsonify(False)
     
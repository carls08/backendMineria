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
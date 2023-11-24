from flask import Blueprint, jsonify,request
from src.controllers.usuario_controller import userController

usuario = Blueprint('usuario',__name__ )
@usuario.route('/login', methods=['POST'])
def login():
    user=request.json
    response = userController.login(user=user)
    return jsonify(response)  
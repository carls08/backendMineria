from flask import Blueprint,request, jsonify
from flask_cors import cross_origin
from controllers.prediccion_controller import prediccion_controller

machine_learning = Blueprint('Machine_Learning', __name__)

@machine_learning.route('/prediction', methods=['POST'])
@cross_origin()
def index_prediction():
    response=prediccion_controller.controller_prediction_predict(request.json)
    return jsonify({'Respuesta':int(response)})


from models.prediccion_model import prediccionModel

class prediccion_controller:
    @classmethod
    def controller_prediction_predict(cls,data):
        for dato in data:
            if not dato:
                return False
        
        response=prediccionModel().model_prediccion_prediction(data=data)
        return response
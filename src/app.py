from flask import Flask, jsonify,Blueprint
from routes.usuario_routes import  usuario
from routes.prediccion_routes import machine_learning

app = Flask(__name__)
app.register_blueprint(usuario)
app.register_blueprint(machine_learning)

app.secret_key="SECRET_KEY"

@app.route('/')
def index():
    return jsonify({'Mensaje':'Welcome to the jungle'})

if __name__ == '__main__':
    app.run(debug=True)
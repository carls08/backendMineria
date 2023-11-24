from flask import Flask, jsonify
from src.routes.usuario_routes import  usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def index():
    return jsonify({'Mensaje':'Welcome to the jungle'})

if __name__ == '__main__':
    app.run(debug=True)
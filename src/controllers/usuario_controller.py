from config import Connecction
from models.usuario_model import usuarioModel


class userController:
    
    @classmethod
    def login(cls, user):
       try:
           with Connecction.getConnection().cursor() as cursor:
               sql="SELECT * FROM usuario WHERE usuario=%s AND user_password=%s"
               cursor.execute(sql, (user['usuario'], user['password']))
               return cursor.fetchone()
           
       except Exception as ex:
           print(ex)
           return False
       
    @classmethod
    def insertar_usuario(cls, usuario):
        for value in usuario.values():
            # validamos que ningun campo venga vacion
            if not value:
                return False
        
        response = usuarioModel.modelo_insertar_usuario(usuario)
        return response
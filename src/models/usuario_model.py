from config import Connecction

class usuarioModel:
    @classmethod
    def modelo_insertar_usuario(cls, user):
            conexion=Connecction.getConnection()
            with conexion.cursor() as cursor:
                try:
                    sql = "INSERT INTO usuario(documento,nombre,apellido,s_apellido,user_password,usuario,correo,telefono) VALUES(%s, %s, %s, %s, %s, %s, %s,%s)"
                    cursor.execute(sql, (int(user['documento']), user['nombre'], user['apellido'],user['s_apellido'], user['user_password'], user['usuario'], user['correo'], (int(user['telefono']))))
                    conexion.commit()
                    return True
                
                except Exception as ex: 
                    print(ex)
                    return False
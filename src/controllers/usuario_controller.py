from config import Connecction
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
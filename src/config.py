import psycopg2
#nuestra conexion a la base de datos con sus credenciales
class Connecction:
    @staticmethod
    def getConnection():
        try:
            con= psycopg2.connect(
                host='db.ycdzcipixhpyqelzgptu.supabase.co',
                database='postgres',
                port=5432,
                user='postgres',
                password='Supa1234Base1234',
               
               
            )
            return con
        except Exception as ex:
            return False
        
if __name__ == '__main__':
    connection = Connecction.getConnection()
    
    print(connection)
        
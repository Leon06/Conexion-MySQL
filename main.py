# 1 Autenticarme con el servidor --> mysql -u root -p ->****6
# USE pythondb;

import pymysql
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"
USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

#Insertar multiples registros
users = [
    ("user1","password","user1@yahoo.com"),
    ("user2","password","user2@yahoo.com"),
    ("user3","password","user3@yahoo.com"),
    ("user4","password","user4@yahoo.com"),
]

if __name__ == '__main__':
    
    try:
        connect= pymysql.Connect(host='127.0.0.1', 
                                port=3306,
                                user= config('USER_MYSQL'),
                                passwd=config('PASSWORD_MYSQL'),
                                db=config('DB_MYSQL'))
        
        with connect.cursor() as cursor:
           
            cursor.execute(DROP_TABLE_USERS)        
            cursor.execute(USERS_TABLE )
            
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            
            #insertar varios usuarios
            for user in users:
                cursor.execute(query, user)            
            connect.commit()        
                
                #OBTENER REGISTROS
            # query = "SELECT * FROM users"
            # rows = cursor.execute(query)    
            # print(rows)
                #acceder a registros
            #1 for user in users:
               #print(user)    
            #2 print(cursor.fetchall())
            
                #ACTUALIZAR REGISTROS                
            # query = "UPDATE users SET username=%s WHERE id=%s"
            # values = ("cambio de username",1)
            # cursor.execute(query, values)            
            # connect.commit()       
            
                #ELIMINAR REGISTROS
            # query = "DELETE FROM users WHERE id = %s"
            # cursor.execute(query, (4))            
            # connect.commit()     
            
            
        
    except pymysql.err.OperationalError as err:
        
        print('¡¡no fue posible realizar la conexion!!')
        print(err)
        
    finally:
        
        cursor.close() # siempre que creememos un objeto de tipo conexion o tipo cursor ;cuando teminenemos de utilizarlo hay que utlizar los metodos close
        connect.close()
        
        print("Conexion finalizada con exito")
    


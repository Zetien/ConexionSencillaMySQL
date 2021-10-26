import pymysql

miConexion=pymysql.connect(user='root',password='12345',host='127.0.0.1',port=3306,database='prueba1server')

cursor=miConexion.cursor()

sql='SELECT * FROM conductor' #tabla en dba

cursor.execute(sql)
linea='__'
registros=cursor.fetchall()

for registro in registros:
    print(registro)
    print(linea*50,'\n') 




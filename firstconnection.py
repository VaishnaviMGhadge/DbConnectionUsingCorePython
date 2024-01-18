import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='Vaish@2350')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("CREATE DATABASE db1")

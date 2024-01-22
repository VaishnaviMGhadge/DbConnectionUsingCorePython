import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vaish@2350',
                             database='db1'

)
cur=mydb.cursor()
query="insert into book1 (bookid,name,price) values(%s,%s,%s)"
b1=(1,'python',23)
cur.execute(query,b1)
mydb.commit()
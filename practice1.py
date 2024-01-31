import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user="root",
                             password='Vaish@2350',
                             database='practice1')
cur=mydb.cursor()

query="update student1 set name='vaishnavi' where Id=1"
cur.execute(query)

mydb.commit()

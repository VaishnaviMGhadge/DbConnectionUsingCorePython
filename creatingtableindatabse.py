import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vaish@2350',
                             database='db1'

)
cur=mydb.cursor()

query="create table book(bookid integer(4),name varchar(20),price float(3,2))"
cur.execute(query)
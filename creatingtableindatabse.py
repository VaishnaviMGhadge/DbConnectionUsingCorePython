import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vaish@2350',
                             database='db1'

)
cur=mydb.cursor()

query="create table book1(bookid integer(4),name varchar(20),price integer(3))"
cur.execute(query)
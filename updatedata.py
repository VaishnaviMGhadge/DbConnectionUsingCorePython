import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vaish@2350',
                             database='db1'


)
cur=mydb.cursor()
query="update book1 set name='Vaishnavi' where bookid=2 "
cur.execute(query)
mydb.commit()
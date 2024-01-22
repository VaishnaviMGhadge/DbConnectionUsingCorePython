import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vaish@2350',
                             database='db1'

)
cur=mydb.cursor()
query='delete from book1 where bookid=3'
cur.execute(query)
mydb.commit()
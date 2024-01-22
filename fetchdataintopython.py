import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vaish@2350',
                             database='db1'

)
cur=mydb.cursor()
query='select * from book1'
cur.execute(query)
list1=cur.fetchall()
for i in list1:
    print(i)


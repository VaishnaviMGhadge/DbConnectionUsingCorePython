import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='Vaish@2350',database='db1')
query='insert into bookdata(bookid,name) values(%s,%s)'
b1=[(11,'a'),(12,'b')]
cur=mydb.cursor()
cur.executemany(query,b1)
for i in cur.fetchall():
    print(i)
#mydb.commit()

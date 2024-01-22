import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Vaish@2350',
    database='db1'
)
cur=mydb.cursor()
query="insert into book1 (bookid,name,price) values(%s,%s,%s)"
book_list=[(2,'tatayan',500),(3,'atomic habits',2000),(4,'let us C',790)]
cur.executemany(query,book_list)
mydb.commit()
def sqlcon():
    import mysql.connector as c
    n=input('Enter mysql password') 
    i=c.connect(host='localhost',user='root',passwd=n)
    cur=i.cursor()
    cur.execute("create database info")
    cur.execute('use info')
    cur.execute('create table information(username varchar(20)unique NOT NULL,password varchar(20) primary key)')



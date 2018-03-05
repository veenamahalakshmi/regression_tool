import sqlite3

conn = sqlite3.connect('spirent.db')
cur = conn.cursor()
#cur.execute("drop table spirent")
#cur.execute("create table spirent(username varchar(255),password varchar(255),emailid varchar(255),empid Integer(255),ph_num Integer(10))")
cur.execute("select * from spirent")
for row in cur.fetchall():
    print(row)
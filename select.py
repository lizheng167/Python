# -*- coding: utf-8
import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='111111',
    db='lianxi',
    charset='utf8'
)
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
print cursor.rowcount

rs = cursor.fetchall()
for row in rs:
    print "user_id=%s,user_name=%s" % row

cursor.close()
conn.close()

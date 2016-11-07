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
sql_insert = "insert into user(user_name) values('guohx')"
sql_update = "update user set user_name='haha' where user_id=1"
sql_delete = "delete from user where userid < 3"
try:
	cursor.execute(sql_insert)
	print cursor.rowcount
	cursor.execute(sql_update)
	print cursor.rowcount
	cursor.execute(sql_delete)
	print cursor.rowcount
	conn.commit()
except Exception as e:
	print e
	conn.rollback()
cursor.close()
conn.close()

**Python操作MySQL实战（四)**

import pymysql

def deleteMySQL():
	try:
		conn=pymysql.connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		sql='delete from student where id=%s'
		params=(12,)
		cur.execute(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()

deleteMySQL()
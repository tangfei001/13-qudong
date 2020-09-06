**课时164(2)-Python操作MySQL实战（二）**

核心:多条语句的查询

用到的知识点
	1:链接数据库conn=pymysql.connect()
	2:创建邮标 cur=conn.cursor()
	3:查询数据cur.execute()
	4:查询多行数据 cur.fetchall()
	5:列表推导是

具体看代码

import pymysql

def connMySQL():
	try:
		conn=pymysql.connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		#创建游标
		cur=conn.cursor()
		#写列表推导四
		sql='select * from student where id=%s'
		params=(1,)
		cur.execute('select * from student')
		data=cur.fetchall()
		print([item for item in data])
	finally:
		pass
print(connMySQL())
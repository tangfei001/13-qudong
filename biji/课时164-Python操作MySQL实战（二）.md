**课时164-Python操作MySQL实战（二）**

01:步骤
	1:导入包 import pymysql
	2:链接mysql 
		conn=pymysql.connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	
	3:创建邮标 cur=conn.cursor()
	4:查询数据
			sql='select * from student where id=%s'
			params=(1,)
			cur.execute(sql,params)
	5:单条语句查询:
		data=cur.fetchone()
		print(data)	
	6:关系mysql链接迟
		cur.close()
		conn.close()
	
代码演示
import pymysql

#查询
def connMySQL():
	try:
		conn=pymysql.connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		sql='select * from student where id=%s'
		params=(1,)
		cur.execute(sql,params)
		data=cur.fetchone()
		print(data)
	finally:
		cur.close()
		conn.close()

print(connMySQL())

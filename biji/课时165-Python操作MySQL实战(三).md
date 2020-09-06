**课时165-Python操作MySQL实战(三)**

单条数据插入:
import pymysql

def insertMySQL():
	try:
		conn=pymysql.connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		#插入语句-单行数据
		sql='insert into student values(%s,%s,%s,%s,%s)'
		params=(9,'网页上',25,'男',80)
		cur.execute(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()

print(insertMySQL())


多条数据插入

import pymysql

def insertMySQL():
	try:
		conn=pymysql.connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		#插入语句-插入多行数据
		sql = 'insert into student values(%s,%s,%s,%s,%s)'
		params=[
			(10,'网点',25,'女',82),
			(11,'我说的',26,'男',86)
		]
		cur.executemany(sql,params)
		conn.commit()
	finally:
		cur.close()
		conn.close()

print(insertMySQL())
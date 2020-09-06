#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:47
# @Author  : Aries
# @Site    : 
# @File    : 04-mysqlTest1.py
# @Software: PyCharm
'''
说明:实现mysql的增删改查
内容:
01:单条语句的查询
02:多条语句的查询
03:插入单条语句
04:插入多条语句
05:删除语句
常用的内容
1:连接数据库conn=pymysql.connect()
2:创建邮标 cur=conn.cursor()
3:写入sql语句并查询
	sql=''
	params=()
	cur.execute(sql,params)
'''

import pymysql

def chaxunMySql():
	'''单条语句的查询'''
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
		params=(2,)
		cur.execute(sql,params)
		data=cur.fetchone()
		return data
	finally:
		conn.close()
		cur.close()

def chaxunMySql2():
	'''多条语句的查询'''
	try:
		conn=pymysql.Connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		sql='select * from student where id=%s'
		params=(2,)
		cur.execute('select * from student')
		data=cur.fetchall()
		return [i for i in data]
	finally:
		conn.close()
		cur.close()

def insertMySql():
	'''单条语句的插入'''
	try:
		conn=pymysql.Connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		sql='insert into student values(%s,%s,%s,%s,%s)'
		params=('21','唐飞6','26','男',85)
		cur.execute(sql,params)
		conn.commit()
	finally:
		conn.close()
		cur.close()

def insertMySql2():
	'''多条语句的插入'''
	try:
		conn=pymysql.Connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		sql='insert into student values(%s,%s,%s,%s,%s)'
		params=[
			(22,'唐飞7',26,'男',87),
			(23,'唐飞8',28,'女',89)
		]
		cur.executemany(sql,params)
		conn.commit()
	finally:
		conn.close()
		cur.close()

def deleteMySqL():
	'''删除数据'''
	try:
		conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='test1')
	except Exception as e:
		print(e.args)
	else:
		cur=conn.cursor()
		sql='delete from student where id=%s'
		params=(20,)
		cur.execute(sql,params)
		conn.commit()
	finally:
		conn.close()
		cur.close()

#print(chaxunMySql())
#print(chaxunMySql2())
#print(insertMySql())
#print(insertMySql2())
print(deleteMySqL())




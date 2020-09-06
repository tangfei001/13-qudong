#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:48
# @Author  : Aries
# @Site    : 
# @File    : 05-mysqlTest2.py
# @Software: PyCharm
'''
第一步:写一个类MySqlHelper()
	01:写链接数据库函数
	02:写查询函数
第二步:写一个检查函数checkVarible(id,name)
	01:对类进行实例化
	02:输入sql和params
	03:返回查询函数
第三步:写一个函数info()
	01:让用户自己输入内容
	02:定义一个变量让他返回检查函数
	03:进行判断
第四步:主函数中执行函数info()
'''
import pymysql

class MySqlHelper():
	def conn(self):
		'''链接数据库'''
		conn=pymysql.Connect(host='127.0.0.1',
		                     user='root',
		                     passwd='root',
		                     db='test1')
		return conn

	def chaxunMySql(self,sql,params):
		'''写单条查询函数'''
		cur=self.conn().cursor()
		data=cur.execute(sql,params)
		result=cur.fetchone()
		return result

def checkMySql(id,name):
	'''写函数对chaxunMySql进行处理'''
	#实例化
	opera=MySqlHelper()
	#输入对应的数据
	sql='select * from student where id=%s and name=%s'
	params=(id,name)
	#返回函数
	return opera.chaxunMySql(sql=sql,params=params)

def info():
	id =int(input('请输入id: \n'))
	name=input('请输入姓名: \n')
	result=checkMySql(id,name)
	if result:
		print('恭喜id是{0}的用户登录成功'.format(id))
	else:
		print('登录失败')

if __name__ == '__main__':
    info()




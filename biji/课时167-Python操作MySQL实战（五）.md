**课时167-Python操作MySQL实战（五）**

思路:通过类的方式对代码进行改造
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
	#链接数据库函数
	def con(self):
		con=pymysql.connect(host='127.0.0.1',
		                    user='root',
		                    passwd='root',
		                    db='test1')
		return con
	#写查询函数
	def get_one(self,sql,params):
		cur=self.con().cursor()
		data=cur.execute(sql,params)
		result=cur.fetchone()
		return result

#写检查函数
def checkVarible(id,name):
	#进行实例化
	opera=MySqlHelper()
	#输入sql和params
	sql='select * from student where id=%s and name=%s'
	params=(id,name)
	#返回查询结果函数
	return opera.get_one(sql=sql,params=params)

#在写一个函数
def info():
	id=int(input('请输入id:\n'))
	name=input('请输入姓名:\n')
	result=checkVarible(id,name)
	if result:
		print('恭喜id是{0}的用户登录成功'.format(id))
	else:print('登录失败')

if __name__ == '__main__':
    info()
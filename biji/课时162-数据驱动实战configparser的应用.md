**课时162-数据驱动实战configparser的应用**


核心:配置文件的应用 后缀.ini

'''
import configparser
04:定义一个新列表
01:实例化
02:读取数据
03:获取数据
04:将获取到的数据写入新的列表
05:打印列表
'''

import configparser
import  os

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)

def getLinux(linux='linux'):
	list1=[]
	#实例化
	config=configparser.ConfigParser()
	#读文件
	config.read(base_dir('config.ini'))
	#获取对应的数据
	ip=config.get(linux,'IP')
	port= config.get(linux, 'PORT')
	username= config.get(linux, 'USERNAME')
	pasword= config.get(linux, 'PASSWORD')
	#写入列表
	list1.append(ip)
	list1.append(port)
	list1.append(username)
	list1.append(pasword)
	return list1

print(getLinux()[0])



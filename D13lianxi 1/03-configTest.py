#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 11:06
# @Author  : Aries
# @Site    : 
# @File    : 03-configTest.py
# @Software: PyCharm
'''
说明:数据驱动配置文件
步骤
import configparser
04:定义一个新列表
01:实例化
02:读取数据
03:获取数据
04:将获取到的数据写入新的列表
05:打印列表
'''
import configparser
import os

def base_dir(fileName=None):
	return os.path.join(os.path.dirname(__file__),fileName)

def getLinux(linux='linux'):
	#定义一个新的列表
	list1=[]
	#实例化
	config=configparser.ConfigParser()
	#读取文件
	config.read(base_dir('config.ini'))
	#通过get方法获取文件
	ip=config.get(linux,'ip')
	port=config.get(linux,'port')
	username=config.get(linux,'username')
	password=config.get(linux,'password')
	#将数据写入新列表
	list1.append(ip)
	list1.append(port)
	list1.append(username)
	list1.append(password)
	#返回新列表
	return list1

print(getLinux())
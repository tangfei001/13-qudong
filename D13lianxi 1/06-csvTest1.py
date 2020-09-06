#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 14:14
# @Author  : Aries
# @Site    : 
# @File    : 06-csvTest1.py
# @Software: PyCharm
'''
第一种读取csv文件的方式--按列表的方式读取
步骤:
01:定义一个函数readCsvList()
	01:使用openn函数打开
		01:使用迭代器reader  csv.reader()
		02:使用next()
		03:进行循环
'''
import csv

def readCsvList():
	with open('csv.csv','r')as f:
		#使用迭代器读取
		reader=csv.reader(f)
		#使用next()
		next(reader)
		#对reader进行循环
		for item in reader:
			print(item)

readCsvList()
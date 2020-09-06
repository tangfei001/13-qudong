#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 14:14
# @Author  : Aries
# @Site    : 
# @File    : 07-csvTest2.py
# @Software: PyCharm
'''
第二种读取csv文件的方式---按字典的方式读取
'''
import csv

def readDictList():
	with open('csv.csv','r')as f:
		reader=csv.DictReader(f)
		for item in reader:
			print(dict(item))

readDictList()
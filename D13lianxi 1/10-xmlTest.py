#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 16:28
# @Author  : Aries
# @Site    : 
# @File    : 10-xmlTest.py
# @Software: PyCharm
'''
01:读取单节点的数据(关键字节点)
	<yan>学海无涯苦作舟</yan>
'''
import xml.dom.minidom

def getXml(value=None):
	xmlFile=xml.dom.minidom.parse('data.xml')
	db=xmlFile.documentElement
	itemList=db.getElementsByTagName(value)
	item=itemList[0]
	return item.firstChild.data

print(getXml('yan'))



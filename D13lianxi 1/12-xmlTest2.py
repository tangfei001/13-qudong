#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 16:31
# @Author  : Aries
# @Site    : 
# @File    : 12-xmlTest2.py
# @Software: PyCharm
'''
02:读取单节点的数据(关键字节点)
	<WuYA nick="无涯" age="18" sex="boy" address="xian"></WuYA>
'''
import xml.dom.minidom

def getUser(parent='WuYA',child=None):
	'''获取单节点的数据内容'''
	xmlFile=xml.dom.minidom.parse('data.xml')
	db=xmlFile.documentElement
	itemList=db.getElementsByTagName(parent)
	item=itemList[0]
	return item.getAttribute(child)

print(getUser(child='address'))

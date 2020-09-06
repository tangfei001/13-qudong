#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 10:36
# @Author  : Aries
# @Site    : 
# @File    : 02-excelTest2.py
# @Software: PyCharm
'''
说明:对excel中的内容进行修改
步骤
01-from xlutils.copy import copy
02-读取文件
03-保存之前的文件 copy()
04-到具体的sheet xxx.get_sheet(0)
05-写入文件 xxx.write()
06-将写入的文件保存到具体的文件 xxx.save()
'''
import xlrd
import os
from xlutils.copy import copy

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)
#打开文件
work=xlrd.open_workbook(base_dir('data.xls'))
#保存之前的文件
old_content=copy(work)
#定位到具体的sheet
wt=old_content.get_sheet(0)
#写文件
wt.write(12,2,'唐飞')
#再次保存
old_content.save(base_dir('data.xls'))






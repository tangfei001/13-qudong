**课时161-数据驱动实战对Excel文件内容的修改**

excel文件内容的修改


思路
'''
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

#读取文件
work=xlrd.open_workbook(base_dir('data2.xls'))
#保存之前的文件
old_content=copy(work)
#到具体的sheet
ws=old_content.get_sheet(0)
#写入文件
ws.write(12,2,'我是传奇')
#再次保存
old_content.save(base_dir('data2.xls'))
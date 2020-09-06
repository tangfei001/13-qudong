**课时159-数据驱动Excel文件的操作方法**

涉及的库
xlrd-----r
xlwt-----w
xlutils---文件内容的修改  (这个库需要安装)
---------------------------------------------------------------------------
'''
思路:
import xlrd
import os

01:写一个函数-使用os库进行目录拼接(获取文件的目录)
02:打开文件
03:具体到sheet或者name
04:操作
	001:查看多少行
	002:获取到具体单元格的内容
-----------------------------------------------------------------------------

import xlrd
import os

def base_dir(filename=None):
	return os.path.join(os.path.dirname(__file__),filename)

'''excel文件内容的操作'''
work=xlrd.open_workbook(base_dir('data.xls'))
sheet=work.sheet_by_index(0)
print(sheet.nrows) 查看多少行
print(sheet.ncols)查看有多少列
print(sheet.cell_value(9,1)) 获取单元格的内容


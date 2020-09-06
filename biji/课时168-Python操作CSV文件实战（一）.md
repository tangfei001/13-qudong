**课时168-Python操作CSV文件实战（一）**

第一种读取csv文件的方式--按列表的方式读取

'''
01:定义一个函数readCsvList()
	01:使用openn函数打开
		01:使用迭代器reader  csv.reader()
		02:使用next()
		03:进行循环

'''
import csv

#定义一个函数readCsvList()
def readCsvList():
	with open('csv.csv','r')as f:
		#迭代器reader()
		reader=csv.reader(f)
		#使用next处理
		next(reader)
		#对reafer进行循环
		for x in reader:
			print(x)

readCsvList()
print(type(readCsvList()))

---------------------------------------------------

第二种读取csv文件的方式---按字典的方式读取
'''
01定义一个函数-readCsvDict()
	01:使用open()函数读取内容
		02:使用csv.DictReader(f)
		03:对内容进行循环

'''
def readCsvDict():
	with open('csv.csv','r')as f:
		reader=csv.DictReader(f)
		for x in reader:
			print(dict(x))




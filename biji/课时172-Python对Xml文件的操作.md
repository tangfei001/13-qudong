**课时172-Python对Xml文件的操作**

01:读取单节点的数据(关键字节点)
'''
<yan>学海无涯苦作舟</yan>
'''

def getXml(value=None):
	'''读取单节点的数据'''
	xmlFile = xml.dom.minidom.parse('data.xml')
	db = xmlFile.documentElement
	itemList = db.getElementsByTagName(value)
	item = itemList[0]
	return item.firstChild.data

print(getXml('yan'))

02:读取单节点的数据(关键字节点)
'''
   <WuYA nick="无涯" age="18" sex="boy" address="xian"></WuYA>
'''
def getUser(parent='WuYA',child=None):
	'''获取单节点的数据内容'''
	xmlFile=xml.dom.minidom.parse('data.xml')
	db=xmlFile.documentElement
	itemList=db.getElementsByTagName(parent)
	item=itemList[0]
	return item.getAttribute(child)

print(getUser(child='address'))
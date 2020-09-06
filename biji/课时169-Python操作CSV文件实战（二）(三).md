**课时169-Python操作CSV文件实战（二）**

# 核心要点:CSV文件的写入 #
'''
01:写一个函数获取请求头
02:定义一个函数lagou  def laGou(page=2):
	03:定义一个空的列表positions positions=[]
	01:完成post接口的编写
	   001:print(r.text)
       002:lagou()---调用函数获得数据
       003:拿到返回的数据,使用json在线工具进行处理
	02:对数据进行处理(使用for循环和json在线工具)
		01:导入对应的参数(结合json在线工具处理) for i in range(1,15)
	   	02:吧获取的数据放到一个字典当中 position={'xx':'xxx'}
        03:positions.append(position)
04:return positions


03:主函数(验证数据.验证完毕关闭注释)
   if __name__ == '__main__':
       for item in range(1,31):
 	      laGou(page=item)

05:定义一个函数-写入 writeCsv()
	02:写入title headers={"公司名称",'xxx'}
	01:对内容进行循环(使用for循环)
	02:在for循环里面写入数据(用csv库中以csv的方式写入)
        with open('login.csv','a',newline='',encoding='gbk') as f:
		    write=csv.DictWriter(f,headers)
		    write.writeheader()
		    write.writerows(positons)

06:writeCsv()


## 案例演示: ##

import csv
import requests


'''通过接口测试的技术获取拉钩网平台的资料'''
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

#写一个函数获取到对应的heswes
def getHeaders():
	headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Cookie':'_ga=GA1.2.1237290736.1534169036; user_trace_token=20180813220356-b7e42516-9f01-11e8-bb78-525400f775ce; LGUID=20180813220356-b7e428ad-9f01-11e8-bb78-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.675811712.1540794503; JSESSIONID=ABAAABAAAGFABEF93F47251563A52306423D37E945D2C54; _gat=1; LGSID=20181029213144-fa3c8e13-db7e-11e8-b51c-525400f775ce; PRE_UTM=; PRE_HOST=www.bing.com; PRE_SITE=https%3A%2F%2Fwww.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539529521,1539785285,1540794503,1540819902; SEARCH_ID=ae3ae41a58d94802a68e848d36c30711; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540819909; LGRID=20181029213151-fe7324dc-db7e-11e8-b51c-525400f775ce',
		'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'}
	return headers

#定义一个函数laGou
def laGou(page=2):
	#定义一个空的列表
	positions=[]
	#完善接口信息
	r=requests.post(url=url,
		headers=getHeaders(),
		data={'first':False,'pn':page,'kd':'自动化测试工程师'},
		timeout=10)
	#因为每页有15条数据所以对其进循环-需要配合json在线工具
	for i in range(0,15):
		city = r.json()['content']['positionResult']['result'][i]['city']
		education = r.json()['content']['positionResult']['result'][i]['education']
		workYear = r.json()['content']['positionResult']['result'][i]['workYear']
		positionAdvantage = r.json()['content']['positionResult']['result'][i]['positionAdvantage']
		salary = r.json()['content']['positionResult']['result'][i]['salary']
		companyFullName = r.json()['content']['positionResult']['result'][i]['companyFullName']
		positionLables = r.json()['content']['positionResult']['result'][i]['positionLables']
		#西写入参数
		position={
			'公司名称': companyFullName,
			'城市': city,
			'学历': education,
			'工作年限': workYear,
			'薪资': salary,
			'工作标签': positionLables,
			'福利': positionAdvantage}
		positions.append(position)
		return positions

#保存数据写数据
def writeCsv():
	headers = {'公司名称', '城市', '学历', '工作年限', '薪资', '工作标签', '福利'}
	for item in range(1.31):
		positons=laGou(page=item)
		with open('login.csv','a',newline='',encoding='gbk') as f:
		writee=csv.DictWriter(f,headers)
		writer.writeheader()
		writer.writerows(positons)

writeCsv()


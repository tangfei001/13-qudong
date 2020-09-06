#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 14:15
# @Author  : Aries
# @Site    : 
# @File    : 08-csvTest3.py
# @Software: PyCharm
'''
说明:csv文件的写入(结合案例进行讲解)
'''
import csv
import requests

'''通过接口测试的技术获取拉钩网平台的资料'''
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def getHeaders():
	'''写一个函数获得请求头'''
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Cookie':'_ga=GA1.2.1237290736.1534169036; user_trace_token=20180813220356-b7e42516-9f01-11e8-bb78-525400f775ce; LGUID=20180813220356-b7e428ad-9f01-11e8-bb78-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFB3FA180CE47D5CD2C77E64B1B975127F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539433248,1539529521,1539785285,1540794503; _gid=GA1.2.675811712.1540794503; _gat=1; LGSID=20181029142824-d6b66331-db43-11e8-83f6-5254005c3644; PRE_UTM=; PRE_HOST=www.bing.com; PRE_SITE=https%3A%2F%2Fwww.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; SEARCH_ID=5e964af2d19e41f1903c1f4f5b41e1a5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540794522; LGRID=20181029142843-e1d2a63c-db43-11e8-83f6-5254005c3644',
		'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'
	}
	return headers

def laGou(page=2):
	#定义一个列表
	positons=[]
	#第一步:吧这个接口写全
	r=requests.post(url=url,
		headers=getHeaders(),
		data={'first':False,'pn':page,'kd':'自动化测试工程师'},
		timeout=10)
	#print(r.text)-拿到数据

	#第二步:对数据进行处理
	for i in range(0,15):
		'''
		city:城市
		education:学历
		workYear:工作年限
		salary:薪资
		companyFullName:公司名称
		positionLables:工作标签
		positionLables:福利
		'''
		city = r.json()['content']['positionResult']['result'][i]['city']
		education = r.json()['content']['positionResult']['result'][i]['education']
		workYear = r.json()['content']['positionResult']['result'][i]['workYear']
		salary = r.json()['content']['positionResult']['result'][i]['salary']
		companyFullName = r.json()['content']['positionResult']['result'][i]['companyFullName']
		positionLables = r.json()['content']['positionResult']['result'][i]['positionLables']
		positionLables = r.json()['content']['positionResult']['result'][i]['positionLables']
		#吧获取到的数据放到对应的字典中
		positon={'公司名称': companyFullName,
		         '城市': city,
		         '学历': education,
		         '工作年限': workYear,
		         '薪资': salary,
			     '工作标签': positionLables,
			     '福利': positionAdvantage
             	}
		#将数据写入到列表positions中
		positons.append(positon)
		#print(r.text)
		#对整个内容进行循环-看结果
	# for item in positons:
	# 	print(item)
	return positons

# if __name__ == '__main__':
#    for item in range(1,31):
# 	   laGou(page=item)
def writeCsv():
	#写title
	headers={'公司名称','城市','学历','工作年限','薪资','工作标签','福利'}
	#使用for循环拿到数据
	for item in range(1,31):
		positions=laGou(page=item)
		#写入数据
		with open('lagou.csv','a',newline='',encoding='gbk')as f:
			writer=csv.DictWriter(f,headers)
			writer.writeheader()
			writer.writerows(positions)

writeCsv()



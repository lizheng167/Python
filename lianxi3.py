# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
book_lists=[]
lists=[]
urls = ['http://www.qiushibaike.com/hot/page/{}/?s=4927830'.format(str(i)) for i in range(1,10,1)]

def spide(url):
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	wb_data = requests.get(url,headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	price = soup.select('div.article > a > div.content > span')
	for item in price:
		book_lists.append(item.text)
	return book_lists

if __name__=='__main__':
	for url in urls:
		lists=spide(url)
	print(lists)

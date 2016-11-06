# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)+'/?s=4927830'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    wb_data = requests.get(url,headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    print soup
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason 
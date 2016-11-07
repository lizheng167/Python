# -*- coding: utf-8
import re
import urllib2
import urllib
import MySQLdb
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request).read().decode('utf8')
soup = BeautifulSoup(response, 'html.parser')
url_lists = soup.find_all('a', href=re.compile(r'^/wiki/'))
# connect mysql
conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='111111',
    db='lianxi',
    charset='utf8'
)

# print url_lists
for url in url_lists:
    # 过滤jpg file
    if not re.search(r'\.(jpg|JPG)$', url.get('href')):
        print 'https://en.wikipedia.org' + url.get('href'), '<------>', url.get_text()
        try:
            cursor = conn.cursor()
            # 创建sql语句
            sql = 'insert into wiki_urls (url_name,url_href) values ("%s","%s")' % (
                url.get_text(), url.get('href'))
            print sql
            cursor.execute(sql)
            # commit
            conn.commit()
        except Exception as e:
            print 'Error', e
            conn.rollback()
conn.close()

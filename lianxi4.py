#-*- coding: UTF-8 -*-
import re
import requests

#匹配手机号，带+86和86的情况
def FindPhoneNumber(text):
    r = re.compile(r'((\+86|86)?1[358][0-9]{9})')
    L = r.findall(text)
    P = [x[0] for x in L]
    print(P)


#匹配合法的邮箱地址
def FindEmailAddress(text):
    r = re.compile(r'[\w.-]+@\w+\.[\w.-]+')
    L = r.findall(text)
    print(L)


#匹配httpurl          !!!有bug
def FindUrl(text):
    r= re.compile(r'((http://|https://)[a-zA-Z0-9]+[a-zA-Z0-9-/?.]+)')
    L = r.findall(text)
    U = [i[0] for i in L]
    print(U)


#匹配ip地址0.0.0.1-254.255.255.255
def FindIpAddress(text):
    r = re.compile(r'(((1\d\d|2[0-4]\d|25[0-5]|[1-9]?\d)\.){3}(2[0-4]\d|25[0-5]|1\d\d|[1-9]?[1-9])\b)')
    L = r.findall(text)
    I = [i[0] for i in L]
    print(I)


#匹配qq
def FindQQ(text):
    r = re.compile(r'([1-9]\d{4,})')
    L = r.findall(text)
    print(L)


#匹配日期，两种格式
def FindDate(text): #****/**/** ****-**-**
    r = re.compile(r'(\d{1,4}[/-](0?[1-9]|1[0-2])[/-](0?[1-9]|[12][0-9]|3[01])\b)')
    L = r.findall(text)
    D = [d[0] for d in L]
    print(D)


#匹配身份证号
def FindId(text):
    r = re.compile(r'\d{17}[0-9xX]|\d{15}')
    L = r.findall(text)
    print(L)


if __name__ == '__main__':
    phone = "18612147870 +8613920327207 77889"
    email = "zhangshna.Mr@163.com,abc_Wang.dd@sian.com,abc_Wang.dd.cc@sian.com zhangshan@163.com,abc@sina.com.cn 123456@jb51.net  web.blue@jb51.net web_blue@jb51.net web-blue@jb51.net "
    http = "https://www.hao123.com.cn http://www.baidu.com http://我.com https://4.-.-.- https://https://1.2..3.4 https://shark.douyucdn.cn/shark/lib/css/base/1.0/base.css?160114 www.sohu.com"
    ip = "111.111.111.111 01.02.03.04 255.178.1.589 1.1.1.0 1.1.1.1"
    qq = "767212665 10000 9999 1 255647824"
    date = "1999/02/03 1/1/1 1994/10/30 7/1/66 2005-1-25"
    id = "192222187504161122 17833319850101222x"
    FindPhoneNumber(phone)
    #FindEmail(email)
    #FindUrl(http)
    #FindIpAddress(ip)
    #FindQQ(qq)
    #FindDate(date)
    #FindId(id)

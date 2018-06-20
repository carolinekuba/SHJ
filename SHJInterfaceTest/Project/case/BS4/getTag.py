#coding:utf-8
from bs4 import BeautifulSoup
import requests
r = requests.get('http://seller.saohuijia.com/#/')
#搜索首页后获取整个Html页面
c = r.content
#print c
#用html.parser解析html
soup = BeautifulSoup(c,"html.parser")
times = soup.find_all(class_= "msg")
for i in times:
    input = i
    print i.input.string

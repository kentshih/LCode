# -*- coding=UTF-8 -*-

import requests                       #用来爬取网页
from bs4 import BeautifulSoup         #用来解析网页
#我们的种子
seds = ["http://www.lagou.com/"]
sum = 0
#我们设定终止条件为：爬取到10000个页面时，就不玩了

while sum < 10000 :
    if sum < len(seds):
         r = requests.get(seds[sum])
         sum = sum + 1
         #提取结构化数据；做存储操作
         do_save_action(r)
         soup = BeautifulSoup(r.content)               
         urls = soup.find_all("href")  #解析网页所有的链接
         for url in urls:
              seds.append(url)
    else:
         break
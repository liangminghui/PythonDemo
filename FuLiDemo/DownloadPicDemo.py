#coding:utf - 8
#先行命令
#pip install beautifulsoup4
#pip install requests
import os
from bs4 import BeautifulSoup
import requests
import urllib

for pageindex in range(1,10):
    url='http://www.loldk.com/fm/f/a/adetail-5-'+str(pageindex)+'.html'
    req=requests.get(url)
    bs=BeautifulSoup(req.text.encode(req.encoding), "html.parser")
    for div in bs.find_all('div',class_='article-detail fr'):
        dir=div.find('p').string
        a=div.find('h3').a
        childurl='http://www.loldk.com'+a['href']
        childbs=BeautifulSoup(requests.get(childurl).text, "html.parser")
        for childa in childbs.find_all('a',class_='img_a'):
            imgurl=childa.img['src']
            curpath='D:\MyDocs\妹子'
            p, f = os.path.split(imgurl)
            if os.path.exists(curpath+'/'+f):
                print('['+f+']已存在~')
            else:
                urllib.request.urlretrieve(imgurl,curpath+'/'+f)
                print('['+f+']下载成功~')
        print('[' + dir + ']下载成功~')
    print('[第'+str(pageindex)+'页]全部下载成功~')
print('全部下载成功~')

import re
import requests
# import requests.packages.urllib3
import os

regX = 'objURL":"(.+?\.(?:jpg|jpeg|png))'
searchURL="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1485435366329_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="
line = 'EP01.mp4'
page = requests.get(searchURL + line).text
picURL = re.search(regX, page)
imgType = re.search("\.(?:jpg|jpeg|png)",picURL.group(1))
img = requests.get(picURL.group(1))
img = requests.get(picURL.group(1))
print (picURL.group(1))
print (imgType)

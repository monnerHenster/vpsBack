#!/usr/bin/python
import re
import requests
# import requests.packages.urllib3
import os
# requests.packages.urllib3.disable_warnings()

head = "{ \n\t\"file\":\"http://pao.iioo.pub/webVideo/"
videoList = open("/home/webVideo/videoList.txt","r")
videoList2json = videoList.readlines()
videoList2 = open("/home/webVideo/videoList.json","w")
videoList2.write("[")

regX = 'objURL":"(.+?\.(?:jpg|jpeg|png))'
searchURL="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1485435366329_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="
sum = ""
for line in videoList2json:
	line = line.strip('\n')
	sum = sum + head + line + "\",\n\t\"title\":\"" + line +"\",\n\t\"tracks\":[{\n\t\t\"file\":\"/home/webVideo/tracks/" + line.replace('mp4','srt') + "\",\n\t\t\"kind\":\"captions\"\n\t\t}],"
	line = line.replace(".mp4","")
	print (line)
	page = requests.get(searchURL + line).text
	picURL = re.search(regX, page)
	imgType = re.search("\.(?:jpg|jpeg|png)",picURL.group(1))
	line = line + imgType.group().encode('utf-8')
	sum = sum + "\n\t\"image\":\"http://pao.iioo.pub/webVideo/images/" + line + "\""
	img = requests.get(picURL.group(1))
	imgFile = open("/home/webVideo/images/" + line,"wb")
	imgFile.write(img.content)
	sum = sum + "\n},"
curr = sum[:-1]
videoList2.write(curr)
videoList2.write("]")
videoList.close()
videoList2.close()

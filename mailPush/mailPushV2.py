#!/usr/bin/python3
# coding:utf-8
# encoding: utf-8

import json
import re
import os
import requests
import time
import smtplib
import xml.etree.ElementTree as ET
from email.mime.text import MIMEText
from email.header import Header


def sendMailText(title, content, sender, receiver, serverip, serverport, username, pwd):
    
    msg = MIMEText(content, _subtype="plain", _charset="utf-8")    # 设置正文为符合邮件格式的HTML内容
    msg['Subject'] = Header(title, "utf-8")     # 设置邮件标题
    msg['From'] = sender                        # 设置发件人
    msg['To'] = receiver                        # 设置收件人
    
    s = smtplib.SMTP_SSL(serverip, serverport)      # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
    s.login(username, pwd)                      # 登陆邮箱
    s.sendmail(sender, receiver, msg.as_string())  # 发送邮件


if __name__ == "__main__":
    
    config = {
    "serverip": "smtp.gmail.com",             # 发件服务器IP
    "serverport":"465",                      # 发件服务器Port
    }
    
    title = "太上章更新了"
    body = "http://m.uuxs.net/book/0/615/index.html"

# oldDatefile = open("/home/mailPush/FictionOldDate.txt")
# oldDate = oldDatefile.read()
# oldDatefile.close()
# url = "http://m.uuxs.net/book/0/615/index.html"
# response = requests.get(url)
# response.encoding = 'gbk'
# regX = u'更新时间.<i>(.*)</i>'
# renewDate =  re.search(regX,response.text)

ntime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

# if renewDate.group(1) == oldDate :
    # print (ntime + "：没有更新")
# else :
    # print (ntime + "：更新了")
    # oldDatefile = open ("/home/mailPush/FictionOldDate.txt",'w')
    # oldDatefile.write(renewDate.group(1))
    # print ( renewDate.group(1) )
    # try:
        # sendMailText(title, body, config['from'], config['to'], config['serverip'], config['serverport'], config['username'], config['pwd'])
    # except:
        # print (ntime + "：邮件发送失败")
    # else:
        # print (ntime + "：邮件发送成功")

updateList = ET.ElementTree(file='/home/mailPush/updateList.xml')
for one in updateList.iter('web'):
    url = one.get('url')
    regX = one.get('regX')
    print (regX)
    date = one.get('date')
    name = one.get('name')
    encoding = one.get ('encoding')
    response = requests.get(url,headers = headers)
    response.encoding = encoding
    renewDate = re.search(regX,response.text)
    if renewDate.group(1) == date :
        print (ntime + "：" + name + "没有更新")
    else :
        print (ntime + "：" + name + "更新了")
        title = name +"：更新了"
        body = url
        try:
            mailSetRes = open("/home/mailPush/mailSetp.json")
            mailSet = json.load(mailSetRes)
            for p in mailSet['reciever']:
                sendMailText(title, body, mailSet['account'], p, config['serverip'], config['serverport'], mailSet['account'], mailSet['passwd'])
            mailSetRes.close()
        except:
            print (ntime + "：邮件发送失败")
        else:
            print (ntime + "：邮件发送成功")   
            one.set("date",renewDate.group(1))
updateList.write('/home/mailPush/updateList.xml',encoding='utf-8')
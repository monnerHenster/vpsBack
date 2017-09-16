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
    
    title = "视频更新"

videoList = open("/home/webVideo/videoList.txt","r")

videoList2json = videoList.read()

# print (type(videoList2json))

mailSetRes = open("/home/mailPush/mailSet.json")
mailSet = json.load(mailSetRes)

print (videoList2json)

for p in mailSet['reciever']:
    sendMailText(title, videoList2json, mailSet['account'], p, config['serverip'], config['serverport'], mailSet['account'], mailSet['passwd'])

mailSetRes.close()
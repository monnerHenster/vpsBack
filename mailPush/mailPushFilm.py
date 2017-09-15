#!/usr/bin/python3
# coding:utf-8
# encoding: utf-8

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
    "from": "monnerhenster@gmail.com",            # 发件人邮箱
    "to1": "incubator_g@outlook.com",             # 收件人邮箱
    "to2": "598059072@qq.com",             # 收件人邮箱
    "to3": "82627306@qq.com",             # 收件人邮箱
    "serverip": "smtp.gmail.com",             # 发件服务器IP
    "serverport":"465",                      # 发件服务器Port
    "username": "monnerhenster@gmail.com",        # 发件人用户名
    "pwd": "405289055"                 # 发件人密码
    }
    
    title = "视频更新"
    body = "http://m.uuxs.net/book/0/615/index.html"

videoList = open("/home/webVideo/videoList.txt","r")

videoList2json = videoList.read()

# print (type(videoList2json))

print (videoList2json)

sendMailText(title, videoList2json, config['from'], config['to1'], config['serverip'], config['serverport'], config['username'], config['pwd'])
sendMailText(title, videoList2json, config['from'], config['to2'], config['serverip'], config['serverport'], config['username'], config['pwd'])
sendMailText(title, videoList2json, config['from'], config['to3'], config['serverip'], config['serverport'], config['username'], config['pwd'])

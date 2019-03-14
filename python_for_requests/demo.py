#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests,codecs

url="https://www.baidu.com"

web_data=requests.get(url)
web_content=web_data.text

try:
    file=codecs.open('web.html','w','utf-8')
    file.write(web_content)
finally:
    file.close()
    input("please input enter!")
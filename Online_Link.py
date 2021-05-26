# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:57:34 2020

@author: User
"""

#網路連線
import urllib.request as request
src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode("utf - 8") #取得網站的原始碼(HTML,CSS,JS)
print(data)
    #串接,擷取公開資料

import urllib.request as request
import json
src = "https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as response:
    data = json.load(response) #利用json模組處理json資料格式
print(data)
    #串接,擷取公開資料
    
#取得公司名稱
clist = data["result"]["results"]
print(clist)
for company in clist:
    print(company["公司名稱"])
with open("Data.txt",mode = "w",encoding = "utf - 8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
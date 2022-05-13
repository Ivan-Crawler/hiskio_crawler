# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:41:01 2021

@author: Ivan
"""
import requests
import json
import pandas as pd
import time
import matplotlib.pyplot as plt

all_data = pd.DataFrame()
i = 0
doit = True
while doit:
    try:
        # 要抓取的網址
        url = 'https://api.hiskio.com/v2/courses?type=arrival&word=&tags=&status=ALL&level=ALL&page=' + str(i) + '&professions=0&free=0'
        #請求網站
        list_req = requests.get(url)
        #將整個網站的程式碼爬下來
        get_data = pd.DataFrame(json.loads(list_req.content)['data'])
        if len(get_data) == 0:
            doit = False
        else:
            all_data = pd.concat([all_data, get_data], axis=0)
    except:
        doit = False
    print('第'+str(i)+'頁')
    i =  i + 1
    time.sleep(2)
   
    
#進行資料分析
plt.figure(figsize=(20,10))

# 繪製圓點
plt.scatter(all_data['price'],all_data['duration'],
            # color= colorlist,
            s=50,
            alpha=0.5)
plt.title("課程價格分析圖",fontsize=30)#標題
plt.ylabel('課程時間（秒）',fontsize=20)#y的標題
plt.xlabel('課程定價',fontsize=20) #x的標題
plt.tight_layout()
# plt.savefig('意見領袖分析.png', dpi=300)
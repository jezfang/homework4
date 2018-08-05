
# 使用台北市公開資料[台北旅遊網景點資料]
# 使用者用捷運站名稱搜尋景點
# 將對應到的景點資訊儲存在檔案中

import urllib.request as request  
import json # 處理json資料格式 (javaScript Object Notation)
with request.urlopen("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5") as response:
     data=json.load(response)    #response.read().decode("utf-8")
klist=data["result"]["results"]
# for MRTname in klist:
#     print(MRTname["MRT"])
# for Titlename in klist:
#     print(Titlename["stitle"])
name=input("想查詢台北市各個捷運站週邊的景點嗎？"+"輸入想查詢的捷運站名＿＿＿＿＿")
print("_________________________________________")

n=0
for Total in klist:
#print(str(Total["MRT"])+str("：")+str(Total["stitle"]))
    if name == Total["MRT"]:
        print(str(Total["MRT"])+str(" - ")+str(Total["stitle"]))
        n+=1
#print(n)
print("_________________________________________")

if n==0:
    print("沒有找到輸入的站名..")
else:
    print(str("查詢結果總共有")+str(n)+str("筆資料："))

# 載入 pandas 模組
import pandas as pd
#資料索引 : pd.DataFrame(字典,index = 索引列表)
data = pd.DataFrame(
    {
        "name" : ["Amy","Chally","Nicle"],
        "salary" : [30000,60000,220123]
    },index = ["a","b","c"]
)
print(data)

#觀察資料
print("資料數量",data.size)
print("資料型狀(列,欄)",data.shape)
print("資料索引",data.index)

#取得列(Row/橫向)的Series資料 : 根據順序,根據索引
print("取得第二列",data.iloc[1],sep = "\n")
print("取得第c列",data.loc["c"],sep = "\n")

#取得欄(Column/直向)的Series資料 : 根據欄位的名稱
print("取得name欄位",data["name"],sep = "\n")
names = data["name"] #取得單維度Series資料
print("把name全轉成大寫",names.str.upper(),sep = "\n")
salarys = data["salary"] #取得薪水的平均值
print("薪水平均值",salarys.mean())

#建立新的欄位
data["revenue"] = [50000,20030,3] #data[新蘭為名稱] = 列表
print(data)
data["rank"] = pd.Series([3,6,1],index = ["a","b","c"]) #data[新欄位名稱] = Series 的資料
print(data)
data["cp"] = data["revenue"]/data["salary"]
print(data)

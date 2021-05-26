# 載入 pandas 模組
import pandas as pd
#資料索引
data = pd.Series([5,4,3,-2,7,4],index = ["a","b","c","d","e","f"]) #可以自改索引
print(data)

#觀察資料
print("資料型態 : ",data.dtype)
print("資料數量 : ",data.size)
print("資料索引 : ",data.index)

#取得資料 : 根據順序,根據索引
print(data[2], data[0])        #根據順續
print(data["e"], data["a"])    #根據索引

#數字運算 : 基本,統計,順序
print("最大值 : ",data.max())
print("總和 : ",data.sum())
print("標準差 : ",data.std())
print("中位數  : ",data.median())
print("最大的三個數 : ",data.nlargest(3))
print("最小的兩個數 : ",data.nsmallest(2))

#字串運算 : 基本,串接,搜尋,取代
data = pd.Series(["您好","Python","Pandas"])
print(data.str.lower())                   #改小寫
print(data.str.upper())                   #改大寫
print(data.str.len())                     #每個字串的長度
print(data.str.cat(sep = "@@"))           #把每個字串串起來
print(data.str.contains("P"))             #判斷是否有包含此字元
print(data.str.replace("您好","Hello"))   #取代
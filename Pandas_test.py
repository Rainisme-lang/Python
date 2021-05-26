# 載入 pandaa 模組
import pandas as pd
# 建立 Series
data = pd.Series([20,10,3])
# 基本 Series 操作
print(data)
print("Max",data.max())
print("Median",data.median())
data = data*2
print(data)
data = data == 20 # data 裡的資料找 20 裡面 int 會變成 bool
print(data)
data = data == 40
print(data)
data = data == False
print(data)

# 建立 DataFrame
data = pd.DataFrame(     # 長度要一樣
    {
        "name" : ["Amy","Nicle","Rain"],
        "salary" : [300,1000,2550] 
    }
)
# 基本 DataFrame 操作
print(data)

#取得特定欄位
print()
print(data["name"])
print()
print(data["salary"])
print()
print(data.iloc[0]) #印出第一列
print()
print(data.iloc[0:2]) #印出第一,二列

# 載入 Pandas 模組
import pandas as pd
#篩選練習 - Series
data = pd.Series([30,50,22])
condition = [True,False,True]
filtered = newData = data[condition]
print(data)
print(filtered)

data = pd.Series(["您好","Python","Pandas"])
condition = [False,True,True]
filtered = data[condition]
print(data)
print(filtered)
condition = data.str.contains("P")
print(condition)
filtered = data[condition]
print(filtered)

#篩選練習 - DataFrame
data = pd.DataFrame({
    "name" : ["Amy","Bob","Chall"],
    "salary" : [23233,333,929]
})
print(data)
condition = data["salary"] >= 4000
filtered = data[condition]
print(filtered)
condition = data["name"] == "Chall"
filtered = data[condition]
print(filtered)
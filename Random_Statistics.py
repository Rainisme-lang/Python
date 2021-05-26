#隨機模組
import random
#隨機選取
data = random.choice([1,5,6,10,20,3])
print(data)
data = random.sample([1,5,6,10,20,3],3)
print(data)
#隨機調換順序(洗牌)
data = [1,4,5,6,3,10]
random.shuffle(data)
print(data)
#隨機取亂數
data = random.random() #0.0 ~ 1.0 取亂數
print(data)
data = random.uniform(60,100) #60.0 ~ 100.0 取亂數
print(data)
#平均數 100,標準差 10,得到的資料多數在90 ~ 100 之間
data = random.normalvariate(100, 10)
print(data)

#統計模組
import statistics as stat
data = stat.mean([1,3,4,5,100])
print(data)
data = stat.median([1,3,4,5,100]) #會刪除極端數字(如 100)
print(data)
data = stat.stdev([1,3,4,5,100]) #標準差 (數字間差距大不大)
print(data)

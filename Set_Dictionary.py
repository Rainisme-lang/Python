#集合的運算
s1 = {3,4,5}
print(3 in s1)
print(10 in s1)
print(4 not in s1)
s2 = {4,5,6,7}
s3 = s1 & s2 #交集
print(s3)
s3 = s1 | s2 #聯集
print(s3)
s3 = s1 - s2 #差集
print(s3)
s3 = s1 ^ s2 #反交集
print(s3)
s = set("Holle") #把字串中的字拆解成集合:set(字串)
print(s)
print("H" in s)

#字典的運算
dic = {"apple" : "蘋果", "bug" : "蟲子"}
print(dic)
dic["apple"] = "小蘋果"
print(dic["apple"])
print(dic)
dic["cat"] = "貓貓"
print(dic)
print("apple" in dic) #判斷key是否存在
del dic["apple"] #刪除字典中鍵值對
print(dic)
dic = {x:x*2 for x in [1,2,3]} #從列表產生字典
print(dic)

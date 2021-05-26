#有序可變動列表 List
grades = [3,12,45,25,9,6,8]
print(grades)
print("grades[3] :",grades[3])
grades[3] = 18
print("grades[3] :",grades[3])
print(grades[1:4])
grades[1:4] = [] #連續刪除列表中從1到4(不包含)的資料
print(grades)
grades = grades + [7,67,21,10,51]
print(grades)
length = len(grades)
print(length)

data = [[3,4,5],[6,7,8]]
print(data)
print(data[0])
print(data[0][0])
data[0][0:2] = [5,5,5]
print(data[0])

#有序不可變動列表 Tuple
data = (3,4,5)
print(data)
data = ((3,4,5),(6,7,8))
print(data)
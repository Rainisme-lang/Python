file = open("data.txt",mode = "w",encoding = "utf - 8")
file.write("Holle_World\n世界你好")
file.close()

file = open("data.txt",mode = "r",encoding = "utf - 8")
read = file.read()
print(read)

with open("data.txt",mode = "w",encoding = "utf - 8") as file:
    file.write("你好世界\nHolle_World")
with open("data.txt",mode = "r",encoding = "utf - 8") as file:
    read = file.read()
print(read)

sum = 0
with open("data.txt",mode = "w",encoding = "utf - 8") as file:
    file.write("3\n25")
with open("data.txt",mode = "r",encoding = "utf - 8") as file:
    for line in file:
        sum = sum + int(line)
print(sum)

import json
with open("test.json",mode = "r",encoding = "utf - 8") as file:
    data = json.load(file)
print(data)
print("name: ",data["name"])
print("varsion: ",data["version"])
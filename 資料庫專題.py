# 解析 JSON 格式資料 取得文章的標題
import json

with open("觀光資訊資料庫.json",mode = "r",encoding = "utf - 8") as file:
    data = json.load(file)

word = ""

for item in data :
    word = word + item["Name"] + "\n"

file = open("data.txt",mode = "w",encoding = "utf - 8")
file.write(word)
file.close()
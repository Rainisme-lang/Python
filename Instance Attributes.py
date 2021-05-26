# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:55:47 2020

@author: User
"""
#Point 實體物件的設計 : 平面座標紹的點
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
#建立第一個實體物件
P1 = Point(3,4)
print(P1.x,P1.y)
#健力第二個實體物件
P2 = Point(5,6)
print(P2.x,P2.y)

#FullName 實體物件的設計 : 分開紀錄姓名資料的全名
class FullName:
    def __init__(self,first,last):
        self.first = first
        self.last = last

name1 = FullName("C.W.","Peng")
print(name1.first,name1.last)
name2 = FullName("T.Y.", "Lin")
print(name2.first, name2.last)

#Point 實體物件的設計:平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #定義實體方法
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX, targetY):
        return (((self.x - targetX)**2)+((self.y - targetY)**2))**0.5
p = Point(3,4)
p.show() #呼叫實體方法/函式
result = p.distance(0,0)
print(result)

#File 實體物件的設計 : 包裝檔案讀取的程式
class File:
    #初始化函式
    def __init__(self,name):
        self.name = name
        self.file = None #尚未開啟檔案 :初期是None
    def open_write(self):
        self.file = open(self.name ,mode = "w",encoding = "utf - 8")
    def write(self,s):
        return self.file.write(s)
    def open_read(self):
        self.file = open(self.name ,mode = "r",encoding = "utf - 8")
    def read(self):
        return self.file.read()

#讀取第一個檔案
f1 = File("data_1.txt")
f1.open_write()
f1.write(input("請輸入:"))
f1.open_read()
data = f1.read()
print(data)
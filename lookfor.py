# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:58:59 2022

@author: 11102196
"""
import sys
#%% Definition
def read_txt(path):
    with open(path,'r',encoding='utf-8') as f:
        log_line = f.readlines()
    return log_line

def compare(word,keyword):
    for i in word:
        if word in i:
            print(word)
#%% Definition
path=r'G:\PQAW_USB\123.txt'
keyword='USBSTOR\DISK&VEN__USB&PROD__SANDISK_3.2GEN1&REV_1.00'
word=read_txt(path)
compare(word,keyword)

# return times

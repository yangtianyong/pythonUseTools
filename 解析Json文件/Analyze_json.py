# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-04
    Update: ---
    Achieve:解析json文件
"""

import json
import re

path = "../case_file/Jsonfle.json"
path1 = "../case_file/new_Jsonfle.json"

# 使用json模块json.load
# load方法打印出来所有内容显示为一行，阅读不方便。
def loadJson(path):
    with open(path,'r') as file:
        data_json = json.load(file)
    #获取到json字符串后，有两种处理方法：
    #方法一：利用字典的形式进行字符串提取
    print(data_json["name"])
    #方法二：利用正则表达式进行字符串提取,()捕获组的概念，标记希望匹配成功后提取的部分
    print(re.findall(r"'name': '(\w*)'",str(data_json)))
    return data_json

#写一个Json文件 index参数让写入的json更容易阅读：将一行的内容分成多行
def wirte_Json(data):
    with open(path1,'w') as file:
        json.dump(data,file,indent=4)

'''
    注意load和loads区别
    注意dump和dumps区别
'''

if __name__ == '__main__':
    data_json = loadJson(path)
    wirte_Json(data_json)




# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-08
    Update: ---
    Achieve:正则表达式相关的内容
"""

import re
'''
    链接：
        https://docs.python.org/2/howto/regex.html
'''

'''
    元字符：
          .         匹配除换行符以外任意字符
          \w        匹配字母、数字、下划线
          \d        匹配数字
          \W        与\w相反
          \D        与\d相反
          |         a|b 匹配a或者b
          []        匹配任意其中一个字符
          [^]       匹配非字符组中的字符
          ^         定位符，从字符串起始开始匹配
          $         定位符，匹配到字符串最后位置
'''

'''
    量词：
          *         重复零次或者多次
          +         重复一次或以上
          ?         重复零次或一次
          {n}       重复n次
          {n,}      至少重复n次
          {n,m}     重复n到m次
'''

'''
    分组：
    链接：https://zhuanlan.zhihu.com/p/375659011
    用圆括号()括起来的正则表达式，匹配出来的内容表示一个分组
    (exp):把括号内的正则作为一个分组，系统自动分配组号，可以通过分组号引用该分组
    (?P<name>exp):定义一个命名分组，分组的正则是exp,通过分组名和分组号引用该分组
    正则表达式引擎会默认分配一个编号，从1开始
    可以通过引用分组的方式对重复出现的文本进行匹配
'''

string  = "现在是北京时间9点40分"
pattern = re.compile(r'\D*(\d{1,2})\D*(\d{1,2})\D*')
# pattern = re.compile(r'\D*(?P<hour>\d{1,2})\D*(?P<minute>\d{1,2})\D*')
result = pattern.match(string)
print(result.groups()[0])
# print(result.groupdict())

'''
    修饰符：
        i      不区分大小写
        g      全局匹配
        m      多行匹配
'''

'''
    re模块：
    链接：https://blog.csdn.net/guo_qingxia/article/details/113979135
        1>re.match(pattern,string,flags=0)
            flags: re.I 忽略大小写  re.M 多行模式
            
        2>re.complie(pattern)
            用于编译正则表达式，生成对象，供match()和search()使用
            
        3>re.search()
            扫描整个字符串并返回第一个成功的匹配，如果没有匹配，就返回一个None
            re.match()只匹配字符串的开始
            
        4>re.sub(pattern,repl,string,count=0,flags=0)
        
        5>re.split()
            
'''
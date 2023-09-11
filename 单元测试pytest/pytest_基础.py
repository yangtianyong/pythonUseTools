# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-11
    Update: ---
    Achieve:pytest单元测试基础
"""

'''
    链接：
    https://www.bilibili.com/video/BV1py4y1t7bJ/?p=2&vd_source=28247d63a7e882f81ab1a2e5e277cc2a
    python测试框架：unittest和pytest
    主要做什么：
        1、测试发现：从多个文件里面去找我们测试用例
        2、测试执行：按照一定的顺序和规则去执行，生成结果
        3、测试判断：通过断言判断预估结果和实际结果的差异
        4、测试报告：统计测试进度、耗时、通过率、生成测试报告等。
'''

'''
    pytest有许多强大的插件，实现很多的实用的操作
    pytest-html   生成html格式自动化测试报告
    pytest-ordering  用于改变测试用例的执行顺序
    allure-pytest 用于生成美观的测试报告
'''

'''
    使用pytest，默认的测试用例规则
        1、模块必须以test_或者_test结尾
        2、测试类必须以Test开头，不能有init方法
        3、测试方法必须以test开头
'''

'''
    pytest测试用例的运行方式
        1、主函数模式
        2、命令行模式
        3、通过读取pytest.ini配置文件运行
    参数详解：
        -s:表示输出调试信息，包括print打印的信息
'''
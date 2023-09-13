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
        1、主函数模式  运行所有、指定模块、指定目录
        2、命令行模式
        3、通过读取pytest.ini配置文件运行 -- 单元测试框架的核心配置文件，存放于项目的根目录 
                                      -- 编码 ANSI
                                      -- 改变pytest默认的行为
                                      -- 主函数模式运行和命令行模式运行都需要调取配置文件
    参数详解：
        -s:表示输出调试信息，包括print打印的信息
        -v:显示更详细的信息
        -n:多线程或分布式执行测试用例
        --reruns=2:失败的测试用例重复运行2次，-- UI自动化不稳定，没有加载完成等情况
        -x:只要有一个测试用例错误，则测试停止
        --maxfail=2:出现两个测试用例失败，则测试停止
        -k:只执行包含匹配到的字符串的测试用例
'''

'''
    执行顺序：
        测试用例从上到下排列的顺序
        改变默认的执行顺序：@pytest.mark.run(order=1)
'''

'''
    分组执行：
        例如冒烟用例，分布在各个模块里面
        pytest -vs -m "smoke"  -- 注意要与ini文件里smoke结合
        pytest -vs -m "smoke or normal"  --  可以同时执行smoke和normal
'''

'''
    测试用例跳过：
        无条件跳过：@pytest.mark.skip(reason="测试用例跳过")
        有条件跳过：@pytest.mark.skipif(填写的条件)
'''

'''
    生成测试报告：
        addopts = -vs  --html  ./report/report.html
'''

'''
    pytest框架实现一些前后置的处理，常用三种：
        setup/teardown,setup_class/teardown_class
    使用@pytest.fixture装饰器来实现部分用例的前后置 --  对其中部分的用例实现前后置
    fixture参数：
        scope表示的是被@pytest.fixture标记的方法的作用域 --function(默认) class  module  package  session
        params:参数化
        autouse=True:自动执行，默认为False
        ids:当使用params参数化时，给每一个值设置一个变量名
        name:表示给被标记的方法取一个别名
'''
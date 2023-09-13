# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-11
    Update: ---
    Achieve:pytest单元测试基础demo
"""

import pytest

class TestLogin:

    #在所有的用例之前执行一次
    def setup_class(self):
        print("在每个类执行前的初始化工作，比如创建日志对象，创建数据库链接等")

    #在每个用例之前执行一次
    def setup_method(self):
        print("在执行测试用例之前执行的代码：打开浏览器，加载网页等")

    @pytest.mark.run(order=2)
    @pytest.mark.normal
    def test02(self):
        print("测试用例运行2")

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    # @pytest.mark.skip(reason="测试用例跳过")
    def test01(self):
        print("测试用例运行1")

    def teardown_method(self):
        print("在执行测试用例之后的扫尾的代码：关闭浏览器")

    def teardown_class(self):
        print("在每个类执行后的扫尾的工作，比如：销毁日志对象等")


if __name__ == '__main__':

    # pytest.main()
    #执行所有的用例

    #输出调试信息和print打印信息
    # pytest.main(["-s"])

    #单独运行一个用例
    pytest.main(["-vs","test_pydemo01.py"])

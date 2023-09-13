# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-11
    Update: ---
    Achieve:pytest单元测试基础demo
"""

import pytest

@pytest.fixture(scope="module",autouse=True)
def my_fixture():
    print("可以实现部分以及全部用例的前置")
    yield
    print("后置方法")

class Test_demo02:

    @pytest.mark.smoke
    def test01(self):
        print("测试用例运行demo02")


    @pytest.mark.smoke
    def test02(self,my_fixture):
        print("测试用例运行demo04")

class Test_demo03:

    @pytest.mark.smoke
    def test01(self):
        print("测试用例运行demo022")


    @pytest.mark.smoke
    def test02(self,my_fixture):
        print("测试用例运行demo042")
# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-11
    Update: ---
    Achieve:pytest单元测试基础demo
"""

import pytest

class TestLogin:

    @pytest.mark.run(order=2)
    def test02(self):
        print("测试用例运行2")

    @pytest.mark.run(order=1)
    def test01(self):
        print("测试用例运行1")

if __name__ == '__main__':

    # pytest.main()
    #执行所有的用例

    #输出调试信息和print打印信息
    # pytest.main(["-s"])

    #单独运行一个用例
    pytest.main(["-vs","test_pydemo01.py"])

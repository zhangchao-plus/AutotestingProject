# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/13 上午 11:11
# File  : test_para.py


import pytest

@pytest.mark.parametrize("key,result",
                         [["appium",200],["selenium",200],["request",200]],
                         ids=['a','b','c'])
def test_interface(key,result):
    url = f"http://ceshiren.com/key={key}"
    print(url,result)


@pytest.mark.parametrize('a',["int","float","string"])
@pytest.mark.parametrize("b",[1,2,3])
def test_ab(a, b):
    print(a,b)

@pytest.mark.parametrize("a,b",
                         [[1,1],[0.1,0.1],[1000,1000]])
class TestDemo():
    def test_add(self,a,b):
        print(a+b)
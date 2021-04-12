# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/12 下午 09:50
# File  : test_add.py

from pytestdemo.Calculator import Calculator

class TestCal():
    def setup(self):
        print("调用setup方法")
        self.calc = Calculator()

    def test_add1(self):
        assert 2 == self.calc.add(1, 1)

    def test_add2(self):
        assert 0.2 == self.calc.add(0.1, 0.1)
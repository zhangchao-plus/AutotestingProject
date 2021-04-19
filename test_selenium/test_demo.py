# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/16 下午 01:34
# File  : test_demo.py


from selenium import webdriver

class TestWework():
    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.url = "https://www.baidu.com"
        self.driver.implicitly_wait(30)


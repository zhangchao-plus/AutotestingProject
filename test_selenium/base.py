# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/24 下午 09:45
# File  : base.py
from selenium import webdriver
class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

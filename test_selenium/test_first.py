# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/19 上午 11:24
# File  : test_first.py

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class TestBaiduSearch():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com"
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_baidusearch(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID,"kw").click()
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID,"su").click()
        assert_text = self.driver.find_element(By.LINK_TEXT ,"霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert assert_text
        sleep(3)
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/24 下午 09:20
# File  : test_window.py
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_selenium.base import Base

class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "s-top-loginbtn").click()
        root = self.driver.current_window_handle
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        window_handles = self.driver.window_handles
        self.driver.switch_to_window(window_handles[-1])
        sleep(5)
        self.driver.switch_to_window(root)
        sleep(5)
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("18702888141")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("5113241@ilove")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()










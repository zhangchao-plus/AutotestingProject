# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/19 下午 09:49
# File  : test_actionchains.py
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_moveto_element(self):
        # 悬停在百度首页的设置上；
        moveto_setting = self.driver.find_element(By.CSS_SELECTOR, "#s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(moveto_setting).perform()
        # 点击搜索设置
        self.driver.find_element(By.LINK_TEXT, "搜索设置").click()
        sleep(5)
        # 点击保存设置
        self.driver.find_element(By.LINK_TEXT, "保存设置").click()
        sleep(5)
        # 点击确认按钮
        self.driver.switch_to.alert.accept()

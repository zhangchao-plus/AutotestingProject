
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/19 下午 12:15
# File  : test_wait.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1040)
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        wait_el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@title="有了新帖的活动主题"]')))
        wait_el.click()
        self.driver.find_element(By.XPATH, "//*[@title='在最近的一年，一月，一周或一天最活跃的主题']").click()
        print("测试完成")

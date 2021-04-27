# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/04/27 下午 12:12
# File  : test_alert.py
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from test_selenium.base import Base

class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        drag_el = self.driver.find_element(By.XPATH, '//*[@id="draggable"]')
        drop_el = self.driver.find_element(By.XPATH, '//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_el,drop_el).perform()
        sleep(2)
        self.driver.switch_to_alert().accept()



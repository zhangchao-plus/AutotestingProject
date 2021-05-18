# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: 笨笨笨啊啊啊
# Date  : 2021/05/16 上午 12:06
# File  : test_search.py
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestAppium():
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.main.view.MainActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset':True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        """
        查询阿里巴巴股票，并判断是否大于200；
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text ='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName' and @text ='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        print(current_price)
        assert current_price >= 200

    def test_touchacton(self):
        """
        使用TouchAction()函数滑动手机页面
        """
        action = TouchAction(self.driver)
        window_rct = self.driver.get_window_rect()
        width = window_rct["width"]
        height = window_rct["height"]
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(1000).move_to(x=x1, y=y_end).release().perform()


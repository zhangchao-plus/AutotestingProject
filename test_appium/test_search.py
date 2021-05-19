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

    def test_get_price(self):
        """
        使用Xpath节点获取阿里巴巴-sw的股价
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text ='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(current_price)
        assert current_price >= 200

    def test_login(self):
        """
        UiSelector()定位：
        1、点击我的，进入用户信息页面；
        2、点击账号密码登录，进入登录页面；
        3、输入账号，密码，点击登录；
        """
        # 使用resourceId和text组合定位，并点击我的
        loc_my = 'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")'
        self.driver.find_element_by_android_uiautomator(loc_my).click()
        # 使用text定位，并点击帐号密码登录
        loc_login = 'new UiSelector().text("帐号密码登录")'
        self.driver.find_element_by_android_uiautomator(loc_login).click()
        # 输入账号
        loc_account = 'new UiSelector().resourceId("com.xueqiu.android:id/login_account")'
        self.driver.find_element_by_android_uiautomator(loc_account).send_keys("18702888141")
        # 输入密码
        loc_password = 'new UiSelector().resourceId("com.xueqiu.android:id/login_password")'
        self.driver.find_element_by_android_uiautomator(loc_password).send_keys("abc@1234")
        # 点击登录
        loc_button = 'new UiSelector().resourceId("com.xueqiu.android:id/button_next")'
        self.driver.find_element_by_android_uiautomator(loc_button).click()
        # 获取登录失败文本
        login_error_text = self.driver.find_element_by_id("com.xueqiu.android:id/md_content").text
        print(login_error_text)





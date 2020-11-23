#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_dwpytest.py
# Author: yaojunjie
# Date  : 2020/11/13
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:

    def setup(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            # "dontStopAppOnReset": True,  # 启动时不停止app
            "skipDeviceInitialization": True,  # 跳过安装、权限等设置操作
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_search(self):
        """
        1.打开雪球app
        2.点击搜索框，
        3.在搜索框内输入腾讯，点击搜索
        4.获取腾讯股价，判断股价大于200
        """
        print("搜索测试用例")
        el = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el1.send_keys("腾讯")
        el2 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='腾讯控股']")
        el2.click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    def test_attr(self):
        """
        打开[雪球]应用app
        定位首页搜索框
        判断搜索框是否可用，并查看搜索康name值
        打印搜索框这个元素左上角坐标和它的宽高
        像搜索框输入腾讯
        判断“腾讯”是否可见
        如果可见，打印搜索成功 反之打印搜索失败
        """
        el = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = el.is_enabled()
        print(el.text)
        print(el.location)
        print(el.size)
        if search_enabled:
            el.click()
            el1 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
            el1.send_keys("腾讯")
            el2 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='腾讯控股']")
            if el2.get_attribute("displayed") == 'true':
                print("success")
            else:
                print("fail")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()  # 获取屏幕大小
        height = window_rect['height']
        width = window_rect['width']
        action.press(x=width / 2, y=int(height * 4 / 5)).wait(200).move_to(x=width / 2,
                                                                           y=int(height * 1 / 5)).release().perform()

    def test_get_current(self):
        '''
        xpath定位
        '''
        el = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el1.send_keys("阿里巴巴")
        el2 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el2.click()
        c_price = self.driver.find_element_by_xpath(
            "//*[@text=09988]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(float(c_price))
        assert float(c_price) > 200

    def test_hamcrest(self):
        assert_that(10, equal_to(10), "这是一个提示")
        assert_that(8, close_to(10, 2))  # true
        assert_that(12, close_to(10, 2))  # true
        assert_that(13, close_to(10, 2))  # false
        assert_that("yao", contains_string("y"))

    pytest.mark.parametrize('search_key, type, price', [
        ('alibaba', 'BaBA', 180),
        ('xiaomi', '01810', 10),
    ])

    def test_param(self, search_key, number, price):
        """
        参数化
        1.打开雪球app
        2.点击搜索框，
        3.在搜索框内输入阿里巴巴或者小米等等，点
        4.点击第一个搜索结果
        5.判断股票价格
        """
        self.driver.find_elemen(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").click().send_keys(search_key)
        self.driver.find_elemen(MobileBy.ID, "com.xueqiu.android:id/name").click()
        c_price = float(self.driver.find_element(
            MobileBy.XPATH,
            f"//*[@text='{number}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        assert_that(c_price, close_to(price, price * 0.1))
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/actin_close").click()


class TestBrowser:

    def setup(self):
        desc_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "browserName": "Browser",
            "noReset": True,
            # "chromedriverExecutable": "C:/Program Files/Appium/chromedriver" # 屏蔽后放到默认路径
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desc_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        locator1 = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator1))
        self.driver.find_element(*locator1).click()


class TestWebView:

    def setup(self):
        desc_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "noReset": True,
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "skipServerInstallation": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desc_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        # 点击交易
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        locator = (MobileBy.XPATH, "//*[@id='Layout_app_3V4']/div/div/ul/li[1]/div[2]/h1")
        print(self.driver.contexts)
        # 切换上下文，切换到webview
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击A股开户
        # print(self.driver.window_handles)
        WebDriverWait(self.driver, 120).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        # 跳转到window
        # print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 输入用户名和验证码，点击立即开户
        locator1 = (MobileBy.ID, "phone-number")
        WebDriverWait(self.driver, 120).until(expected_conditions.element_to_be_clickable(locator1))
        self.driver.find_element(*locator1).send_keys("13265803556")
        self.driver.find_element(MobileBy.ID, "code").send_keys("1234")
        self.driver.find_element(MobileBy.CSS_SELECTOR, "body > div > div > div.form-wrap > div > div.btn-submit").click()


if __name__ == '__main__':
    pytest.main("-v")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_dwpytest.py
# Author: yaojunjie
# Date  : 2020/11/13
from time import sleep

import pytest
from appium import webdriver


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


if __name__ == '__main__':
    pytest.main("-v")
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
from appium.webdriver.extensions.android.gsm import GsmCallActions
from hamcrest import *


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
            "resetKeyBoard": True,
            "avd": "Pixel_23_6"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_api(self):
        self.driver.make_gsm_call("13265803553", GsmCallActions.CALL)
        self.driver.send_sms("13265803553", "hello")
        self.driver.set_network_connection(type=2)
        self.driver.get_screenshot_as_file('./photos/img.png')
        # 录屏
        self.driver.start_recording_screen()
        self.driver.stop_recording_screen()


if __name__ == '__main__':
    pytest.main("-v")

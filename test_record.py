#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_recording.py
# Author: yaojunjie
# Date  : 2020/11/10
from appium import webdriver

desired_cap = {
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True,
  "dontStopAppOnReset": True,   # 启动时不停止app
  "skipDeviceInitialization": True  # 跳过安装、权限等设置操作
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)
el = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el.click()
el1 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el1.send_keys("腾讯")
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                   ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android"
                                   ".widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget"
                                   ".RecyclerView/android.widget.RelativeLayout[1]")
el2.click()
driver.back()  # 返回上一级页面
driver.quit()

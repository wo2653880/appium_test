#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : maplocal.py
# Author: yaojunjie
# Date  : 2020/12/21
import json

from mitmproxy import http


def response(flow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        data = json.loads(flow.response.content)
        data["a"] = "aa"  # 修改指定字段
        print(json.dumps(data, indent=4))
        flow.response.text = json.dumps(data)

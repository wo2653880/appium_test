#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : maplocal.py
# Author: yaojunjie
# Date  : 2020/12/21

from mitmproxy import http


def request(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,
            b"Hello Word",
            {"Content-Type": "text/html"}
        )

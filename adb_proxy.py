#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : adb_proxy.py
# Author: yaojunjie
# Date  : 2020/11/22
"""
mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/ -s adb_proxy.py
"""
from mitmproxy.utils import strutils
from mitmproxy import ctx
from mitmproxy import tcp


def tcp_message(flow: tcp.TCPFlow):
    message = flow.message[-1]
    old_content = message.content
    message.content = old_content.replace(b"@webview_devtools_remote_", b"@.*.*.*._devtools_remote_")
    ctx.log_info(
        "[tcp_message{}] from {} to {}:\n{}".format(
            "(modified)" if message.content != old_content else "",
            "client" if message.from_client else "server",
            "server" if message.from_client else "client",
            strutils.bytes_to_escaped_str(message.content))
    )

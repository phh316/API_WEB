#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/3/8
# @Author : Ph
# @File : test_remote.py

from async_test_func import test_search, test_login
from async_test_cls import AsyncTestMain, AsyncTestLogin
from async_main import main_cls, main_func
from caps_setting import *

chrome_url = r'http://localhost:9515'
firefox_url = r'http://localhost:4444'


test_suit_func = [
    ([test_login, ], chrome_url, CHROME_CAPS)
]

# test_suit_func = [
#     ([test_login, ], chrome_url, CHROME_CAPS),
#     ([test_search, ], chrome_url, CHROME_CAPS_2),
#     ([test_search, ], firefox_url, FIREFOX_CAPS)
# ]

# test_suit_cls = [
#     ([AsyncTestLogin, ], chrome_url, CHROME_CAPS),
#     # ([AsyncTestMain, ], chrome_url, CHROME_CAPS_2),
#     ([AsyncTestMain, ], firefox_url, FIREFOX_CAPS)
# ]

main_func(test_suit_func)
# main_cls(test_suit_cls)
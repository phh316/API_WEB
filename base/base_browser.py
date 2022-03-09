#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/18
# @Author : Ph
# @File : base_browser.py

from selenium.webdriver import *
from typing import Type, Union
from selenium.webdriver.chromium.options import ChromiumOptions
from resources.settings import *


class BrowserTypeError(Exception):

    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f"  未知的浏览器类型： {self._type}"


class BROWSER:
    """浏览器基类"""
    CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
    IE_DRIVER_PATH = IE_DRIVER_PATH
    FIREFOX_DRIVER_PATH = FIREFOX_DRIVER_PATH
    OPERA_DRIVER_PATH = OPERA_DRIVER_PATH
    EDGE_DRIVER_PATH = EDGE_DRIVER_PATH
    PAGE_LOAD_TIME = PAGE_LOAD_TIME
    IMP_TIME = IMP_TIME
    SCRIPT_TIME_OUT = SCRIPT_TIME_OUT
    HEADLESS = HEADLESS

    def __init__(self,
                 browser_type: Type[Union[Firefox, Chrome, Ie, Opera, Edge, Safari]] = Chrome,
                 browser_option: Type[Union[FirefoxOptions, ChromeOptions, IeOptions, EdgeOptions]] = ChromeOptions,
                 browser_path: str = CHROME_DRIVER_PATH):
        if not issubclass(browser_type, (Firefox, Chrome, Ie, Opera, Edge, Safari)):
            raise BrowserTypeError(browser_type)
        if not issubclass(browser_option, (FirefoxOptions, ChromeOptions, IeOptions, EdgeOptions)):
            raise BrowserTypeError(browser_option)
        if not isinstance(browser_path, str):
            raise TypeError
        self._browser = browser_type
        self._path = browser_path
        self._option = browser_option


class CHROME(BROWSER):
    """谷歌浏览器"""
    OPTION_MARK = CHROME_OPTION_MARK
    METHOD_MARK = CHROME_METHOD_MARK
    START_MAX = CHROME_START_MAX
    WINDOWS_SIZE = WINDOWS_SIZE
    EXP = CHROME_EXP
    HEADLESS = HEADLESS
    PAGE_LOAD_TIME = PAGE_LOAD_TIME
    IMP_TIME = IMP_TIME
    SCRIPT_TIME_OUT = SCRIPT_TIME_OUT

    @property
    def option(self):
        if self.OPTION_MARK:
            chrome_option = self._option()
            assert isinstance(chrome_option, ChromiumOptions)
            chrome_option.add_argument(self.START_MAX)
            for k, v in self.EXP.items():
                chrome_option.add_experimental_option(k, v)
            chrome_option.headless = self.HEADLESS
            return chrome_option
        return None

    @property
    def browser(self):
        if self.option:
            chrome = self._browser(self._path, options=self.option)
        else:
            chrome = self._browser(self._path)
        if self.METHOD_MARK:
            chrome.set_script_timeout(self.SCRIPT_TIME_OUT)
            chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
            chrome.implicitly_wait(self.IMP_TIME)
        return chrome


class IE(BROWSER):

    #清空缓存
    CLEAN_SESSION = True
    IE_MARK = IE_MARK
    IE_ATTACH_TIME = IE_ATTACH_TIME

    """IE浏览器基类"""
    def __init__(self):
        super(IE, self).__init__(
            browser_path=super().IE_DRIVER_PATH,
            browser_type=Ie,
            browser_option=IeOptions

        )

    @property
    def option(self):
        if self.IE_MARK:
            ie_option = self._option()
            ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        ie_browser = self._browser(self._path,options=self.option)
        ie_browser.set_script_timeout(self.SCRIPT_TIME_OUT)
        ie_browser.set_page_load_timeout(self.IE_ATTACH_TIME)
        ie_browser.implicitly_wait(self.IMP_TIME)
        ie_browser.maximize_window()
        return ie_browser



with IE().browser as _chrome:
    _chrome.get('https://www.fastmock.site/#/login')
    from time import sleep
    sleep(5)

# with CHROME().browser as _chrome:
#     _chrome.get('https://www.fastmock.site/#/login')
#     from time import sleep
#     sleep(5)

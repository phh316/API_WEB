#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/8
# @Author : Ph
# @File : base_page2.py
from resources.settings import *
from common.reader import YamlReader
from base.base_browser import *


class Page:
    url = None
    locators = {}
    browser = CHROME()

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser.browser

    def __getattr__(self, loc):
        if loc not in self.locators.keys():
            raise Exception
        by, val = self.locators[loc]
        return self.driver.find_element(by, val)


class CommonLoginPage(Page):
    url = PROJECT_URL
    locators = YamlReader(YML_ELEMENT['cp']).data

    def get(self):
        self.driver.get(self.url)

    def login(self,name: str = 'admin',pwd: str = 'Phh8238112'):
        self.username.send_keys(name)
        self.password.send_keys(pwd)
        self.loginBtn.click()


class MainPage(CommonLoginPage):
    CommonLoginPage.locators.update(
        YamlReader(YML_ELEMENT['sp']).data
    )

    def search(self,bug_id:str ='1'):
        self.searchInput.send_keys(bug_id)
        self.searchGo.click()

    def login_out(self):
        self.username.click()
        self.exit.click()
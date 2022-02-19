#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/19
# @Author : Ph
# @File : base_page.py
from base.base_browser import CHROME, IE


class Page:
    """基类页面"""
    url = None
    locators = {}
    browser = CHROME

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browser

    def __getattr__(self, item):
        if item not in self.locators:
            raise Exception
        by, val = self.locators[item]
        return self.driver.find_element(by, val)


class CommonLoginPage(Page):
    url = 'http://127.0.0.1/zentao/user-login.html'
    locators = {
        'username': ('id', 'account'),
        'password': ('name', 'password'),
        'loginBtn': ('id', 'submit')
    }

    def get_url(self):
        return self.driver.get(self.url)

    def login(self, username: str = 'admin', password: str = 'Phh8238112'):
        self.username.send_keys(username)
        self.password.send_keys(password)
        if isinstance(self.driver,CHROME):
            self.loginBtn.click()
        else:
            from selenium.webdriver.common.keys import Keys
            self.password.send_keys(Keys.ENTER)


class MainPage(CommonLoginPage):
    CommonLoginPage.locators.update({
        'searchInput': ('id', 'searchInput'),
        'searchGo': ('id', 'searchGo'),
        'user_name': ('xpath', '//span[@class="user-name"]'),
        'bug_label': ('xpath', '//span[@class="label label-id"]')
    })

    def search_bug(self, bug_id: str = '1'):
        self.searchInput.send_keys(bug_id)
        self.searchGo.click()


# class TestMain:
#
#     def test_login(self):
#         page = MainPage()
#         page.get_url()
#         page.login()
#         assert page.user_name.text == 'admin'
#         print('test login is ok')
#         page.driver.quit()

    # def test_search(self):
    #     page = MainPage()
    #     page.get_url()
    #     page.login()
    #     page.search_bug()
    #     assert page.bug_label.text == '1'
    #     print('test search is ok')
    #     page.driver.quit()


# obj = TestMain()
# obj.test_login()
# # obj.test_search()

#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/3/8
# @Author : Ph
# @File : async_test_cls.py
from time import sleep


class Base:

    def __init__(self,driver):
        self.async_driver = driver

    async def get(self, url: str = r'http://127.0.0.1/zentao/user-login.html'):
        await self.async_driver.get(url)


class LoginPage(Base):

    async def login(self, username: str = 'admin', password: str = 'Phh8238112'):
        await self.async_driver.send_keys('id', 'account', text=username)
        await self.async_driver.send_keys('name', 'password', text=password)
        await self.async_driver.click('id', 'submit')


class MainPage(LoginPage):

    async def search(self, text: str = '1'):
        await self.async_driver.send_keys('id', 'searchInput', text=text)
        await self.async_driver.click('id', 'searchGo')

    async def logout(self):
        await self.async_driver.click('class', 'user-name')
        await self.async_driver.click('xpath', '//a[text()="退出"]')


class AsyncTestLogin(MainPage):

    async def test_login(self, *args):
        await self.get()
        sleep(1)
        await self.login(*args)
        sleep(1)
        assert await self.async_driver.find_element('xpath', '//span[@class="user-name"]')
        await self.logout()
        sleep(1)


class AsyncTestMain(MainPage):

    async def test_search(self, text: str = '1'):
        await self.get()
        sleep(1)
        await self.login()
        sleep(1)
        await self.search(text)
        sleep(1)
        assert await self.async_driver.text('xpath', '//span[@class="label label-id"]') == text
        await self.logout()
        sleep(1)
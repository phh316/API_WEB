#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/3/7
# @Author : Ph
# @File : async_test_func.py
from asyncio import sleep


async def get(async_driver, url: str = r'http://127.0.0.1/zentao/user-login.html'):
    await async_driver.get(url)


async def login(async_driver, username: str = 'admin', password: str = 'Phh8238112'):
    await async_driver.send_keys('id', 'account', text=username)
    await async_driver.send_keys('name', 'password', text=password)
    await async_driver.click('id', 'submit')


async def search(async_driver, text: str = '1'):
    await async_driver.send_keys('id', 'searchInput', text=text)
    await async_driver.click('id', 'searchGo')


async def logout(async_driver):
    await async_driver.click('class', 'user-name')
    await async_driver.click('xpath', '//a[text()="退出"]')


async def test_login(async_driver):
    await get(async_driver)
    await sleep(2)
    await login(async_driver)
    await sleep(2)
    assert await async_driver.find_element('xpath', '//span[@class="user-name"]')
    await sleep(2)
    await logout(async_driver)


async def test_search(async_driver, text: str = '1'):
    await get(async_driver)
    await sleep(2)
    await login(async_driver)
    await sleep(2)
    await search(async_driver, text)
    await sleep(2)
    assert await async_driver.text('xpath', '//span[@class="label label-id"]') == text
    await sleep(2)
    await logout(async_driver)

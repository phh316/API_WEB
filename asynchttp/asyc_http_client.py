#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/3/5
# @Author : Ph
# @File : asyc_http_client.py
from aiohttp import ClientSession
from selenium.webdriver.remote.errorhandler import ErrorCode, ErrorHandler


class Command:

    _error_handler = ErrorHandler()

    async def command(self, method: str, url: str, session: ClientSession, **kwargs):
        async with session.request(method=method, url=url, **kwargs) as resp:
            status_code = resp.status
            """重定向"""
            if 300 <= status_code < 304:
                return self.command('GET', resp.headers.get('location', ''), session)
            res = await resp.json()
            """请求问题"""
            if 399 < status_code <= 500:
                res['status'] = status_code
            """success"""
            if 199 < status_code < 300:
                res['status'] = ErrorCode.SUCCESS
            else:
                res['status'] = ErrorCode.UNKNOWN_ERROR
            self._error_handler.check_response(res)
            return res['value']


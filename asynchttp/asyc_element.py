#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/3/5
# @Author : Ph
# @File : asyc_element.py

from asynchttp.asyc_http_client import Command


class Element(Command):

    def __init__(self,element, url, session):
        """
        :param element: {element:elementid}
        :param url: http://ip:port/session/session_id
        :param session:
        """
        self.element = list(element.values())[0]
        self.url = url
        self.session = session
        self.api = f'{self.url}/element/{self.element}'
        self.session_id = self.url.split('/')[-1]

    async def command(self, method: str, endpoint: str, **kwargs):
        return await super(Element,self).command(method,self.api+endpoint,self.session,**kwargs)

    async def send_keys(self,*keys):
        json = {
            'text':''.join(keys)
        }
        return await self.command('POST','/value',json=json)

    async def text(self):
        return await self.command('GET', '/text')

    async def click(self):
        json = {
            'id':self.element,
            'sessionId':self.session_id
        }
        return await self.command('POST', '/click',json=json)

    async def clear(self):
        json = {
            'id': self.element,
            'sessionId': self.session_id
        }
        return await self.command('POST', '/clear',json=json)

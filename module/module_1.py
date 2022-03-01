#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/27
# @Author : Ph
# @File : module_1.py
import unittest
from base.base_pase import MainPage


class M1(unittest.TestCase,MainPage):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_get()
        cls.cls_login()
        assert cls.cls_element('sp.user_name').text == 'admin'
        print('test_login is ok')

    def test_0_0(self):
        print("----------------")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()





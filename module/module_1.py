#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/27
# @Author : Ph
# @File : module_1.py
import unittest
from unittest import skipIf, skip, skipUnless


class M1(unittest.TestCase):

    @skip("用户密码不能为空")
    def test_a(self):
        print(f"222")

    @skipIf(1 == 1, "用户名等于张三")
    def test_b(self):
        print(f"2333")

    @skipUnless(1 == 10, "条件为假")
    def test_c(self):
        print(f"444")



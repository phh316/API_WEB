#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/28
# @Author : Ph
# @File : reader.py
from os.path import exists
from yaml import safe_load, safe_load_all


class File:

    def __init__(self, file_path: str):
        if not exists(file_path):
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlReader(File):

    def __init__(self, yml_path: str, multi: bool = False):
        super(YamlReader, self).__init__(yml_path)
        self._multi = multi

    @property
    def data(self):
        if not self._data:
            with open(self._file_path, 'rb') as f:
                if self._multi:
                    self._data = list(safe_load_all(f))
                else:
                    self._data = safe_load(f)
        return self._data

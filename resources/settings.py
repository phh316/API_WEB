#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/2/17
# @Author : Ph
# @File : settings.py
from typing import List
import os

"""文件路径"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOUDLE_DIR_PATH = os.path.join(BASE_DIR, '../module')
REPORT_DIR_PATH = os.path.join(BASE_DIR, '../report')
REPORT_FILE_PATH = r'\\report.html'

'''模块1 测试套件'''
SUIT_MODULE_1 = ['module_1.py','module_2.py']

'''测试主模块'''
SUIT_PROJRCT: List[str] = SUIT_MODULE_1


'''浏览器驱动路径'''
CHROME_DRIVER_PATH = '../drivers/chrome_driver_v97.exe'
EDGE_DRIVER_PATH = '../drivers/edge_driver.exe'
FIREFOX_DRIVER_PATH = '../drivers/gecko_driver.exe'
IE_DRIVER_PATH = '../drivers/IEDriverServer3.9.exe'
OPERA_DRIVER_PATH = '../drivers/opera_driver.exe'

'''浏览器属性'''

'''浏览器启动尺寸'''
WINDOWS_SIZE = (1024, 768)
'''隐式等待时间'''
IMP_TIME = 30
'''页面加载时间'''
PAGE_LOAD_TIME = 30
'''js执行异步超时时间'''
SCRIPT_TIME_OUT = 30
'''无头化'''
HEADLESS = False

#chrome 属性
'''操作开关'''
CHROME_OPTION_MARK = True
'''方法开关'''
CHROME_METHOD_MARK = True
'''窗口最大化'''
CHROME_START_MAX = '--start-maximized'
'''启动参数'''
CHROME_EXP = {
    'excludeSwitches': ['enable-automation','load-extension'],
    'prefs':{
        'credentials_enable_service': False,
        'profile': {
         'password_manager_enabled': False
        }
    },
}

#ie参数
'''启动参数开关'''
IE_MARK = True
'''清空本地会话'''
IE_CLEAN_SESSION = True
'''页面超时时间'''
IE_ATTACH_TIME = 30
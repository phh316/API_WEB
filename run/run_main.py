import unittest
import os,sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from resources.settings import MOUDLE_DIR_PATH,SUIT_PROJRCT,REPORT_DIR_PATH,REPORT_FILE_PATH
from common.HTMLTestRunner import HTMLTestRunner
file_path = REPORT_DIR_PATH+REPORT_FILE_PATH
#创建测试套件实例
suite = unittest.TestSuite()
#初始化加载器
loader = unittest.defaultTestLoader
#加载测试对象
for test in SUIT_PROJRCT:
    test_suits = loader.discover(start_dir=MOUDLE_DIR_PATH,pattern=test)
    suite.addTest(test_suits)

if os.path.exists(file_path):
    os.remove(file_path)
with open('../report/report.html', 'wb') as f:
    runner = HTMLTestRunner(f, title='自动化测试报告', verbosity=2)
    runner.run(suite)
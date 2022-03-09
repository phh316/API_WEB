#!/usr/bin/env python
# -- coding: utf-8 --
# @Date : 2022/3/8
# @Author : Ph
# @File : caps_setting.py

CHROME_CAPS = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'chrome',
            'platformName': 'any',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            },
            'goog:chromeOptions': {
                'excludeSwitches': ['enable-automation','load-extension'],
                'args': [
                    '--start-maximized',
                ],
                'prefs': {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False
                }
            }
        }
    }
}

CHROME_CAPS_2 = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'chrome',
            'platformName': 'any',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            },
            'goog:chromeOptions': {
                'excludeSwitches': ['enable-automation', 'load-extension'],
                'prefs': {
                    # 禁用密码保存弹框
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False
                }
            }
        }
    }
}

FIREFOX_CAPS = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'firefox',
            'platformName': 'windows',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 30000,
                'script': 30000
            }
        }
    }
}

IE_CAPS = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'ie',
            'platformName': 'windows',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            }
        }
    }
}
# 页面属性封装（url，浏览器实例，元素，操作）
# 页面调用（页面继承, 页面实例化）
# 基于页面调用可以有两种实现方式

from resources.settings import *
from base.base_browser import CHROME
from common.reader import YamlReader


class Page:
    url = None
    driver = None
    elements_yml = None

    # 缓存读取结果
    elements_pool = {}

    def _locator(self, expr: str = 'cp.username'):
        """解析元素表达式的方法 """
        name, value = expr.split('.')
        if name not in self.elements_yml:
            raise Exception('元素配置别名:{}未找到'.format(name))
        if name not in self.elements_pool:
            self.elements_pool[name] = YamlReader(self.elements_yml[name]).data
            if (locator := self.elements_pool[name][value])[0] not in BY_RULES:
                raise Exception(
                    f'未知的元素定位方式 :{self.elements_pool[name][value]}'
                )
            return locator
        return self.elements_pool[name][value]

    @classmethod
    def cls_locator(cls, expr: str = 'cp.username'):
        """解析元素表达式的方法 """
        name, value = expr.split('.')
        if name not in cls.elements_yml:
            raise Exception('元素配置别名:{}未找到'.format(name))
        if name not in cls.elements_pool:
            cls.elements_pool[name] = YamlReader(cls.elements_yml[name]).data
            if (locator := cls.elements_pool[name][value])[0] not in BY_RULES:
                raise Exception(
                    f'未知的元素定位方式 :{cls.elements_pool[name][value]}'
                )
            return locator
        return cls.elements_pool[name][value]

    @classmethod
    def cls_element(cls, loc: str):
        """
        定位元素的方法
        :param loc:
        :return:
        """
        return cls.driver.find_element(*cls.cls_locator(loc))

    def element(self, loc: str):
        """
        定位元素的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*self._locator(loc))

    def elements(self, loc: str):
        """
        定位一组元素或多个元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*self._locator(loc))


class CommonLoginPage(Page):
    url = PROJECT_URL
    driver = CHROME().browser
    elements_yml = YML_ELEMENT


    @classmethod
    def cls_get(cls):
        """
        类方法,打开首页
        :return:
        """
        cls.driver.get(cls.url)

    def get(self):
        """
        打开首页地址
        :return:
        """
        self.driver.get(self.url)

    @classmethod
    def cls_login(cls, username: str = 'admin', password: str = 'Phh8238112'):
        cls.cls_element('cp.username').send_keys(username)
        cls.cls_element('cp.password').send_keys(password)
        cls.cls_element('cp.loginBtn').click()

    def login(self, username: str = 'admin', password: str = 'Phh8238112'):
        self.element('cp.username').send_keys(username)
        self.element('cp.password').send_keys(password)
        self.element('cp.loginBtn').click()


class MainPage(CommonLoginPage):

    def search_bug(self, bug_id: str = '1'):
        self.element('sp.searchInput').send_keys(bug_id)
        self.element('sp.searchGo').click()
        assert self.element('sp.bug_label').text == '1'

    def login_out(self):
        self.element('sp.user_name').click()
        self.element('sp.log_out').click()


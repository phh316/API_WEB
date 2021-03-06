# 页面属性封装（url，浏览器实例，元素，操作）
# 页面调用（页面继承, 页面实例化）
# 基于页面调用可以有两种实现方式

# from setting import *
from page.base_page import CHROME


class Page:
    url = None
    driver = None

    @classmethod
    def cls_element(cls, loc: tuple):
        return cls.driver.find_element(*loc)

    def element(self, loc: tuple):
        """
        定位元素的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)

    def elements(self, loc: tuple):
        """
        定位一组元素或多个元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*loc)


class CommonLoginPage(Page):
    url = 'http://127.0.0.1/zentao/user-login.html'
    driver = CHROME().browser
    username = ('id', 'account')
    password = ('name', 'password')
    loginBtn = ('id', 'submit')


    @classmethod
    def cls_get(cls):
        """
        类方法,打开首页
        :return:
        """
        cls.driver.get(cls.url)

    @classmethod
    def cls_login(cls, username: str = 'admin', password: str = 'Phh8238112'):
        cls.cls_element(cls.username).send_keys(username)
        cls.cls_element(cls.password).send_keys(password)
        cls.cls_element(cls.loginBtn).click()

    def get(self):
        """
        打开首页地址
        :return:
        """
        self.driver.get(self.url)

    def login(self, username: str = 'admin', password: str = 'admin123456'):
        self.element(self.username).send_keys(username)
        self.element(self.password).send_keys(password)
        self.element(self.loginBtn).click()


class Search(CommonLoginPage):
    searchInput = ('id', 'searchInput')
    searchGo = ('id', 'searchGo')
    user_name = ('xpath', '//span[@class="user-name"]')
    bug_label = ('xpath', '//span[@class="label label-id"]')
    log_out = ('xpath', '//a[text()="退出"]')

    def search_bug(self, bug_id: str = '1'):
        self.element(self.searchInput).send_keys(bug_id)
        self.element(self.searchGo).click()
        assert self.element(self.bug_label).text == '1'
        print("检索完成")

    def login_out(self):
        self.element(self.user_name).click()
        self.element(self.log_out).click()

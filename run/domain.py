import unittest
from page.base_page import Search
from time import sleep

data = (
    {'name': 'admin', 'pwd': 'Phh8238112', 'ass': 'admin', 'text': 'admin login success'},
    {'name': '001', 'pwd': 'Phh8238112', 'ass': 'zhansan', 'text': '001 login success'},
    {'name': '002', 'pwd': 'Phh8238112', 'ass': 'lisi1', 'text': '002 login success'}
)


class MyTestCase(unittest.TestCase, Search):
    def test_login(self):
        for _ in data:
            with self.subTest(_):
                self.get()
                self.login(_['name'], _['pwd'])
                print(self.element(self.user_name).text)
                assert self.element(self.user_name).text == _['ass'], \
                    self.driver.save_screenshot(f'./{_["ass"]}.png')
                print(_['text'])
                self.login_out()
                sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)

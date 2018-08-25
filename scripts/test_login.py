from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_username("13800138006")
        self.page.login.input_password("123456")
        self.page.login.click_login()
        assert self.page.login.is_toast_exist("登录成功")

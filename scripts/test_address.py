from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        # 点击我的
        self.page.home.click_mine()
        # 判断是否登录
        if not self.page.mine.is_login():  # 如果没有登录
            # 登录
            self.page.mine.click_login_sign_up()
            self.page.login.login()

        # 点击收货地址
        self.page.mine.click_address()


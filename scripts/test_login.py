import time

import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_sign_up()
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(password)
    #     self.page.login.click_login()
    #     assert self.page.login.is_toast_exist(expect)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        username = args["username"]
        password = args["password"]

        self.page.home.click_mine()
        self.page.mine.click_login_sign_up()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        assert not self.page.login.is_login_button_enabled()


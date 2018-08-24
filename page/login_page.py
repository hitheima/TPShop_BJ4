from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 用户名
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    # 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    # 登录
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self, text):
        self.input(self.username_edit_text, text)

    def input_password(self, text):
        self.input(self.password_edit_text, text)

    def click_login(self):
        self.click(self.login_button)
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 用户名
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    # 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    # 登录
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach("用户名：", text)
        self.input(self.username_edit_text, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach("密码：", text)
        self.input(self.password_edit_text, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)

    def is_login_button_enabled(self):
        return self.is_location_enabled(self.login_button)

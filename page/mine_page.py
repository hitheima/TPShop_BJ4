import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MinePage(BaseAction):

    login_sign_up_button = By.ID, "com.tpshop.malls:id/nickname_txtv"

    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"

    title_text_view = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    # 收货地址
    address_button = By.XPATH, "//*[@text='收货地址']"

    @allure.step(title="点击登录/注册")
    def click_login_sign_up(self):
        self.click(self.login_sign_up_button)

    def click_setting(self):
        self.click(self.setting_button)

    def is_login(self):
        self.click_setting()
        is_login = not self.find_element(self.title_text_view).text == "登录"
        self.press_back()
        return is_login

    def click_address(self):

        if self.is_location_exist_scroll_page(self.address_button):
            self.click(self.address_button)



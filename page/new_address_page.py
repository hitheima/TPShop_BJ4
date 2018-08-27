from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewAddressPage(BaseAction):
    # 收货人
    name_exit_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"
    # 手机号
    mobile_exit_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"
    # 地址
    address_exit_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"
    # 区域
    region_text_view = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    def click_region(self):
        self.click(self.region_text_view)

    def input_name(self, text):
        self.input(self.name_exit_text, text)

    def input_mobile(self, text):
        self.input(self.mobile_exit_text, text)

    def input_address(self, text):
        self.input(self.address_exit_text, text)
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

        if self.page.mine.is_location_exist_scroll_page(self.page.mine.address_button):
            # 点击收货地址
            self.page.mine.click_address()
            self.page.address.click_new_address()
            self.page.new_address.input_name("itcast")
            self.page.new_address.input_mobile("18500002222")
            self.page.new_address.input_address("5单元203")
            self.page.new_address.click_region()
            # 选择城市
            self.page.region.click_city()
            # 选择城市的确定
            self.page.region.click_commit()
            # 保存收货地址
            self.page.new_address.click_save_address()
            assert self.page.address.is_toast_exist("添加成功")

        else:
            assert False

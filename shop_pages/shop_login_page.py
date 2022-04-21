from .shop_base_page import BaseShopPage
from .shop_locators import LoginForm


class ShopLoginPage(BaseShopPage):
    def register_new_user(self, email, password):
        self.browser.find_element(
            *BasePageLocators.MAIL_ADDRESS).send_keys(email)
        self.browser.find_element(
            *BasePageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(
            *BasePageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(
            *BasePageLocators.REGISTRATION_SUBMIT).click()


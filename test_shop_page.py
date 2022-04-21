import pytest
import faker

from .shop_pages.shop_base_page import ShopBasePage
from .shop_pages.shop_login_page import ShopLoginPage
from .shop_pages.shop_locators import LoginForm

SHOP_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


class TestUserAddToBasket:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = SHOP_LINK
        page = ShopLoginPage(browser, link)
        page.open()
        fake = faker.Faker()
        page.register_new_user(fake.email(), fake.fname())
        print(fake.fname())


import pytest
import allure
from pages.cart_page import cart_page
from pages.main_page import main_page


@allure.epic('WEB.Add product to cart')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking whether a product has been added to cart")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestCart:

    @allure.title("Adding and removing a book to cart")
    def test_item_add_and_delete_cart(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Book search"):
            cart_page.find_item()
        with allure.step("Open product page"):
            cart_page.open_page_item()
        with allure.step("Click add to cart"):
            cart_page.click_add_to_cart()
        with allure.step("Open cart"):
            cart_page.open_cart()
        with allure.step("Clear cart"):
            cart_page.clear_cart()
        with allure.step("Confirm clear cart"):
            cart_page.confirm_clear_cart()
        with allure.step("Assert text cart"):
            cart_page.assert_page_cart()

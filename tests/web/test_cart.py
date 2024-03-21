import pytest
import allure
from my_shop_project_test.pages.cart_page import cart
from my_shop_project_test.pages.main_page import main


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
            main.open_shop_page()
        with allure.step("Book search"):
            cart.find_item()
        with allure.step("Open product page"):
            cart.open_page_item()
        with allure.step("Click add to cart"):
            cart.click_add_to_cart()
        with allure.step("Open cart"):
            cart.open_cart()
        with allure.step("Clear cart"):
            cart.clear_cart()
        with allure.step("Confirm clear cart"):
            cart.confirm_clear_cart()
        with allure.step("Assert text cart"):
            cart.assert_page_cart()

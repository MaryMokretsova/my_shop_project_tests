import pytest
import allure
from my_shop_project_test.pages.favorite_page import favorite
from my_shop_project_test.pages.main_page import main


@allure.epic('WEB.Add product to favorites')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking whether a product has been added to favorites")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestFavorites:
    @allure.title("Adding and removing a book to favorites")
    def test_item_add_and_delete_favorites(self):
        with allure.step("Open marketplace"):
            main.open_shop_page()
        with allure.step("Number book search"):
            favorite.find_item()
        with allure.step("Open product page"):
            favorite.open_page_item()
        with allure.step("Click add to favorites"):
            favorite.click_add_to_favorites()
        with allure.step("Open favorites"):
            favorite.open_favorites()
        with allure.step("Click delete to favorites"):
            favorite.click_delete_to_favorites()
        with allure.step("Assert text favorites"):
            favorite.assert_page_favorites()

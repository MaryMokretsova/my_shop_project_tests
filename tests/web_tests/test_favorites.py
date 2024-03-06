import allure
from pages.favorite_page import favorite_page
from pages.main_page import main_page


@allure.epic('WEB.Add product to favorites')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking whether a product has been added to favorites")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
class TestFavorites:
    @allure.title("Adding and removing a book to favorites")
    def test_item_add_and_delete_favorites(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Number book search"):
            favorite_page.find_item()
        with allure.step("Open product page"):
            favorite_page.open_page_item()
        with allure.step("Click add to favorites"):
            favorite_page.click_add_to_favorites()
        with allure.step("Open favorites"):
            favorite_page.open_favorites()
        with allure.step("Click delete to favorites"):
            favorite_page.click_delete_to_favorites()
        with allure.step("Assert text favorites"):
            favorite_page.assert_page_favorites()
            
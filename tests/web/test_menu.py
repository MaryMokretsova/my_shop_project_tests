import pytest
import allure
from my_shop_project_test.pages import main_page


@allure.epic('WEB.Menu')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking menu items")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestMenu:

    def test_main_menu(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Checking first level menu items"):
            main_page.assert_header_main_menu()
        with allure.step("Checking second level menu items"):
            main_page.assert_body_main_menu()
        with allure.step("Checking third level menu items"):
            main_page.assert_footer_main_menu()

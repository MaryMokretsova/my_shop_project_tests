import pytest
import allure
from pages import main_page
from pages import search_page


@allure.epic('WEB.Search Page')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking an successful and an unsuccessful search")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestSearch:

    def test_header_search_positive(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Input text for search"):
            search_page.header_search('Тетради')
        with allure.step("Check the result of an successful search"):
            search_page.search_result_success('Тетради')

    def test_header_search_negative(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Input text for search"):
            search_page.header_search('asddfgrhtjykykk')
        with allure.step("Check the result of an unsuccessful search"):
            search_page.search_result_failure('По вашему запросу ничего не найдено. Возможно, вам понравятся эти ')

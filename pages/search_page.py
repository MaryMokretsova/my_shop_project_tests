from selene import browser, have
import time


class SearchPage:

    def header_search(self, text):
        browser.element('[class*="_input_vn1tc_35"]').type(text).press_enter()
        time.sleep(5)

    def search_result_success(self, text):
        browser.element('[class*="h1"] [class="title"]').should(have.text(text))

    def search_result_failure(self, text):
        browser.element('[class*="search-type"] [class="search-type__text"]').should(have.text(text))


search_page = SearchPage()

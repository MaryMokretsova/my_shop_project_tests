from selene import browser, have


class MainPage:

    def open_shop_page(self):
        browser.open("/")
        return self

    def assert_header_main_menu(self):
        browser.element('[href*="/my/partner"]').should(have.text('Партнёрам'))
        return self

    def assert_body_main_menu(self):
        browser.element('[aria-label="Майшоп.Гид рекомендует"]').should(
            have.text('Майшоп.Гид рекомендует'))
        return self

    def assert_footer_main_menu(self):
        browser.element('[class*="footer__copyright"]').should(
            have.text('Все права защищены © 2002-2024 Майшоп'))
        return self


main_page = MainPage()

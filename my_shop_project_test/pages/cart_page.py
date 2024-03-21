from selene import browser, have


class CartPage:

    def find_item(self):
        browser.element("[placeholder='Поиск на Майшоп']").type(
            "Complete Brambly Hedge"
        ).press_enter()
        return self

    def open_page_item(self):
        browser.element('[class="img"]').click()
        return self

    def click_add_to_cart(self):
        browser.element('[class*="field flex-grow"] [class*="_button_vas"]').click()
        return self

    def open_cart(self):
        browser.element('[href*="/my/cart"]').click()
        return self

    def clear_cart(self):
        browser.element('[class*="icon icon__delete"]').click()
        return self

    def confirm_clear_cart(self):
        browser.element(
            ' [class*="cart-confirm__btns"] [class*="_button_vas41_1 _is-medium_vas41_75 _is-basic_vas41_174 nowrap"]'
        ).click()
        return self

    def assert_page_cart(self):
        browser.element('[class*="text-20"]').should(
            have.text('Ваша корзина пуста')
        )
        return self


cart = CartPage()

from selene import browser, have


class CartPage:

    def find_item(self):
        browser.element('[class*="_input_vn1tc_35"]').type(
            "Complete Brambly Hedge"
        ).press_enter()
        return self

    def open_page_item(self):
        browser.element('[class*="container"] [class="item__title"]').click()
        return self

    def click_add_to_cart(self):
        browser.element("._label_ogzmc_28").click()
        return self

    def open_cart(self):
        browser.element('[class*="tabs-button orange"]').click()
        return self

    def clear_cart(self):
        browser.element('[class*="icon icon__delete"]').click()
        return self

    def confirm_clear_cart(self):
        browser.element(
            ' [class*="cart-confirm__btns"] [class*="_is-basic_ogzmc_174 nowrap"]'
        ).click()
        return self

    def assert_page_cart(self):
        browser.element('[class*="cart-empty__header"]').should(
            have.text('Ваша корзина пуста')
        )
        return self


cart_page = CartPage()

from selene import browser, have


class FavoritePage:

    def find_item(self):
        browser.element('[class*="_input_vn1tc_35"]').type(
            "Python для детей. Самоучитель по программированию"
        ).press_enter()
        return self

    def open_page_item(self):
        browser.element('[class*="container"] [class="item__title"]').click()
        return self

    def click_add_to_favorites(self):
        browser.element('[class*="form-control"] [class*="is-heart _icon"]').click()
        return self

    def open_favorites(self):
        browser.element('[class*="favorite"]').click()
        return self

    def click_delete_to_favorites(self):
        browser.element('[class*="field"] [class*="is-heart"]').click()
        return self

    def assert_page_favorites(self):
        browser.element('[class*="cart-empty__header"]').should(
            have.text("Избранных товаров нет")
        )
        return self


favorite_page = FavoritePage()

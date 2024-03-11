from selene import browser, have


class FavoritePage:

    def find_item(self):
        browser.element('[class*="_input_vn1tc_35"]').type(
            "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
        ).press_enter()
        return self

    def open_page_item(self):
        browser.element('[class*="container"] [class="item__title"]').click()
        return self

    def click_add_to_favorites(self):
        browser.element('[class*="form-control"] [class*="is-heart _icon"]').click()
        return self

    # '[aria-label="Добавить в избранное"]'

    def open_favorites(self):
        browser.element('[class*="favorite"]').click()
        return self

    def click_delete_to_favorites(self):
        browser.element('[class*="field"] [class*="is-heart"]').click()
        return self

    def assert_page_favorites(self):
        browser.element('[class*="text-20"]').should(
            have.text("Избранных товаров нет")
        )
        return self


favorite_page = FavoritePage()

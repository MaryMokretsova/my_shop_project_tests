from selene import browser, have, be


class LoginPage:

    def open_form(self):
        browser.element('[href*="#"]').click()
        return self

    def assert_name_form(self, value):
        browser.element('[class="h2"]').should(have.text(value))
        return self

    def log_in_with_password(self):
        browser.element(
            '[class*="_button_vas41_1 _is-large_vas41_100 _is-white-violet_vas41_246 _is-border_vas41_254 nowrap _is-expanded_vas41_194"]').click()
        return self

    def fill_user_email(self, value):
        browser.element('[type="email"]').should(be.blank).type(value)
        return self

    def fill_password(self, value):
        browser.element('[type="password"]').should(be.blank).type(value)
        return self

    def submit_the_form(self):
        browser.element(
            '[class*="_button_vas41_1 _is-large_vas41_100 _is-basic_vas41_174 nowrap _is-expanded_vas41_194"]').type('Войти').press_enter()
        return self

    def assert_authorization(self):
        browser.element('.otp__h1').should(have.text('Мой кабинет'))
        return self


login = LoginPage()

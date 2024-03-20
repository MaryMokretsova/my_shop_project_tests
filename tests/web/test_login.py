import pytest
import allure
from pages.login_page import login_page
from pages.main_page import main_page
import config


@allure.epic('WEB.Authorized')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking the authorization of the user")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestFavorites:
    @allure.title("Verifying successful user authorization")
    def test_authorization_registered_user(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Open the authorization form"):
            login_page.open_form()
        with allure.step("Assert name the authorization form"):
            login_page.assert_name_form('Вход и регистрация')
        with allure.step("Open the authorization form with email"):
            login_page.log_in_with_password()
        with allure.step("Filling the authorization form"):
            login_page.fill_user_email()
            login_page.fill_password()
        with allure.step("Submit the form"):
            login_page.submit_the_form()
        with allure.step("Checking that user has been authorized"):
            login_page.assert_authorization()


@allure.epic('WEB.Authorized')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking the authorization of the user")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestFavorites:
    @allure.title("Verifying unsuccessful user authorization")
    def test_authorization_unregistered_user(self):
        with allure.step("Open marketplace"):
            main_page.open_shop_page()
        with allure.step("Open the authorization form"):
            login_page.open_form()
        with allure.step("Assert name the authorization form"):
            login_page.assert_name_form('Вход и регистрация')
        with allure.step("Open the authorization form with email"):
            login_page.log_in_with_password()
        with allure.step("Filling the authorization form"):
            login_page.fill_user_email(config.settings.USER_EMAIL)
            login_page.fill_password()
        with allure.step("Submit the form"):
            login_page.submit_the_form()
        with allure.step("Assert name the authorization form"):
            login_page.assert_name_form('Вход и регистрация')
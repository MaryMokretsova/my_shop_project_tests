import pytest
import allure
from my_shop_project_test.pages.login_page import login
from my_shop_project_test.pages.main_page import main
import config


@allure.epic('WEB.Authorized')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking the authorization of the user")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@pytest.mark.web
class TestAuthorization:
    @allure.title("Verifying successful user authorization")
    def test_authorization_registered_user(self):
        with allure.step("Open marketplace"):
            main.open_shop_page()
        with allure.step("Open the authorization form"):
            login.open_form()
        with allure.step("Assert name the authorization form"):
            login.assert_name_form('Вход и регистрация')
        with allure.step("Open the authorization form with email"):
            login.log_in_with_password()
        with allure.step("Filling the authorization form"):
            login.fill_user_email(config.settings.USER_EMAIL)
            login.fill_password(config.settings.PASSWORD)
        with allure.step("Submit the form"):
            login.submit_the_form()
        with allure.step("Checking that user has been authorized"):
            login.assert_authorization()

    @allure.title("Verifying unsuccessful user authorization")
    def test_authorization_unregistered_user(self):
        with allure.step("Open marketplace"):
            main.open_shop_page()
        with allure.step("Open the authorization form"):
            login.open_form()
        with allure.step("Assert name the authorization form"):
            login.assert_name_form('Вход и регистрация')
        with allure.step("Open the authorization form with email"):
            login.log_in_with_password()
        with allure.step("Filling the authorization form"):
            login.fill_user_email(config.settings.USER_EMAIL)
            login.fill_password('123')
        with allure.step("Submit the form"):
            login.submit_the_form()
        with allure.step("Assert name the authorization form"):
            login.assert_name_form('Вход и регистрация')

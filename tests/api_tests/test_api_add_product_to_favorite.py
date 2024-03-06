import allure
import jsonschema
from helper.load_schema import load_schema
from helper.api_requests import api_put


@allure.epic('API. Add product to favorites')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking whether a product has been added to favorites")
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_adding_product_to_favorite():
    schema = load_schema('successful_adding_product_to_favorite.json')

    with allure.step("Send a request to add a product to favorites"):
        url = f"/shop2.pl?q=add_cart&quantity=1&product_id=4913578&save=1"
        data = {"quantity": 1}
        headers = {"Content-Type": "application/json"}
        result = api_put(url, headers=headers, data=data)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()['save']['4913578'] == 1
        assert result.json()['total']['quantity'] == 1


@allure.epic('API. Get data about product in favorite')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking a product in favorite")
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_adding_product_to_favorite():
    schema = load_schema('get_info_product_in_favorite.json')

    with allure.step("Send a request to receive your favorite products"):
        url = f"/shop2.pl?q=cart"
        headers = {"Content-Type": "application/json"}
        result = api_put(url, headers=headers)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()['save'][0]['ga_item']['quantity'] == 1
        assert result.json()['save'][0]['ga_item']['id'] == 4913578

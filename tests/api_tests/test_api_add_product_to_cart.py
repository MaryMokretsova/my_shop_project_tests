import allure
import jsonschema
from helper.load_schema import load_schema
from helper.api_requests import api_put


@allure.epic('API. Add product to cart')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking whether a product has been added to cart")
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_adding_product_to_cart():
    schema = load_schema('successful_adding_product_to_cart.json')

    with allure.step("Send a request to add a product to cart"):
        url = f"/shop2.pl?q=add_cart&quantity=1&product_id=4875742"
        data = {"quantity": 1}
        headers = {"Content-Type": "application/json"}
        result = api_put(url, headers=headers, data=data)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()['cart']['4875742'] == 1
        assert result.json()['total']['quantity'] == 1


import json
import requests
from allure_commons.types import AttachmentType
import logging
import allure


BASE_URL = 'https://api.my-shop.ru/cgi-bin'


def api_get(url, **kwargs):
    with allure.step("API Request"):
        result = requests.get(url=BASE_URL + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result


def api_put(url, **kwargs):
    with allure.step("API Request"):
        result = requests.put(url=BASE_URL + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result

import logging
from urllib.parse import urljoin

from jsonschema import validate
from register_3_step.requests import Client
from register_3_step.models import ResponseModel

logger = logging.getLogger("api")


class SwaggerStore:
    def __init__(self):
        self.client = Client()

    URL = 'https://stores-tests-api.herokuapp.com'
    POST_REGISTER_USER = '/register'
    POST_AUTH_USER = '/auth'
    POST_USER_INFO = '/user_info/'
    _STORE = '/store/'
    POST_STORE_ITEM = '/item/'
    GET_ALL_ITEMS = '/items'

    def register_user(self, body: dict, schema: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.client.custom_request("POST", urljoin(self.URL, self.POST_REGISTER_USER), json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def auth_user(self, body: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth
        """
        response = self.client.custom_request("POST", urljoin(self.URL, self.POST_AUTH_USER), json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def add_user_info(self, user_id, body: dict, schema: dict, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        url_add_user_info = urljoin(self.URL, self.POST_USER_INFO)
        response = self.client.custom_request("POST", urljoin(url_add_user_info, str(user_id)),
                                              headers={"Authorization": f"JWT {token}"}, json=body)

        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def add_new_store(self, store, body, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        url_add_new_store = urljoin(self.URL, self._STORE)
        response = self.client.custom_request("POST", urljoin(url_add_new_store, str(store)),
                                              headers={"Authorization": f"JWT {token}"},
                                              json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_store(self, store, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        url_get_store = urljoin(self.URL, self._STORE)
        response = self.client.custom_request("GET", urljoin(url_get_store, str(store)),
                                              headers={"Authorization": f"JWT {token}"})
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def post_item(self, name_item, body: dict, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        url_post_item = urljoin(self.URL, self.POST_STORE_ITEM)
        response = self.client.custom_request("POST", urljoin(url_post_item, str(name_item)),
                                              headers={"Authorization": f"JWT {token}"}, json=body)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    def get_all_items(self, token):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/user_info
        """
        response = self.client.custom_request("GET", urljoin(self.URL, self.GET_ALL_ITEMS),
                                              headers={"Authorization": f"JWT {token}"})
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

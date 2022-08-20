import random

from register_3_step.api import SwaggerStore
from register_3_step.models import FakeUserData
from schemas.registration import valid_schema
from schemas.user_info import valid_user_schema

URL = "https://stores-tests-api.herokuapp.com"


class TestSwaggerStore:
    def test_registration(self):
        body = FakeUserData.random()
        response = SwaggerStore(url=URL).register_user(body=body, schema=valid_schema)
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')

    def test_auth(self):
        body = FakeUserData.random()
        response_reg = SwaggerStore(url=URL).register_user(body=body, schema=valid_schema)
        response_auth = SwaggerStore(url=URL).auth_user(body=body)
        assert response_auth.status == 200
        assert response_auth.response.get('access_token')

    def test_user_info(self):
        body = FakeUserData.random()
        response_reg = SwaggerStore(url=URL).register_user(body=body, schema=valid_schema)
        response_auth = SwaggerStore(url=URL).auth_user(body=body)
        access_token = response_auth.response.get('access_token')
        uuid = response_reg.response.get('uuid')
        body_user_info = FakeUserData.random_user_info()
        self.info = SwaggerStore(url=URL).add_user_info(user_id=uuid, body=body_user_info, headers=access_token,
                                                        schema=valid_user_schema)
        response_user_info = self.info
        assert response_user_info.status == 200

    def test_add_new_store(self):
        random_store = random.randrange(9999999)
        body_reg = FakeUserData.random()
        body_store = FakeUserData.random_product()
        response_reg = SwaggerStore(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = SwaggerStore(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = SwaggerStore(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        assert response_store.status == 201

    def test_get_store(self):
        random_store = random.randrange(9999999)
        body_reg = FakeUserData.random()
        body_store = FakeUserData.random_product()
        response_reg = SwaggerStore(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = SwaggerStore(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = SwaggerStore(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        response_get_store = SwaggerStore(url=URL).get_store(store=random_store, headers=access_token)
        assert response_get_store.status == 200

    def test_post_item(self):
        random_store = random.randrange(9999999)
        random_name_item = FakeUserData.random_item()
        body_reg = FakeUserData.random()
        body_store = FakeUserData.random_product()
        response_reg = SwaggerStore(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = SwaggerStore(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = SwaggerStore(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        uuid = response_store.response.get('uuid')
        body_item = FakeUserData.random_store_item(uuid)
        response_item = SwaggerStore(url=URL).post_item(name_item=random_name_item, body=body_item,
                                                        headers=access_token)
        assert response_item.status == 201

    def test_get_all_items(self):
        random_store = random.randrange(9999999)
        body_reg = FakeUserData.random()
        body_store = FakeUserData.random_product()
        response_reg = SwaggerStore(url=URL).register_user(body=body_reg, schema=valid_schema)
        response_auth = SwaggerStore(url=URL).auth_user(body=body_reg)
        access_token = response_auth.response.get('access_token')
        response_store = SwaggerStore(url=URL).add_new_store(store=random_store, body=body_store, headers=access_token)
        uuid = response_store.response.get('uuid')
        for i in range(3):
            random_name_item = FakeUserData.random_item()
            body_item = FakeUserData.random_store_item(uuid)
            response_item = SwaggerStore(url=URL).post_item(name_item=random_name_item, body=body_item,
                                                            headers=access_token)
        response_get_all_items = SwaggerStore(url=URL).get_all_items(headers=access_token)
        assert response_get_all_items.status == 200

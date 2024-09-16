import random
from register_3_step.api import SwaggerStore
from register_3_step.models import FakeUserData
from schemas.registration import valid_schema
from schemas.user_info import valid_user_schema


class TestSwaggerStore:

    def test_registration(self):
        body = FakeUserData.random()
        response = SwaggerStore().register_user(body=body, schema=valid_schema)
        print("test_registration")
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')

    def test_auth(self):
        body = FakeUserData.random()
        response_reg = SwaggerStore().register_user(body=body, schema=valid_schema)
        response_auth = SwaggerStore().auth_user(body=body)
        print("test_auth")
        assert response_auth.status == 200
        assert response_auth.response.get('access_token')

    def test_add_user_info(self, reg_auth):
        uuid, access_token = reg_auth
        body_user_info = FakeUserData.random_user_info()
        info = SwaggerStore().add_user_info(user_id=uuid, token=access_token, body=body_user_info,
                                            schema=valid_user_schema)
        response_user_info = info
        print("test_add_user_info")
        assert response_user_info.status == 200

    def test_add_new_store(self, reg_auth):
        random_store = random.randrange(9999999)
        body_store = FakeUserData.random_product()
        uuid, access_token = reg_auth
        response_store = SwaggerStore().add_new_store(store=random_store, body=body_store, token=access_token)
        print("test_add_new_store")
        assert response_store.status == 201

    def test_get_store(self, reg_auth):
        random_store = random.randrange(9999999)
        body_store = FakeUserData.random_product()
        uuid, access_token = reg_auth
        response_store = SwaggerStore().add_new_store(store=random_store, body=body_store, token=access_token)
        response_get_store = SwaggerStore().get_store(store=random_store, token=access_token)
        print("test_get_store")
        assert response_get_store.status == 200

    def test_post_item(self, reg_auth):
        random_store = random.randrange(9999999)
        random_name_item = FakeUserData.random_item()
        body_store = FakeUserData.random_product()
        uuid, access_token = reg_auth
        response_store = SwaggerStore().add_new_store(store=random_store, body=body_store, token=access_token)
        uuid_store = response_store.response.get('uuid')
        body_item = FakeUserData.random_store_item(uuid_store)
        response_item = SwaggerStore().post_item(name_item=random_name_item,
                                                 body=body_item, token=access_token)

        print("test_post_item")
        assert response_item.status == 201

    def test_get_all_items(self, reg_auth):
        random_store = random.randrange(9999999)
        body_store = FakeUserData.random_product()
        uuid, access_token = reg_auth
        response_store = SwaggerStore().add_new_store(store=random_store, body=body_store, token=access_token)
        uuid_store = response_store.response.get('uuid')
        for i in range(3):
            random_name_item = FakeUserData.random_item()
            body_item = FakeUserData.random_store_item(uuid_store)
            response_item = SwaggerStore().post_item(name_item=random_name_item,
                                                     body=body_item, token=access_token)
        response_get_all_items = SwaggerStore().get_all_items(token=access_token)
        print("test_get_all_items")
        assert response_get_all_items.status == 200

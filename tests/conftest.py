import pytest
from register_3_step.api import SwaggerStore
from register_3_step.models import FakeUserData
from schemas.registration import valid_schema

URL = "https://stores-tests-api.herokuapp.com"


@pytest.fixture(scope="session")
def reg_auth():
    body = FakeUserData.random()
    response_reg = SwaggerStore().register_user(body=body, schema=valid_schema)
    response_auth = SwaggerStore().auth_user(body=body)
    access_token = response_auth.response.get('access_token')
    uuid = response_reg.response.get('uuid')
    assert response_auth.status == 200
    assert response_auth.response.get('access_token')
    return uuid, access_token

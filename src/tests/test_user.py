import pytest
from src.api.endpoints import Endpoints
from src.schemas.get_user_schema import user_response_schema
from src.validation import response_validator
from src.validation.response.user_response import expected_user


@pytest.mark.contract
def test_should_return_valid_user_contract(api_client, schema_validator):
    response = api_client.get(Endpoints.PATH_USER + "/1")
    schema_validator.validate_response(response, user_response_schema)


@pytest.mark.functional
def test_given_valid_user_id_when_consulting_user_then_should_return_data_user(api_client):
    resp = api_client.get(Endpoints.PATH_USER + "/1")
    response_validator.validate_user_response(resp, expected_user)

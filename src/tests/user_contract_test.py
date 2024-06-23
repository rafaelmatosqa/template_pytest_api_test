import pytest
from src.apis.endpoints import Endpoints
from src.schemas.get_user_schema import user_response_schema


class UserContractTest:
    @pytest.mark.contract
    def test_should_return_valid_user_contract(self, api_client, schema_validator):
        response = api_client.get(Endpoints.PATH_USER, params={"userId": 1})
        schema_validator.validate_response(response, user_response_schema)

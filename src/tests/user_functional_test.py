import pytest

from src.apis.endpoints import Endpoints
from src.validation import response_validator
from src.validation.response.user_response import expected_user


class UserFunctionalTest:
    @pytest.mark.functional
    def test_given_valid_user_id_when_consulting_user_then_should_return_data_user(self, api_client):
        response = api_client.get(Endpoints.PATH_USER, params={"userId": 1})
        response_validator.validate_user_response(response, expected_user)

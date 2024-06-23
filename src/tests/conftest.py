import pytest
import json

from src.apis.client import ApiClient
from src.validation.schema_validator import SchemaValidator


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against"
    )


@pytest.fixture(scope="session")
def env_config(request):
    env = request.getoption("env")
    with open(f'config/{env}.json', 'r') as config_file:
        config = json.load(config_file)
        return config


@pytest.fixture(scope="session")
def api_client(env_config):
    return ApiClient(env_config["base_url"])


@pytest.fixture(scope="session")
def schema_validator():
    return SchemaValidator()

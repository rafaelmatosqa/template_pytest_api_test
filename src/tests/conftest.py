import pytest
import json
import os

from src.api.client import ApiClient
from src.validation.schema_validator import SchemaValidator


@pytest.fixture(scope="session")
def env_config(request):
    env = os.getenv('ENV', 'dev')
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config", f"{env}.json"))
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config


@pytest.fixture(scope="session")
def api_client(env_config):
    return ApiClient(env_config["base_url"])


@pytest.fixture(scope="session")
def schema_validator():
    return SchemaValidator()

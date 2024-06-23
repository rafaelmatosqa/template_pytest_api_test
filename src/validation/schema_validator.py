# validation/schema_validator.py

from jsonschema import validate, ValidationError


class SchemaValidator:
    def validate_response(self, response, schema):
        try:
            validate(instance=response, schema=schema)
        except ValidationError as e:
            raise AssertionError(f"Response schema validation failed: {e}")

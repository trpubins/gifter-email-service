"""Validation module for generating emails."""

# Standard modules
import json
import logging

# 3rd party modules
import jsonschema

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# JSON schema files
EMAIL_SCHEMA_FILE = "email_schema.json"


def validate_payload(payload: dict):
    """Validates the provided payload.
    Throws a ValidationError exception if invalid, otherwise returns.
    
    Parameters
    ----------
    payload: dict
        Dictionary required to contain content to form a single email.
    """
    # load the schema file into python obj
    email_schema = _load_schema(file=EMAIL_SCHEMA_FILE)

    try:
        jsonschema.validate(instance=payload, schema=email_schema)
        logger.info("Email is valid per JSON schema")
    except jsonschema.ValidationError as e:
        logger.error(e)
        raise e
    
    return


def _load_schema(file: str) -> dict:
    """Loads a JSON schema file into a dictionary."""
    try:
        logger.info(f"reading schema file: {file}")
        with open(file) as f:
            schema = json.loads(f.read())
            logger.info(f"schema: {json.dumps(schema)}")
    except Exception as e:
        raise Exception(f"failed to read schema file: {file}. Reason: {e}")
    
    return schema

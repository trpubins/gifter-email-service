# Standard modules
import json
import logging

# Package modules
from validate import validate_payload

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Running: preprocess.app.lambda_handler")
    logger.info(f"event: {event}")
    logger.info(f"context: {context}")

    payload = event['payload']

    # convert from string to dict if req'd
    if isinstance(payload, str):
        payload = json.loads(payload)
        logger.info(f"Converted event['payload'] to type: {type(payload)}")

    # validate the payload
    logger.info("Validating data structure of payload")
    validate_payload(payload)

    return event

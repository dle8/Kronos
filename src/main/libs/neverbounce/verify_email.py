from src.main.config import config
import requests
import json


def validate_email(email):
    try:
        api_response = requests.post(
            config.EMAIL_VERIFICATION_URL.format(config.NEVERBOUNCE_API_KEY, email)
        ).content
        api_response = json.loads(api_response)

        if api_response['result'] == 'invalid':
            raise Exception('Invalid email')
    except Exception:
        raise Exception('Error(s) happened when validating email')

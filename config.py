import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    RUN_SETTING = {
        'host': os.environ.get('SERVER_HOST', 'localhost'),
        'port': int(os.environ.get('SERVER_PORT', 8080)),
        'debug': os.getenv('DEBUG', False),
        "access_log": False,
        "auto_reload": True,
        'workers': int(os.getenv('SERVER_WORKERS', 4))
    }
    # uWSGI를 통해 배포되어야 하므로, production level에선 run setting을 건드리지 않음

    SECRET = os.environ.get('SECRET_KEY', 'example project')
    JWT_PASSWORD = os.getenv('JWT_PASSWORD', 'dev123')
    EXPIRATION_JWT = 2592000  # 1 month
    RESPONSE_TIMEOUT = 900  # seconds

    FALLBACK_ERROR_FORMAT = 'json'

    OAS_UI_DEFAULT = 'swagger'
    SWAGGER_UI_CONFIGURATION = {
        'apisSorter': "alpha",
        'docExpansion': "list",
        'operationsSorter': "alpha"
    }

    API_HOST = os.getenv('API_HOST', '0.0.0.0:8096')
    API_SCHEMES = os.getenv('API_SCHEMES', 'http')
    API_VERSION = os.getenv('API_VERSION', '0.1.0')
    API_TITLE = os.getenv('API_TITLE', 'Centic API')
    API_DESCRIPTION = os.getenv('API_DESCRIPTION', 'Swagger for Centic API')
    API_CONTACT_EMAIL = os.getenv('API_CONTACT_EMAIL', 'example@gmail.com')



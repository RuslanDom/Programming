import os
from dotenv import load_dotenv
from pydantic import SecretStr, BaseConfig, StrictStr

load_dotenv()


class SiteSettings(BaseConfig):
    API_KEY: SecretStr = os.getenv('API_KEY', None)
    HOST_API: StrictStr = os.getenv('HOST', None)



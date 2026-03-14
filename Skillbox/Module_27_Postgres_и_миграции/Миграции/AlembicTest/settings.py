from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}'

    @property
    def DATABASE_URL_psycorg(self):
        return f'postgresql+psycorg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}'

    model_config = SettingsConfigDict(env_file=".env")


config_ = Config()
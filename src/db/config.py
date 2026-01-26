from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = ''
    JWT_SECRET_KEY: str = ''
    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore', env_file_encoding='utf-8'
    )

    @field_validator('DATABASE_URL')
    @classmethod
    def fix_database_url(cls, value: str) -> str:
        if value:
            return value.replace('sslmode=require', 'ssl=require').replace(
                '&channel_binding=require', ''
            )
        return value


settings = Settings()

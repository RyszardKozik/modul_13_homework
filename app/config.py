from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    postgres_username: str
    postgres_password: str
    db_name: str
    mail_username: str
    mail_password: str
    mail_server: str
    mail_port: int
    mail_from: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    mail_starttls: bool
    mail_ssl_tls: bool

    class Config:
        env_file = ".env"
        extra = "allow"

# Load environment variables from the .env file
load_dotenv()

# Initialize the settings object
settings = Settings()

# Print the loaded settings for verification
print("Settings loaded:", settings)

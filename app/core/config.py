"""
Application configuration settings, loaded from environment variables or .env file.
"""

# from pydantic_settings import BaseSettings, SettingsConfigDict
# from pydantic import PostgresDsn, HttpUrl, SecretStr
# from typing import List, Optional

# class Settings(BaseSettings):
#     # --- Core Settings --- #
#     PROJECT_NAME: str = "PMDC Data Exchange"
#     API_V1_STR: str = "/api/v1"
#     DEBUG: bool = False

#     # --- Database Settings --- #
#     # Example: POSTGRES_SERVER=db POSTGRES_USER=pmdc POSTGRES_PASSWORD=changeme POSTGRES_DB=pmdc_dev
#     POSTGRES_SERVER: str
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: SecretStr
#     POSTGRES_DB: str
#     # Assemble the DSN (Data Source Name) for SQLAlchemy
#     DATABASE_URI: Optional[PostgresDsn] = None

#     # @validator("DATABASE_URI", pre=True)
#     # def assemble_db_connection(cls, v: Optional[str], values: dict[str, Any]) -> Any:
#     #     if isinstance(v, str):
#     #         return v
#     #     return PostgresDsn.build(
#     #         scheme="postgresql+psycopg",
#     #         username=values.get("POSTGRES_USER"),
#     #         password=values.get("POSTGRES_PASSWORD").get_secret_value(),
#     #         host=values.get("POSTGRES_SERVER"),
#     #         path=f"{values.get(	\"POSTGRES_DB\") or \"\"}",
#     #     )

#     # --- SaaS Provider Settings --- #
#     SAAS_PROVIDER_NAME: str = "lume" # Example: lume, nexla, matterbeam
#     SAAS_API_BASE_URL: HttpUrl
#     SAAS_API_KEY: SecretStr
#     SAAS_API_TIMEOUT: int = 30 # Timeout in seconds

#     # --- Authentication Settings (OAuth2 / OIDC) --- #
#     # These will depend heavily on the chosen IdP (Auth0, Okta, Azure AD B2C)
#     AUTH_TOKEN_URL: HttpUrl # Token endpoint of the IdP
#     AUTH_JWKS_URL: HttpUrl # URL to fetch the JSON Web Key Set for token verification
#     AUTH_AUDIENCE: str # The API identifier (audience) expected in the JWT
#     AUTH_ISSUER: HttpUrl # The issuer expected in the JWT
#     AUTH_ALGORITHMS: List[str] = ["RS256"] # Algorithm used to sign the JWT

#     # Optional: Define required scopes for different actions
#     # SCOPE_PUBLISHER_WRITE: str = "write:data"
#     # SCOPE_SUBSCRIBER_READ: str = "read:data"
#     # SCOPE_ADMIN: str = "manage:system"

#     # --- Celery Settings (for background tasks) --- #
#     CELERY_BROKER_URL: str = "redis://redis:6379/0" # Example using Redis
#     CELERY_RESULT_BACKEND: str = "redis://redis:6379/0"

#     # --- CORS Settings --- #
#     # List of allowed origins for frontend interactions
#     # BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"] # Example for local dev

#     # --- Environment Loading --- #
#     model_config = SettingsConfigDict(
#         env_file=".env", 
#         env_file_encoding=	\"utf-8\", 
#         case_sensitive=True
#     )

# # Instantiate settings to be imported elsewhere
# settings = Settings() 
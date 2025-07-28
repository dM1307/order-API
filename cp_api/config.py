# src/cp_api/config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # … other settings …

    OAUTH2_CLIENT_ID = os.getenv("OAUTH2_CLIENT_ID")
    OAUTH2_CLIENT_SECRET = os.getenv("OAUTH2_CLIENT_SECRET")
    KEYCLOAK_HOST = "http://localhost:8081"
    KEYCLOAK_REALM = "chronos-realm"
    OAUTH2_AUTH_URL = f"{KEYCLOAK_HOST}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth"
    OAUTH2_TOKEN_URL = f"{KEYCLOAK_HOST}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
    OAUTH2_REDIRECT_URI = "http://localhost:5000/v1/docs/oauth2-redirect.html"

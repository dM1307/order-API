from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt
from cp_lib.services.jobs_service import JobService
from cp_lib.repositories.jobs_repository import JobRepository

# OAuth2 scheme for authorization
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=".../auth",
    tokenUrl=".../token",
)


# Function to decode and verify the JWT token
def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, "YOUR_PUBLIC_KEY", algorithms=["RS256"])
        return payload
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_jwt_token(token)


# Dependency to get the job service
def get_job_service() -> JobService:
    return JobService(repository=JobRepository())

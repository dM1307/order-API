import os


class Config:
    SECRET_KEY = os.getenv("API_SECRET", "change-me")

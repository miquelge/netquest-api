import os

class Config:
    DATABASE_CONNECTION_STRING = os.environ.get(
        "DATABASE_CONNECTION_STRING", "postgresql+psycopg2://user:password@postgres:5432/records"
    )


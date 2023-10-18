from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config


Engine = create_engine(Config.DATABASE_CONNECTION_STRING)
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

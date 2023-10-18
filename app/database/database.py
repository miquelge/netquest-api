from pydantic import AnyUrl
from pydantic_core import Url
from app.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psycopg2.extensions import register_adapter, AsIs
from pydantic.networks import IPv4Address, IPv6Address
import logging

Engine = create_engine(Config.DATABASE_CONNECTION_STRING)
Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

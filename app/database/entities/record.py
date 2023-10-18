
from pydantic import AnyUrl
from app.database.baseClass import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils.types.url import URLType
from sqlalchemy.ext.declarative import declarative_base
import uuid
import logging as log

class Record(Base):
    id = Column(UUID, primary_key=True)
    title = Column(String)
    img = Column(String)
    __allow_unmapped__ = True

    def __init__(self, title, img, id = None):
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.title = title
        self.img = str(img)

    def patch(self, attributes):
        for key, value in attributes.items():
            if type(value) == AnyUrl:
                value = str(value)
            setattr(self, key, value)

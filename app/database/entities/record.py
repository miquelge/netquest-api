import uuid

from pydantic import AnyUrl
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.database.baseClass import Base


class Record(Base):
    id = Column(UUID, primary_key=True)
    title = Column(String)
    img = Column(String)
    __allow_unmapped__ = True

    def __init__(self, title, img, id=None):
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

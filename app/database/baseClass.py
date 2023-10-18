from typing import Any
from uuid import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from sqlalchemy import UUID, Column


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

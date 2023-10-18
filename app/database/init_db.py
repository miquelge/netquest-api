from app.database.base_class import Base
from app.database.database import Engine


def init_db() -> None:
    Base.metadata.create_all(bind=Engine)

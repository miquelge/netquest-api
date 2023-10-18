from app.database.baseClass import Base
from app.database.database import Engine


def init_db() -> None:
    Base.metadata.create_all(bind=Engine)

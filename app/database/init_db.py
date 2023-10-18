from app.database.baseClass import Base
from app.database.database import Engine
from app.database.entities.record import Record


def init_db() -> None:
    Base.metadata.create_all(bind=Engine)

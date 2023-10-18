from uuid import UUID
import app.models.record as Models
from sqlalchemy.orm import Session
from app.database.database import Session
from app.database.entities.record import Record
import logging as log
from sqlalchemy.orm import sessionmaker, mapper

from app.utils.exceptions.internalErrorException import InternalErrorException
from app.utils.exceptions.notFoundException import NotFoundException

class RecordsService():
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self):
        try:
            records = self.db.query(Record).all()
            return Models.GetAllRecordsResultModel.model_validate({"items": records})
        except Exception as e:
            raise InternalErrorException("Exception while listing all elements", e)

    def create(self, record: Models.RecordCreateModel) -> Models.RecordModel:
        try:
            newRecord = Record(**record.model_dump())
            self.db.add(newRecord)
        except Exception as e:
            self.db.rollback()
            raise InternalErrorException("Exception while creating the element", e)
        else:
            self.db.commit()
            return Models.RecordModel.model_validate(newRecord)
    
    def get_by_id(self, id: UUID):
        try:
            record = self.db.get(Record, id)
            if record is None:
                raise NotFoundException()
            return Models.RecordModel.model_validate(record)
        except NotFoundException as e:
            raise e
        except Exception as e:
            raise InternalErrorException("Exception while getting element by id", e)

    def delete_by_id(self, id: UUID) -> Models.DeletionResponseModel:
        try:
            record = self.db.get(Record, id)
            if record is None:
                raise NotFoundException()
            self.db.delete(record)
        except NotFoundException as e:
            raise e
        except Exception as e:
            self.db.rollback()
            raise InternalErrorException("Exception while deleting element by id", e)
        else:
            self.db.commit()
            return Models.DeletionResponseModel(deleted=True)
    
    def update_by_id(self, id: UUID, record: Models.RecordPatchModel) -> Models.RecordModel:
        try:
            recordDB = self.db.get(Record, id)
            if recordDB is None:
                raise NotFoundException()
            recordDB.patch(record.model_dump(exclude_unset=True))
            self.db.add(recordDB)
        except NotFoundException as e:
            raise e
        except Exception as e:
            self.db.rollback()
            raise InternalErrorException("Exception while updating element by id", e)
        else:
            self.db.commit()
            return Models.RecordModel.model_validate(recordDB)

recordsService = RecordsService(Session())

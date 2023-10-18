from uuid import UUID

from sqlalchemy.orm import Session

import app.models.record as Models
from app.database.database import SessionMaker
from app.database.entities.record import Record
from app.utils.exceptions.internal_error_exception import \
    InternalErrorException
from app.utils.exceptions.not_found_exception import NotFoundException


class RecordsService():
    def __init__(self, db: Session):
        self.db = db

    def create(self, record: Models.RecordCreateModel) -> Models.RecordModel:
        try:
            newRecord = Record(**record.model_dump())
            self.db.add(newRecord)
        except Exception as e:
            self.db.rollback()
            raise InternalErrorException(
                "Exception while creating the element", e
            )
        else:
            self.db.commit()
            return Models.RecordModel.model_validate(newRecord)

    def get_all(self):
        try:
            records = self.db.query(Record).all()
            return Models.GetAllRecordsResultModel.model_validate(
                {"items": records}
            )
        except Exception as e:
            raise InternalErrorException(
                "Exception while listing all elements", e
            )

    def get_by_id(self, id: UUID):
        try:
            record = self.db.query(Record).get(id)
            if record is None:
                raise NotFoundException()
            return Models.RecordModel.model_validate(record)
        except NotFoundException as e:
            raise e
        except Exception as e:
            raise InternalErrorException(
                "Exception while getting element by id", e
            )

    def delete_by_id(self, id: UUID) -> Models.DeletionResponseModel:
        try:
            record = self.db.query(Record).get(id)
            if record is None:
                raise NotFoundException()
            self.db.query(Record).filter(Record.id == id).delete()
        except NotFoundException as e:
            raise e
        except Exception as e:
            self.db.rollback()
            raise InternalErrorException(
                "Exception while deleting element by id", e
            )
        else:
            self.db.commit()
            return Models.DeletionResponseModel(deleted=True)

    def update_by_id(
        self, id: UUID, record: Models.RecordPatchModel
    ) -> Models.RecordModel:
        try:
            recordDB = self.db.query(Record).get(id)
            if recordDB is None:
                raise NotFoundException()
            recordDB.patch(record.model_dump(exclude_unset=True))
        except NotFoundException as e:
            raise e
        except Exception as e:
            self.db.rollback()
            raise InternalErrorException(
                "Exception while updating element by id", e
            )
        else:
            self.db.commit()
            return Models.RecordModel.model_validate(recordDB)


recordsService = RecordsService(SessionMaker())


from typing import Optional
from uuid import UUID

from pydantic import BaseModel, AnyUrl


class RecordCreateModel(BaseModel):
    title: str
    img: AnyUrl

    class Config:
        from_attributes = True

class RecordPatchModel(BaseModel):
    title: Optional[str] = None
    img: Optional[AnyUrl] = None

class RecordModel(BaseModel):
    id: UUID
    title: Optional[str] = None
    img: Optional[AnyUrl] = None
    
    class Config:
        from_attributes = True

class GetAllRecordsResultModel(BaseModel):
    items: list[RecordModel]

class DeletionResponseModel(BaseModel):
    deleted: bool

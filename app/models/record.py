from typing import Optional
from uuid import UUID

from pydantic import AnyUrl, BaseModel, ConfigDict


class RecordCreateModel(BaseModel):
    title: str
    img: AnyUrl


class RecordPatchModel(BaseModel):
    title: Optional[str] = None
    img: Optional[AnyUrl] = None


class RecordModel(BaseModel):
    id: UUID
    title: Optional[str] = None
    img: Optional[AnyUrl] = None

    model_config = ConfigDict(from_attributes=True)


class GetAllRecordsResultModel(BaseModel):
    items: list[RecordModel]


class DeletionResponseModel(BaseModel):
    deleted: bool

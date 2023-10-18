from uuid import UUID

from fastapi import APIRouter

import app.models.record as Models
from app.services.records.recordsService import recordsService


recordsRouter = APIRouter(prefix='/records')


@recordsRouter.get("")
async def get_all_records():
    return recordsService.get_all()


@recordsRouter.post("")
async def create_record(record: Models.RecordCreateModel):
    return recordsService.create(record)


@recordsRouter.get("/{id}")
async def get_record_by_id(id: UUID):
    return recordsService.get_by_id(id)


@recordsRouter.patch("/{id}")
async def update_record_by_id(id: UUID, record: Models.RecordPatchModel):
    return recordsService.update_by_id(id, record)


@recordsRouter.delete("/{id}")
async def delete_record_by_id(id: UUID):
    return recordsService.delete_by_id(id)

import pytest
from fastapi.testclient import TestClient
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from app.models.record import RecordCreateModel, RecordModel, RecordPatchModel
from app.routers.records import recordsRouter
from app.services.records import RecordsService

client = TestClient(recordsRouter)


@pytest.fixture
def service():
    db = UnifiedAlchemyMagicMock()
    return RecordsService(db)


def test_create_record(service):
    record = RecordCreateModel(title="title", img="https://test.com")
    create = service.create(record)
    assert create
    assert create.id


def test_get_all_records(service):
    record = RecordCreateModel(title="title", img="https://test.com")
    createResponse = service.create(record)
    result = service.get_all()
    assert result
    assert type(result.items) == list
    assert len(result.items) == 1
    assert result.items[0].id == createResponse.id


def test_get_record_by_id(service):
    record = RecordCreateModel(title="title", img="https://test.com")
    createResponse = service.create(record)
    result = service.get_by_id(createResponse.id)
    assert result
    assert type(result) == RecordModel
    assert result.id == createResponse.id


def test_delete_by_id(service):
    record = RecordCreateModel(title="title", img="https://test.com")
    createResponse = service.create(record)
    getAllResponse = service.get_all()
    assert getAllResponse
    assert type(getAllResponse.items) == list
    assert len(getAllResponse.items) == 1
    _ = service.delete_by_id(createResponse.id)
    getAllReponse2 = service.get_all()
    assert getAllReponse2
    assert type(getAllReponse2.items) == list
    assert len(getAllReponse2.items) == 0


def test_update_by_id(service):
    record = RecordCreateModel(title="title", img="https://test.com")
    createResponse = service.create(record)
    patchModel = RecordPatchModel(title="This is a new title")
    updateResult = service.update_by_id(createResponse.id, patchModel)
    assert updateResult
    assert updateResult.title
    assert updateResult.title == "This is a new title"

    getresult = service.get_by_id(createResponse.id)
    assert getresult
    assert getresult.title
    assert getresult.title == "This is a new title"


from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer

from app.database.init_db import init_db
from app.middleware.middleware import Middleware
from app.routers.records import recordsRouter


# Handle DB
init_db()

# Initialize api
app = FastAPI()
app.add_middleware(Middleware)
app.include_router(recordsRouter, dependencies=[Depends(HTTPBearer())])

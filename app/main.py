
from fastapi import FastAPI

from app.database.init_db import init_db
from app.middleware.middleware import Middleware
from app.routers.records import recordsRouter


init_db()

# Populate db
# populate_db()

# security = OAuth2PasswordBearer()
# app = FastAPI(dependencies=[Depends(security)])

# Initialize api
app = FastAPI()
app.add_middleware(Middleware)
app.include_router(recordsRouter)

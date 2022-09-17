from urllib.request import Request
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from router import document_get, document_post
from db import models
from db.database import engine
#from router.exceptions import StoryException
from fastapi import HTTPException, status
from starlette.responses import PlainTextResponse

app = FastAPI()
app.include_router(document_get.router)

models.Base.metadata.create_all(engine)
from urllib.request import Request
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from router import document_get, document_post
from db import models
from db.database import engine
from router.exceptions import TitleException
# from fastapi import HTTPException, status
# from starlette.responses import PlainTextResponse

app = FastAPI()
app.include_router(document_get.router)
app.include_router(document_post.router)

@app.exception_handler(TitleException)
def story_exception_handler(request: Request, exc: TitleException):
    return JSONResponse(
        status_code = 418,
        content = {'detail': exc.name}
    )

models.Base.metadata.create_all(engine)
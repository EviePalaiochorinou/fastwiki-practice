from sqlalchemy.sql.sqltypes import DateTime
from pydantic import BaseModel
from db.models import DBDocument

class DocumentBase(BaseModel):
    title: str
    content: str

class DocumentCreate(BaseModel):
    content: str

class DocumentDisplay(BaseModel):
    title: str
    content: str
    class Config():
        orm_mode = True
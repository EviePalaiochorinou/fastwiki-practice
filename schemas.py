from sqlalchemy.sql.sqltypes import DateTime
from pydantic import BaseModel
from typing import List
from db.models import DBDocument

class DocumentBase(BaseModel):
    title: str
    content: str

class DocumentCreate(BaseModel):
    content: str

class DocumentDisplay(BaseModel):
    title: str
    content: str
    #last_edited: DBDocument.timestamp
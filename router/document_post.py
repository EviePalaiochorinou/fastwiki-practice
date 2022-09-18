from typing import Optional, List
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from db import db_document
from fastapi import Depends
from db.database import get_db
from sqlalchemy.orm import Session
from schemas import DocumentDisplay, DocumentCreate
 
router = APIRouter(
    prefix = '/documents',
    tags = ['documents']
)

@router.post('/{title}', response_model=DocumentDisplay)
def create_new_document_revision(title: str, request: DocumentCreate,  db: Session = Depends(get_db)):
    db_document.create_new_document_revision(
        db, title, request
    )
    # return {
    #     'title': title,
    #     'content': content,
    #     'data': document
    # }
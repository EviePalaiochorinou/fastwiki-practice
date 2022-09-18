from fastapi import APIRouter, APIRouter, Depends
from typing import Optional
from sqlalchemy.orm.session import Session
from db import db_document
from db.database import get_db

router = APIRouter(
    prefix='/documents',
    tags=["documents"]
)

@router.get(
    '/',
    summary = "Retrieve all documents",
    description= "This api call is fetching all documents",
    response_description= "The list of available documents"
    )
def get_all_documents(db: Session = Depends(get_db)):
    return db_document.get_all_documents(db)
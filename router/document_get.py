from fastapi import APIRouter, APIRouter, Depends
from typing import Optional
from sqlalchemy.orm.session import Session
from db import db_document
from db.database import get_db
from fastapi import HTTPException, status

router = APIRouter(
    prefix='/documents',
    tags=["documents"]
)

@router.get(
    '/',
    summary = "Retrieve all documents.",
    description= "This api call is fetching all documents.",
    response_description= "The list of available documents."
    )
def get_all_documents(db: Session = Depends(get_db)):
    return db_document.get_all_documents(db)

@router.get(
    ('/{title}'),
    summary = "Retrieve a list of available revisions for a document.",
    description = "This api call is retrieving all available revisions for a document.",
    response_description = "The list of available revisions for a documents."
)
def get_a_documents_revisions(title: str, db: Session = Depends(get_db)):
    revisions = db_document.get_document(db, title)
    if not revisions:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Document with title '{title}' not found")
    return revisions
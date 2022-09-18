from db.models import DBDocument
# from router.exceptions import StoryException
from schemas import DocumentBase
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

def get_document(db: Session, title: str):
    document = db.query(DBDocument).filter(DBDocument.title == title).first()
    if not document:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'Document with title {title} not found')
    return document

def get_all_documents(db: Session):
    return db.query(DBDocument).all()
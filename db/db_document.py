from db.models import DBDocument
# from router.exceptions import StoryException
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from schemas import DocumentBase, DocumentCreate
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

def get_document(db: Session, title: str) -> DocumentBase:
    document = db.query(DBDocument).filter(DBDocument.title == title).first()
    if not document:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'Document with title {title} not found')
    return document

def get_all_documents(db: Session):
    return db.query(DBDocument).all()

def create_new_document_revision(db: Session, title: str, request: DocumentCreate):
    new_revision = DBDocument(
        title = title,
        content = request.content,
    )
    db.add(new_revision)
    db.commit()
    db.refresh(new_revision)
    return new_revision
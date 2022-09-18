from fastapi import APIRouter, status, Response, APIRouter, Depends
from enum import Enum
from typing import Optional
from db import db_document

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
def get_all_documents():
    return db_document.get_all_documents
from fastapi import APIRouter, status, Response, APIRouter, Depends
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/documents',
    tags=["documents"]
)

@router.get(
    '/all',
    summary = "Retrieve all documents",
    description= "This api call is fetching all documents",
    response_description= "The list of available documents"
    )
def get_all_documents():
    return {"message": f"All available documents."}
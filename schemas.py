from pydantic import BaseModel
from typing import List

class DocumentBase(BaseModel):
    title: str
    content: str
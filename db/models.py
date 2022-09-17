from sqlite3 import Timestamp
from xmlrpc.client import Boolean
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
#from sqlalchemy.sql.schema import ForeignKey
#from sqlalchemy.orm import relationship

class DBDocument(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    timestamp = Column(Timestamp)
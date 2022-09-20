from fastapi.testclient import TestClient
from db.database import get_db,Base
from db.db_document import create_new_document_revision
from db.models import DBDocument
from main import app
from schemas import DocumentCreate
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_get_all_documents():
    response = client.get('/documents/')
    assert response.status_code == 200

def test_get_a_documents_revisions():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    doc = DocumentCreate(content = 'this is my test content')
    revision = create_new_document_revision(session, 'hello', doc)

    response = client.get('/documents/hello')
    assert response.status_code == 200
    assert response.json()[0]['title'] == revision.title
    assert response.json()[0]['content'] == revision.content

def test_create_new_document_revision():
    response = client.post('/documents/hello',
        json = {
            'content': 'test content'
        }
    )
    assert response.status_code == 200

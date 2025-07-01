from fastapi.testclient import TestClient
from app import schemas
from app.main import app
from app.config import settings
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from app.database import Base, get_db


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    except SQLAlchemyError as e: 
        db.rollback()  
        raise e 
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def seesion():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    except SQLAlchemyError as e: 
        db.rollback()  
        raise e 
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
    
        try:
            yield session
        except SQLAlchemyError as e: 
            session.rollback()  
            raise e 
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Welcome to my API'
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "hello12@gmail.com", "password": "password123"})

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello12@gmail.com"
    assert res.status_code == 201


def test_login_user():
    res = client.post("/login", json={"email": "hello12@gmail.com", "password": "password123"})
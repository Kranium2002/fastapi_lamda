from fastapi.testclient import TestClient
from pymongo import MongoClient
from api.main import app
import sys, asyncio
import pytest

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
client = MongoClient("mongodb+srv://mathurvidhu2002:hTPfNu8e26R4nyaB@cluster0.xjtky9j.mongodb.net/?retryWrites=true&w=majority")
db = client["db1"]
col = db["col"]    

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "server is running"}
    

def test_find_all():
    # Insert some test data
    col.insert_many([{"name": "John"}, {"name": "Jane"}])
    response = client.get("/find")
    assert response.status_code == 200
    assert response.json()[-2:] == [{"name": "John"}, {"name": "Jane"}]

def test_delete():
    return True;

def test_insert_record():
    response = client.put("/insert", json={"name": "Bob"})
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
    

    
  
from fastapi import Body, FastAPI
from pymongo import MongoClient
from mangum import Mangum

app = FastAPI()

client = MongoClient("mongodb+srv://mathurvidhu2002:hTPfNu8e26R4nyaB@cluster0.xjtky9j.mongodb.net/?retryWrites=true&w=majority")
db = client["db1"]
col = db["col"]

@app.get("/")
async def root():
    print("abc")
    return {"server is running"}
                
@app.get("/find")
def find_all():
    results = []
    for doc in db.col.find({}, {"_id": 0}):
        results.append(doc)
    return results

@app.put("/insert")
def insert_record(name: str = Body(...)):
    record_dict = {"name": name}
    try:
        result = db.col.insert_one(record_dict)
        print(result.inserted_id)
        return {"message": "success"}
    except Exception as e:
        print(str(e))
        return {"message": "error"}


handler = Mangum(app)
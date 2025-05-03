from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Hello_J(BaseModel):
    name : str
    format : str

@app.get("/helloj")
@app.get("/helloj/{name}/{format}")
async def helloj_get(name:str="rahul",format:str="json"):
    return {"name":name,"format":format}
    
    
@app.post("/helloj")
async def helloj_post(item : Hello_J):
    return {"name":item.name ,"format":item.format}

from fastapi import FastAPI

from pydantic import BaseModel
app=FastAPI()


class mul(BaseModel):
    num1:int
    
@app.get("/api/test")
def welcome():
    return "hii"

@app.post("/mul")
def multiples(data:mul):
    result = [data.num1 * i for i in range(1, 11)]
    return {"multiples":result}

items={'a': 'Apple','b':'Banana','c':'Cherry'}

class Item(BaseModel):
    user:str
    password:str

@app.get('/api/items')
def get_items():
    return items
#add new item
@app.post('/api/add')
def add_items(item:Item):
    return 'The username is {item.user} and password is {item.password}'



   
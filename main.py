from fastapi import FastAPI

from pydantic import EmailStr, BaseModel
import uvicorn



app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }
    
#параметр запроса  
@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}  

#параметр тела запроса
@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }
    
#несколько параметров в 1 функции
@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }
    
@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]    
    
@app.get("/items/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}    
    
#параметр пути
@app.get("/items/{item_id}/")    
#item_id получаем из адресной строки
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id" : item_id,
            },
    }
 

    
#запуск приложения    
if __name__ == '__main__': 
    uvicorn.run("main:app", reload=True)   
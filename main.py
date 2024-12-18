from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from core.models import Base, db_helper
from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as router_v1
from core.config import settings



@asynccontextmanager
async def lifespan(app: FastAPI):
    #Создание базы данных 
    #таблицы создаются через асинхронный движок
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield
    


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1,prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)



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

    
#несколько параметров в 1 функции
@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }
    
    
#запуск приложения    
if __name__ == '__main__': 
    uvicorn.run("main:app", reload=True)   
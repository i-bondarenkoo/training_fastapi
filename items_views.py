from typing import Annotated

from  fastapi import Path

from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]    
    

@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}    
    

#параметр пути
@router.get("/{item_id}/")    
#item_id получаем из адресной строки
#Annotated для параметра пути, чтобы поставить ограничение
#больше 1 и меньше миллиона
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {
        "item": {
            "id" : item_id,
            },
    }
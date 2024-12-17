from pydantic_settings import BaseSettings
from pathlib import Path

#Абсолютный путь до проекта
BASE_DIR = Path(__file__).parent.parent


#настройки для БД
class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    #db_echo: bool = True
    db_echo: bool = False
    
#Инициализация, создадим экземпляр класса
settings = Setting()   


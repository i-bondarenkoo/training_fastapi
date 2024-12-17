from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session
from core.config import settings
from asyncio import current_task
from sqlalchemy.ext.asyncio import AsyncSession


#подключение к БД
# создаем подключение и фабрику сессий
# на основе фабрики сессий, создается async_scoped_session
# далее ее используем чтобы создавать сессию подключения во время запроса
class DatabaseHelper():
    
    def __init__(self, url: str, echo: str):
        self.engine = create_async_engine(
            url=url,
            echo=echo, 
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            #Подготовка к commit
            autoflush=False,
            #Автоматическое сохранение
            autocommit=False,
            #Автоматическое удаление информации об объектах из сессии
            expire_on_commit=False,
        )
    #отдельный помошник для создания сессии
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session
    #метод который создает сессию для каждого запроса
    async def session_dependency(self) ->  AsyncSession:
        async with self.session_factory() as session:
            yield session    
            await session.close()
        
    async def scoped_session_dependency(self) ->  AsyncSession:
        session = self.get_scoped_session()
        
        yield session    
        await session.close()    
        
        
#создание экземпляра
db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
    
)
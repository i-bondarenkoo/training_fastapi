from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


#Основа над чем мы будем дальше работать
#базовый класс
class Base(DeclarativeBase):
    
    #св-во которое говорит что такой таблицы не будет в базе данных
    __abstract__ = True
    
    #declared_attr свойство которое на уровне класса 
    #выполняется как property
    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    
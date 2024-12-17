
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from core.models import Product
from sqlalchemy import select

from .schemas import ProductCreate, ProductUpdate, ProductUpdatePartial

#чтение товаров
async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    #execute - выполнить выражение
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


#чтение по одному
async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


#создание товара 
async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


#обновление put patch
#put обновляет целиком
#patch обновляет только некоторые свойства
async def update_product(
    session: AsyncSession,
    product: Product, 
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
    ) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()    
    return product


#удаление
async def delete_product(
    session: AsyncSession,
    product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
    
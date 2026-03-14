from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import relationship, selectinload, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, \
    Identity, Float, select, update

from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()
Base = declarative_base()

engine = create_async_engine('postgresql+asyncpg://postgres:postgres@localhost')
async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    title = Column(String(100), default=False)
    count = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref="products")

    def __repr__(self):
        return '<Product %r>' % self.title

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    num = Column(Integer, Identity(minvalue=100, maxvalue=150, cycle=True))


    def __repr__(self):
        return '<User %r>' % self.name

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    User(name='Richard', surname='Gir'),
                    User(name='Adam', surname='Won'),
                    User(name='Ben', surname='Stiller'),
                    Product(title='Car', user_id=2),
                    Product(title='House', user_id=3),
                    Product(title='Helicopter', user_id=1),
                ]
            )

            await session.commit()


@app.delete('/products/<int:product_id>', status_code=202)
async def delete_product(product_id: int):
    async with async_session() as session:
        async with session.begin():
            product = await session.execute(select(Product).where(Product.id == product_id))
            product = product.scalar_one()
            await session.delete(product)
            await session.commit()


@app.post('/products', status_code=201)
async def add_product():
    async with async_session() as session:
        async with session.begin():
            p = Product(title='Airplane')
            session.add(p)
            await session.flush()

@app.put('/products/<int:product_id>', status_code=204)
async def update_product(product_id: int):
    async with async_session() as session:
        async with session.begin():
            q = update(Product).where(Product.id == product_id).\
                values(title='Update data').\
                execution_options(synchronize_session='fetch').\
                returning(Product)
            result = await session.execute(q)
            return result.scalar_one()







@app.get('/products', status_code=200)
async def get_products():
    async with async_session() as session:
        async with session.begin():
            # without user
            # q = await session.execute(select(Product))

            # with User
            q = await session.execute(
                select(Product).options(selectinload(Product.user))
            )
            products = q.scalars().all()
            return products
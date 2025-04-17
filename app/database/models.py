from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Annotated
from sqlalchemy import BigInteger, String, ForeignKey, JSON
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

price_str = Annotated[str, mapped_column(String(6))]
id = Annotated[int, mapped_column(primary_key=True)]

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[id]
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25))
    bag: Mapped['Bag'] = relationship(
        'Bag', 
        back_populates='user', 
        uselist=False, 
        lazy='joined'
    )


class Bag(Base):
    __tablename__ = 'bags'

    id: Mapped[id]
    ticker: Mapped[list[str]] = mapped_column(JSON)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(
        'User', 
        back_populates='bag', 
        uselist=False
    )
    


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)






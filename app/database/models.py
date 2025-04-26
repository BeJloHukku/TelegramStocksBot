from sqlalchemy import BigInteger, String, ForeignKey, JSON
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from typing import Annotated


id = Annotated[int, mapped_column(primary_key=True)]


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
    ticker: Mapped[list[str] | None] = mapped_column(MutableList.as_mutable(JSON), default=list)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    user: Mapped['User'] = relationship(
        'User', 
        back_populates='bag', 
        uselist=False,
    )
    









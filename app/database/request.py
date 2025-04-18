from .base import connection
from sqlalchemy.exc import SQLAlchemyError
from .models import User, Bag
from sqlalchemy import select, update



@connection
async def set_user(session, user_id, name):
    try:
        user = await session.scalar(select(User).where(User.tg_id == user_id))

        if not user:
            new_user = User(tg_id=user_id, name=name)
            new_user.bag = Bag(ticker=[])
            session.add(new_user)
            await session.commit()
            return None
        else:
            return user
    except SQLAlchemyError as e:
        await session.rollback()


@connection
async def add_stock(session, user_id, ticker):
    try:
        user = await session.scalar(select(User).where(User.tg_id == user_id))

        if not user:
            return None
        else:
            if ticker not in user.bag.ticker:
                user.bag.ticker.append(ticker)
                session.commit()
                return True
        return False
    except SQLAlchemyError as e:
        await session.rollback()


@connection
async def open_bag(session, user_id):
    try:
        user = await session.scalar(select(User).where(User.tg_id == user_id))

        if not user:
            return None
        else:
            return user.bag.ticker
    except SQLAlchemyError as e:
        await session.rollback()


from app.database.models import async_session
from app.database.models import User, Bag, Stock
from sqlalchemy import select, update, delete
import utils.stocks as st


async def set_user(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, name=name))
            await session.commit()


# async def add_stock(ticker):
#     stock_inf = st.get_information(ticker)
#     async with async_session() as session:
#         stock = await session.scalar(select(Bag).where(Bag.user_id == User.id and Bag.ticker == ticker))
#         if not stock:

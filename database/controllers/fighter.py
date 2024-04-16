from sqlalchemy import select, update
from sqlalchemy.exc import DBAPIError

from database.connection import get_db_sessionmaker
from database.models import FighterModel

from exceptions import DatabaseError

from utils.fighter import FighterType


class FighterController:
    def __init__(self):
        self.db_sessionmaker = get_db_sessionmaker()

    async def select_fighter_by_name(self, name: str) -> FighterModel:
        try:
            async with self.db_sessionmaker.begin() as session:
                return await session.scalar(
                    select(FighterModel).where(FighterModel.name == name)
                )
        except DBAPIError as e:
            raise DatabaseError() from e

    async def register_fighter(self, fighter: FighterType):
        is_exists = await self.select_fighter_by_name(fighter.name)

        if is_exists:
            return

        try:
            async with self.db_sessionmaker.begin() as session:
                session.add(
                    FighterModel(
                        name=fighter.name,
                        age=fighter.age,
                        fight_art=fighter.fight_art,
                    )
                )
                await session.commit()
        except DBAPIError as e:
            await session.rollback()
            raise DatabaseError() from e

    async def update_fights(self, *args: FighterType):
        for fighter in args:
            try:
                async with self.db_sessionmaker.begin() as session:
                    await session.execute(
                        update(FighterModel)
                        .where(FighterModel.name == fighter.name)
                        .values(fights=FighterModel.fights + 1)
                    )
            except DBAPIError as e:
                await session.rollback()
                raise DatabaseError() from e

    async def update_wins(self, fighter: FighterType):
        try:
            async with self.db_sessionmaker.begin() as session:
                await session.execute(
                    update(FighterModel)
                    .where(FighterModel.name == fighter.name)
                    .values(wins=FighterModel.wins + 1)
                )
        except DBAPIError as e:
            await session.rollback()
            raise DatabaseError() from e

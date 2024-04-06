from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    __table_args__ = {"schema": "fight_club"}

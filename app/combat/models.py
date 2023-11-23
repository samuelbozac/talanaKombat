import enum
from os import listdir
from json import loads

from sqlalchemy import (
    event,
    Column,
    String,
    Integer,
    Enum
)

from app.database import Base
from app.conf import settings


class PlayerEnum(enum.Enum):
    player1 = "player1"

    player2 = "player2"


class Movement(Base):
    __tablename__ = "movements"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    movement = Column(
        String(7),
        nullable=False
    )

    energy = Column(Integer, nullable=False)

    name = Column(String, nullable=False)

    player = Column(
        Enum(PlayerEnum),
        nullable=False,
        index=True,
    )


def load_fixtures():
    fixtures_path = f"{settings.BASE_PATH}/fixtures"

    return [f"{fixtures_path}/{x}" for x in listdir(fixtures_path)]


def insert_data(target, connection, **kw):
    """
    Function to insert intial player's initial movements.
    """
    fixtures = load_fixtures()
    for file in fixtures:
        fixture = loads(open(file, "r").read())
        for item in fixture:
            connection.execute(
                target.insert(),
                item
            )


event.listen(Movement.__table__, "after_create", insert_data)

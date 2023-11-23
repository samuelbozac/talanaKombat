from pydantic import BaseModel


class Player(BaseModel):
    movimientos: list[str]

    golpes: list[str]


class Combat(BaseModel):
    player1: Player

    player2: Player

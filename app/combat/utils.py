import re

from sqlalchemy.orm import Session

from app.combat.models import PlayerEnum, Movement
from app.combat.schemas import Combat


class Player():
    def __init__(self, forward: str, back: str, player: PlayerEnum) -> None:
        self.energy = 6
        self.forward = forward
        self.back = back
        self.player = player
        self.history = []
        self.valid_moves = ["A", "W", "S", "D"]
        self.name = "Tonyn" if player == PlayerEnum.player1 else "Arnold"

    def movements(self, session: Session):
        return session.query(Movement).filter(
            Movement.player == self.player.value
        ).all()

    def winner(self):
        self.history.append(
            f"{self.name} ha ganado, aun con {self.energy} de energía"
        )

    def move(self):
        self.history.append(
            f"{self.name} se ha movido"
        )

    def use_movement(self, movement: Movement, player, prev_move=""):
        if len(movement.movement) > 1:
            self.history.append(
                f"{self.name} ha lanzado un {movement.name}"
            )
        else:
            if prev_move == self.forward:
                prev_move = "ha avanzado y "
            elif prev_move == self.back:
                prev_move = "ha retrocedido y "
            elif prev_move in self.valid_moves:
                prev_move = "se ha movido y "

            self.history.append(
                    f"{self.name} {prev_move}ha lanzado un {movement.name}"
            )
        player.energy -= movement.energy
        print(f"{player.name} le queda {player.energy} de energía")
        if player.energy < 1:
            return False
        return True


def make_movements(moves: list[str], attacks: list[str]):
    return [f"{moves[x]} + {attacks[x]}" for x in range(len(moves))]


def validate_move(
        combination, player: Player, regex, session: Session, other_player
        ):
    movement = re.search(regex, combination)
    player_movements = player.movements(session)
    if movement:
        if movement.group() in [x.movement for x in player_movements]:
            print("Combo used")
            movement_for_use = [
                x for x in player_movements if x.movement == movement.group()
            ][0]
            move_used = player.use_movement(
                movement_for_use,
                other_player
                )
            return move_used

        elif not movement.group(2):
            print("Just move")
            player.move()
            return True

        elif not movement.group(1):
            print("Just attack")
            movement_for_use = [
                x for x in player_movements if x.movement == movement.group(2)
            ][0]
            move_used = player.use_movement(
                movement_for_use,
                other_player
            )
            return move_used

        if (len(movement.group(1)) >= 1) and (len(movement.group(2)) == 1):
            print("Move and attack")
            movement_for_use = [
                x for x in player_movements if x.movement == movement.group(2)
            ][0]
            move_used = player.use_movement(
                movement_for_use,
                other_player,
                prev_move=movement.group(1)[-1]
            )
            return move_used
    return True


def intercalate_messages(messages1: list[str], messages2: list[str]) -> list[str]:  # noqa: E501
    intercalated_messages = []
    zip_messages = zip(messages1, messages2,)
    for x, y in zip_messages:
        intercalated_messages.append(x)
        intercalated_messages.append(y)

    if len(messages1) < len(messages2):
        intercalated_messages.extend(
            messages2[len(messages1):]
        )
    elif len(messages1) > len(messages2):
        intercalated_messages.extend(
            messages1[len(messages2):]
        )
    return intercalated_messages


def make_combat_messages(combat: Combat, session: Session):
    regex1 = r'(DSD|SD|[WASD]){0,1} \+ (K|P){0,1}$'
    regex2 = r'(ASA|SA|[WASD]){0,1} \+ (K|P){0,1}$'
    movements1 = make_movements(
        combat.player1.movimientos,
        combat.player1.golpes
    )
    movements2 = make_movements(
        combat.player2.movimientos,
        combat.player2.golpes
    )
    combat_movements = zip(movements1, movements2)
    player1 = Player("D", "A", PlayerEnum.player1)
    player2 = Player("A", "D", PlayerEnum.player2)

    for combination1, combination2 in combat_movements:
        print(f"Player 1 does: {combination1}")
        move_used1 = validate_move(
            combination1, player1, regex1, session, player2
        )
        if not move_used1:
            player1.winner()
            break
        print(f"Player 2 does: {combination2}")
        move_used2 = validate_move(
            combination2, player2, regex2, session, player1
        )
        if not move_used2:
            player2.winner()
            break

    return player1.history, player2.history

def make_movements(moves: list[str], attacks: list[str]):
    return [f"{moves[x]} + {attacks[x]}" for x in range(len(moves))]


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

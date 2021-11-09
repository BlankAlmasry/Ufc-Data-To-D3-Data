import typing

from elote.competitors.base import BaseCompetitor

from helpers import write_to_csv, assign_players_to_dict


def rating_algorithm(fighters, fights, rating, algorithm: typing.Type[BaseCompetitor]):
    players = {}
    for match in fights:
        player1, player2, result1, result2, *meta = match
        assign_players_to_dict(player1, player2, players, algorithm)
        p1 = players[player1]
        p2 = players[player2]
        if result1 == "Win" or result2 == "Lose":
            p1.beat(p2)
        elif result1 == "Lose" or result2 == "Win":
            p2.beat(p1)
        elif result1 == "Draw" or result2 == "Draw":
            p1.tied(p2)
        else:
            continue
        if player1 in fighters:
            write_to_csv(player1, p1.rating, rating)
        if player2 in fighters:
            write_to_csv(player2, p2.rating, rating)

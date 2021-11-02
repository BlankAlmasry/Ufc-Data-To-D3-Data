import csv
import operator
import typing

import pandas
from elote.competitors.base import BaseCompetitor


def assign_players_to_dict(player1, player2, players, cls):
    for player in [player1, player2]:
        if not player in players:
            players[player] = cls()


def write_to_csv(player1, player2, p1, p2, rating, *meta):
    rating.writerow([meta[0][:4] + "-01-01", player1, p1.rating])
    rating.writerow([meta[0][:4] + "-01-01", player2, p2.rating])


def compile_matches(cls: typing.Type[BaseCompetitor]):
    players = {}
    with open('fights.csv', 'r', encoding='UTF8', newline='') as fights:
        with open('ratings.csv', 'w', encoding='UTF8', newline='') as ratings:
            fights = csv.reader(fights)
            # sort by date
            sorted_fights = sorted(fights, key=operator.itemgetter(4), reverse=False)
            rating = csv.writer(ratings)
            # header
            rating.writerow(["date", "name", "value"])
            for match in sorted_fights:
                player1, player2, result1, result2, *meta = match
                assign_players_to_dict(player1, player2, players, cls)
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
                write_to_csv(player1, player2, p1, p2, rating, *meta)

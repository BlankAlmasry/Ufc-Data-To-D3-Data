import csv
import json
import operator
import os
import typing
from elote.competitors.base import BaseCompetitor

from algorithms.glicko2.glicko2 import Rating, Glicko2


def top_15_fighters():
    return ["Khabib-Nurmagomedov", "Kamaru-Usman", "Demetrious-Johnson", "Amanda-Nunes", "Jon-Jones", "Henry-Cejudo",
            "Jose-Aldo", "Daniel-Cormier", "Stipe-Miocic", "Conor-McGregor", "Georges-St-Pierre", "Anderson-Silva",
            "Israel-Adesanya", "Alexander-Volkanovski", "Francis-Ngannou"]


def assign_players_to_dict(player1, player2, players, cls):
    for player in [player1, player2]:
        if player not in players:
            players[player] = cls()


def write_to_csv(player, rating, file):
    file.writerow([player, rating])


def generate_d3_format(ratings_file, fighters):
    r = csv.reader(ratings_file)
    next(r)  # skip header
    d = {}
    for fighter in fighters:
        d[fighter] = ["1500"]
    for row in r:
        d[row[0]].append(row[1])
    for f in d.keys():
        if len(d[f]) < 24:
            d[f].extend([d[f][len(d[f]) - 1]] * (25 - len(d[f])))
    j = open('data.js', 'w')
    j.write("const dataOri = [")
    # headers
    json.dump(["fights", *[n for n in range(0, 25)]], j)
    j.write(',\n')
    for k, v in d.items():
        json.dump([k, *v], j)
        if list(d.keys())[-1] != k:
            j.write(',\n')
        else:
            j.write('\n')

    j.write("]")


def compile_matches(csv_file):
    players = {}
    fighters = top_15_fighters()

    with open(csv_file, 'r', encoding='UTF8', newline='') as fights:
        fights = csv.reader(fights)
        # sort by date
        sorted_fights = sorted(fights, key=operator.itemgetter(4), reverse=False)
        init(fighters, players, sorted_fights)


def init(fighters, players, fights):
    glicko_2_facade(fighters, players, fights)


def glicko_2_facade(fighters, players, fights):
    with open('ratings_glicko_2.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        glicko_2(fighters, players, rating, fights)
    with open('ratings_glicko_2.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters)
    os.remove("ratings_glicko_2.csv")


# TODO
# glicko_1(fighters, players, rating, sorted_fights)
# ECF(fighters, players, rating, sorted_fights)
# ELO(fighters, players, rating, sorted_fights)
# DWZ(fighters, players, rating, sorted_fights)
# TrueSkill(fighters, players, rating, sorted_fights)


def glicko_2(fighters, players, rating, sorted_fights):
    g = Glicko2()
    for match in sorted_fights:
        player1, player2, result1, result2, *meta = match
        assign_players_to_dict(player1, player2, players, Rating)
        p1 = players[player1]
        p2 = players[player2]
        if result1 == "Win" or result2 == "Lose":
            p1, p2 = g.rate_1vs1(p1, p2)
            players[player1] = p1
            players[player2] = p2
        elif result1 == "Lose" or result2 == "Win":
            p2, p1 = g.rate_1vs1(p2, p1)
            players[player1] = p1
            players[player2] = p2
        elif result1 == "Draw" or result2 == "Draw":
            p1, p2 = g.rate_1vs1(p1, p2, drawn=True)
            players[player1] = p1
            players[player2] = p2
        else:
            continue
        if player1 in fighters:
            write_to_csv(player1, p1.mu, rating)
        if player2 in fighters:
            write_to_csv(player2, p2.mu, rating)

import csv
import json
import operator
import os
import typing
from elote.competitors.base import BaseCompetitor

from algorithms.glicko2.glicko2 import Rating, Glicko2
from algorithms.glicko2.glicko2facade import glicko_2_facade


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




# TODO
# glicko_1(fighters, players, rating, sorted_fights)
# ECF(fighters, players, rating, sorted_fights)
# ELO(fighters, players, rating, sorted_fights)
# DWZ(fighters, players, rating, sorted_fights)
# TrueSkill(fighters, players, rating, sorted_fights)



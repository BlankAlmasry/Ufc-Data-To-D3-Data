import csv
import os

from elote import EloCompetitor

import matches
from algorithms.rating_algorithm import rating_algorithm


def elo_facade(fighters, fights):
    with open('ratings_elo.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, EloCompetitor)
    with open('ratings_elo.csv', 'r', encoding='UTF8', newline='') as ratings:
        matches.generate_d3_format(ratings, fighters, 1000, "elo")
    os.remove("ratings_elo.csv")

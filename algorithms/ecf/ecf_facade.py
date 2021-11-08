import csv
import os

from elote import ECFCompetitor

import matches
from algorithms.rating_algorithm import rating_algorithm


def ecf_facade(fighters, fights):
    with open('ratings_ecf.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, ECFCompetitor)
    with open('ratings_ecf.csv', 'r', encoding='UTF8', newline='') as ratings:
        matches.generate_d3_format(ratings, fighters, 40, "ecf")
    os.remove("ratings_ecf.csv")

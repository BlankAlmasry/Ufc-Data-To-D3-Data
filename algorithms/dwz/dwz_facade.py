import csv
import os

from elote import DWZCompetitor

from algorithms.rating_algorithm import rating_algorithm
from helper import generate_d3_format


def dwz_facade(fighters, fights):
    with open('ratings_dwz.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, DWZCompetitor)
    with open('ratings_dwz.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters, 400, "dwz")
    os.remove("ratings_dwz.csv")

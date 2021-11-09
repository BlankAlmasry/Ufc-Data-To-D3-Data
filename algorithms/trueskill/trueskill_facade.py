import csv
import os

from algorithms.rating_algorithm import rating_algorithm
from algorithms.trueskill.trueskill_adapter import TrueskillAdapter
from helpers import generate_d3_format


def trueskill_facade(fighters, fights):
    with open('ratings_trueskill.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, TrueskillAdapter)
    with open('ratings_trueskill.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters, 25, "trueskill")
    os.remove("ratings_trueskill.csv")


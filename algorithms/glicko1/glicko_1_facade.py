import csv
import os

from elote import GlickoCompetitor

from algorithms.rating_algorithm import rating_algorithm
from helper import generate_d3_format


def glicko_1_facade(fighters, fights):
    with open('ratings_glicko_1.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, GlickoCompetitor)
    with open('ratings_glicko_1.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters, 1500, "glicko1")
    os.remove("ratings_glicko_1.csv")

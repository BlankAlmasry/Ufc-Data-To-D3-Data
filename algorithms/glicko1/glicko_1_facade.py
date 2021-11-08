import csv
import os

import matches
from algorithms.glicko1.glicko_1 import glicko_1


def glicko_1_facade(fighters, fights):
    with open('ratings_glicko_1.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        glicko_1(fighters, fights, rating)
    with open('ratings_glicko_1.csv', 'r', encoding='UTF8', newline='') as ratings:
        matches.generate_d3_format(ratings, fighters, 1500, "glicko1")
    os.remove("ratings_glicko_1.csv")

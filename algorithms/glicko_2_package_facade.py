import csv
import os

import matches
from algorithms.glicko_2_adapter import glicko_2_adapter


def glicko_2_facade(fighters, fights):
    with open('ratings_glicko_2.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        glicko_2_adapter(fighters, rating, fights)
    with open('ratings_glicko_2.csv', 'r', encoding='UTF8', newline='') as ratings:
        matches.generate_d3_format(ratings, fighters, 1500, "glicko2")
    os.remove("ratings_glicko_2.csv")


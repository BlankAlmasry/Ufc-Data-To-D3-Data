import csv
import os

from algorithms.glicko2.glicko_2_adapter import Glicko2Adapter
from algorithms.rating_algorithm import rating_algorithm
from helper import generate_d3_format


def glicko_2_facade(fighters, fights):
    with open('ratings_glicko_2.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, Glicko2Adapter)
    with open('ratings_glicko_2.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters, 1500, "glicko2")
    os.remove("ratings_glicko_2.csv")

import csv
import os

from algorithms.fire.fire import Fire
from algorithms.rating_algorithm import rating_algorithm
from helpers import generate_d3_format


def fire_facade(fighters, fights):
    with open('ratings_fire.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, Fire)
    with open('ratings_fire.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters, 10, "fire")
    os.remove("ratings_fire.csv")

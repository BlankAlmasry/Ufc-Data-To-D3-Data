import csv
import os

from algorithms.openskills.BradleyTerryModel_Adapter import BradleyTerryModelAdapter
from algorithms.rating_algorithm import rating_algorithm
from helper import generate_d3_format


def BradleyTerryModel_facade(fighters, fights):
    with open('ratings_openskill.csv', 'w+', encoding='UTF8', newline='') as ratings:
        rating = csv.writer(ratings)
        rating.writerow(["fighter", "value"])
        rating_algorithm(fighters, fights, rating, BradleyTerryModelAdapter)
    with open('ratings_openskill.csv', 'r', encoding='UTF8', newline='') as ratings:
        generate_d3_format(ratings, fighters, 25, "openskill")
    os.remove("ratings_openskill.csv")


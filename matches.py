import csv
import operator

from algorithms.dwz.dwz_facade import dwz_facade
from algorithms.ecf.ecf_facade import ecf_facade
from algorithms.elo.elo_facade import elo_facade
from algorithms.glicko1.glicko_1_facade import glicko_1_facade
from algorithms.glicko2.glicko_2_package_facade import glicko_2_facade
from algorithms.trueskill.trueskill_facade import trueskill_facade
from helper import top_15_fighters


def compile_matches(csv_file):
    top_fighters = top_15_fighters()
    with open(csv_file, 'r', encoding='UTF8', newline='') as fights:
        fights = csv.reader(fights)
        # sort by date
        sorted_fights = sorted(fights, key=operator.itemgetter(4), reverse=False)
        # compute matches with several algorithms
        init(top_fighters, sorted_fights)


def init(fighters, fights):
    glicko_2_facade(fighters, fights)
    glicko_1_facade(fighters, fights)
    ecf_facade(fighters, fights)
    dwz_facade(fighters, fights)
    elo_facade(fighters, fights)
    trueskill_facade(fighters, fights)

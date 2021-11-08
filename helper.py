import csv
import json


def top_15_fighters():
    return ["Khabib-Nurmagomedov", "Kamaru-Usman", "Demetrious-Johnson", "Amanda-Nunes", "Jon-Jones", "Henry-Cejudo",
            "Jose-Aldo", "Daniel-Cormier", "Stipe-Miocic", "Conor-McGregor", "Georges-St-Pierre", "Anderson-Silva",
            "Israel-Adesanya", "Alexander-Volkanovski", "Francis-Ngannou"]


def assign_players_to_dict(player1, player2, players, cls):
    for player in [player1, player2]:
        if player not in players:
            players[player] = cls()


def write_to_csv(player, rating, file):
    file.writerow([player, rating])


def generate_d3_format(ratings_file, fighters, initialized_rating, class_name):
    r = csv.reader(ratings_file)
    next(r)  # skip header
    d = {}
    for fighter in fighters:
        d[fighter] = []
        d[fighter].append(str(initialized_rating))
    for row in r:
        d[row[0]].append(row[1])
    for f in d.keys():
        if len(d[f]) < 24:
            d[f].extend([d[f][len(d[f]) - 1]] * (25 - len(d[f])))
    j = open("data/" + class_name + '_data.js', 'w')
    j.write("const dataOri = [")
    # headers
    json.dump(["fights", *[n for n in range(0, 25)]], j)
    j.write(',\n')
    for k, v in d.items():
        json.dump([k, *v], j)
        if list(d.keys())[-1] != k:
            j.write(',\n')
        else:
            j.write('\n')

    j.write("]")
    j.close()

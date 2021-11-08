import matches
from algorithms.glicko2_package.glicko2 import Rating, Glicko2


def glicko_2_adapter(fighters, rating, sorted_fights):
    players = {}
    g = Glicko2()
    for match in sorted_fights:
        player1, player2, result1, result2, *meta = match
        matches.assign_players_to_dict(player1, player2, players, Rating)
        p1 = players[player1]
        p2 = players[player2]
        if result1 == "Win" or result2 == "Lose":
            p1, p2 = g.rate_1vs1(p1, p2)
            players[player1] = p1
            players[player2] = p2
        elif result1 == "Lose" or result2 == "Win":
            p2, p1 = g.rate_1vs1(p2, p1)
            players[player1] = p1
            players[player2] = p2
        elif result1 == "Draw" or result2 == "Draw":
            p1, p2 = g.rate_1vs1(p1, p2, drawn=True)
            players[player1] = p1
            players[player2] = p2
        else:
            continue
        if player1 in fighters:
            matches.write_to_csv(player1, p1.mu, rating)
        if player2 in fighters:
            matches.write_to_csv(player2, p2.mu, rating)

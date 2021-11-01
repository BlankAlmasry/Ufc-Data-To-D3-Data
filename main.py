from elote import LambdaArena, GlickoCompetitor, ECFCompetitor, DWZCompetitor, EloCompetitor
import json
from matches import compile_matches

matches = [
    ("lol", "Blank", "Lose", "Win", "2019-1-1"),
    ("lol", "Blank", "Lose", "Win", "2019-1-1"),
    ("lol", "Blank", "Lose", "Win", "2019-1-1"),
    ("lol", "Blank", "Lose", "Win", "2019-1-1"),
    ("lol", "Blank", "Win", "Lose", "2019-1-1"),
    ("lol", "Blank", "Win", "Lose", "2019-1-1")
]

compile_matches(matches, GlickoCompetitor)

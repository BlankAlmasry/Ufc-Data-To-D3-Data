from elote import LambdaArena, GlickoCompetitor, ECFCompetitor, DWZCompetitor, EloCompetitor
import json

from algorithms.glicko2 import Rating, Glicko2

from matches import compile_matches
compile_matches(EloCompetitor)


from elote.competitors.base import BaseCompetitor
from trueskill import rate_1vs1, Rating, quality_1vs1


class TrueskillAdapter(BaseCompetitor):
    def __init__(self):
        self._rating = Rating()

    @property
    def rating(self):
        return self._rating.mu

    def beat(self, competitor):
        p1, p2 = rate_1vs1(self._rating, competitor._rating)
        self._rating = p1
        competitor._rating = p2

    def lost_to(self, competitor):
        p1, p2 = rate_1vs1(competitor._rating, self._rating)
        self._rating = p1
        competitor._rating = p2

    def tied(self, competitor):
        p1, p2 = rate_1vs1(self._rating, competitor._rating, drawn=True)
        self._rating = p1
        competitor._rating = p2

    def export_state(self):
        return {
            "initial_rating": self._rating.mu,
            "initial_rd": self._rating.sigma,
        }

    def expected_score(self, competitor):
        return quality_1vs1(self._rating, competitor._rating)

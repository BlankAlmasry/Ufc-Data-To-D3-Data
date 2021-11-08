from elote.competitors.base import BaseCompetitor

from algorithms.glicko2_package.glicko2 import Rating, Glicko2


class Glicko2Adapter(BaseCompetitor):
    def __init__(self):
        self._rating = Rating()

    @property
    def rating(self):
        return self._rating.mu

    def expected_score(self, competitor):
        g = Glicko2()
        quality = g.quality_1vs1(self._rating, competitor._rating)
        return quality

    def beat(self, competitor):
        g = Glicko2()
        p1, p2 = g.rate_1vs1(self._rating, competitor._rating)
        self._rating = p1
        competitor._rating = p2

    def lost_to(self, competitor):
        g = Glicko2()
        p1, p2 = g.rate_1vs1(competitor._rating, self._rating)
        self._rating = p1
        competitor._rating = p2

    def tied(self, competitor):
        g = Glicko2()
        p1, p2 = g.rate_1vs1(self._rating, competitor._rating, drawn=True)
        self._rating = p1
        competitor._rating = p2

    def export_state(self):
        return {
            "initial_rating": self._rating.mu,
            "initial_rd": self._rating.phi,
            "initial_vol": self._rating.sigma
        }

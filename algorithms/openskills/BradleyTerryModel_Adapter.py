from elote.competitors.base import BaseCompetitor
from openskill import Rating, rate
from openskill.models import BradleyTerryFull


class BradleyTerryModelAdapter(BaseCompetitor):
    def __init__(self):
        self._rating = Rating()

    @property
    def rating(self):
        return self._rating.mu

    def expected_score(self, competitor):
        pass

    def beat(self, competitor):
        p = rate([[self._rating], [competitor._rating]], model=BradleyTerryFull)
        p1, p2 = p[0], p[1]
        self._rating = Rating(*p1[0])
        competitor._rating = Rating(*p2[0])

    def lost_to(self, competitor):
        p = rate([[competitor._rating], [self._rating]], model=BradleyTerryFull)
        p1, p2 = p[1], p[0]
        self._rating = Rating(*p1[0])
        competitor._rating = Rating(*p2[0])

    def tied(self, competitor):
        p = rate([[self._rating], [competitor._rating]], model=BradleyTerryFull, score=[1, 1])
        p1, p2 = p[0], p[1]
        self._rating = Rating(*p1[0])
        competitor._rating = Rating(*p2[0])

    def export_state(self):
        pass

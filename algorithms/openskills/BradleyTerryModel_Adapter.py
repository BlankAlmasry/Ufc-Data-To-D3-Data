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
        p1, p2 = rate([[self._rating], [competitor._rating]], model=BradleyTerryFull)
        self._rating = Rating(*p1)
        competitor._rating = Rating(*p2)

    def lost_to(self, competitor):
        p1, p2 = rate([[competitor._rating], [self._rating]], model=BradleyTerryFull)
        self._rating = Rating(*p2)
        competitor._rating = Rating(*p1)

    def tied(self, competitor):
        p1, p2 = rate([[competitor._rating], [self._rating]], model=BradleyTerryFull, score=[1, 1])
        self._rating = Rating(*p2)
        competitor._rating = Rating(*p1)

    def export_state(self):
        pass

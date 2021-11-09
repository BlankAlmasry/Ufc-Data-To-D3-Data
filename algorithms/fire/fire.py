from elote.competitors.base import BaseCompetitor


class Fire(BaseCompetitor):
    def __init__(self, name):
        self.fire_count = 10

    @property
    def rating(self):
        return self.fire_count

    def expected_score(self, competitor):
        pass

    def beat(self, competitor):
        self.fire_count += competitor.fire_count
        competitor.fire_count = 0

    def lost_to(self, competitor):
        competitor.fire_count += self.fire_count
        self.fire_count = 0

    def tied(self, competitor):
        total = self.fire_count - competitor.fire_count
        if total > 0:
            self.fire_count -= total/2
            competitor.fire_count += total/2
        else:
            self.fire_count += total/2
            competitor.fire_count -= total/2

    def export_state(self):
        pass

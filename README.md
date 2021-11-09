# Ufc-Data-To-D3-Data

Just a script to convert the data from the Ufc-Scrapper repository to a format that is easier to work with my
Rating-Algorithms-Visualizer.

Kinda special, because it's a script. wasn't designed to be reused

## Usage

Must have csv file in format of
`name1, name2, result1, result2, date(yyyy-mm-dd))`

`py -m pip install -r requirements.txt`

`py main.py path-to-csv-file`

data will be generated in data folder

I left fights.csv file which is a real example based on all UFC fights

### Supported Algorithms:

- [Glicko-2](https://en.wikipedia.org/wiki/Glicko-2_rating_algorithm)
- [Glicko-1](https://en.wikipedia.org/wiki/Glicko-1_rating_algorithm)
- [Elo](https://en.wikipedia.org/wiki/Elo_rating_system)
- [TrueSkill](https://en.wikipedia.org/wiki/TrueSkill)
- [Dwz](https://en.wikipedia.org/wiki/Dwz_rating_system)
- [ECF](https://en.wikipedia.org/wiki/ECF_grading_system)
- [OpenSkill(BradleyTerryFull-model)](https://en.wikipedia.org/wiki/Open-skill_rating_system)
- Fire🔥

### about Fire🔥 Model
You are legally unallowed to read this if you are mathematician, or every wanted to be one

Players start with 10 Points

On every win, they get All Opponent Points, and Opponent lose half of his

On a loss, they lose half of his points

On a draw, half of the differential points between him and his opponent get added to both of their points
(ex Rating(30), Rating(20) -> Rating(25), Rating(25))

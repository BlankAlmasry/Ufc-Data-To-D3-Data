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

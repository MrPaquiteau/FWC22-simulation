<h1 align="center"> ⚽️ Random FIFA World Cup 2022 Simulation </h1>

## Project Overview

This Python project simulates a completely randomized football (soccer) World Cup tournament. The simulation follows a comprehensive process from team selection to crowning a champion, introducing elements of chance and randomness at each stage.

## Project Structure

```
📦FWC22-simulation
 ┣ 📂group_stage
 ┃ ┣ 📂groups
 ┃ ┣ 📂results
 ┃ ┗ 📂tables
 ┣ 📂knockout_stage
 ┃ ┣ 📂final
 ┃ ┣ 📂quarter_finals
 ┃ ┣ 📂round_of_16
 ┃ ┣ 📂semi_finals
 ┃ ┗ 📊qualified.csv
 ┣ 📂src
 ┃ ┣ 🐍__init__.py
 ┃ ┣ 🐍q1_create_groups.py
 ┃ ┣ 🐍q2_generate_groups_results.py
 ┃ ┣ 🐍q3_create_group_tables.py
 ┃ ┣ 🐍q4_generate_knockout_teams.py
 ┃ ┗ 🐍q5_simulate_knockout_stage.py
 ┣ 📊FWC22_teams.csv
 ┣ 📜Instructions_FR.pdf
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┗ 🐍q6_main.py
```

The simulation is implemented across multiple Python scripts, each handling a specific phase of the World Cup:

1. **Group Stage Team Assignment**
   - Randomly distributes teams into 8 groups of 4 teams
   - Generates group composition files

2. **Match Simulation**
   - Simulates matches within each group
   - Generates random scores for each match
   - Implements a simple scoring system

3. **Group Table Calculation**
   - Calculates points for each team based on match results
   - Generates group standings
   - Determines top two teams from each group

4. **Knockout Stage Team Selection**
   - Selects 16 teams (top two from each group) for the knockout rounds
   - Prepares teams for elimination matches

5. **Knockout Stage Simulation**
   - Simulates matches from Round of 16 to Final
   - Uses probabilistic methods to determine winners
   - Generates results for each round


## Key Features

- Completely randomized match and tournament outcomes
- Modular Python script design
- CSV-based data handling
- Flexible group and knockout stage simulations

## Simulation Logic

- Group Stage: Random score generation (0-3 goals)
- Points System: 
  - Win: 3 points
  - Draw: 1 point
  - Loss: 0 points
- Knockout Stages: Winner determined by coin-flip probability

## Potential Improvements

The project includes an open-ended question about making match simulations more realistic. Potential enhancements could include:
- Incorporating team rankings
- Adding more complex scoring probabilities
- Considering team historical performance

## Requirements

- Python 3.x
- Standard library modules: `random`, `os`

## How to Run

1. Ensure you have a `FWC22_teams.csv` file with participating teams
2. Run scripts with `q6_main.py` or in sequence: 
   - `q1_generate_groups.py`
   - `q2_generate_groups_results.py`
   - `q3_create_group_tables.py`
   - `q4_generate_knockout_teams.py`
   - `q5_simulate_knockout_stage.py`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Romain TROILLARD

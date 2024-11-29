import random
import os


ROUND_NAMES = ["round_of_16", "quarter_finals", "semi_finals", "final"]

def ensure_directory_exists(directory):
    """Creates the directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_qualified():
    """
    Reads the file and returns a dictionary with groups as keys
    and teams as values (list of tuples with the team's name and its position).
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    qualified_file_path = os.path.join(base_dir, "..", "knockout_stage", "qualified.csv")
    
    groups = {}
    with open(qualified_file_path, 'r') as file:
        for line in file:
            country, group, position = line.strip().split(',')
            groups.setdefault(group, []).append((country, position))
    return groups

def create_round_of_16(groups):
    """
    Creates the matches for the round of 16 by pairing
    the first of a group with the second of the next group.
    """
    matches = []
    groups_list = list(groups.items())
    for i, (_, teams) in enumerate(groups_list):
        next_group = groups_list[(i + 1) % len(groups_list)][1]
        home = next((x for x in teams if x[1] == '1'), None)
        away = next((x for x in next_group if x[1] == '2'), None)  
        if home and away:
            matches.append([home[0], away[0]])
    return matches

def create_other_rounds(teams):
    """
    Creates the matches for subsequent rounds based on the list of qualified teams.
    """
    return [[teams[i], teams[i + 1]] for i in range(0, len(teams), 2)]

def simulate_match(home, away, p):
    """
    Simulates a match between two teams and returns the scores.
    """
    if random.random() < p:
        home_score = random.randint(1, 3)
        away_score = random.randint(0, home_score - 1)
    else:
        away_score = random.randint(1, 3)
        home_score = random.randint(0, away_score - 1)
    print(f'{home} {home_score} - {away_score} {away}')
    return home, home_score, away_score, away

def simulate_round(matches, p):
    """
    Simulates all matches in a round and returns the results.
    """
    return [simulate_match(match[0], match[1], p) for match in matches]

def identify_winners(results):
    """
    Identifies the winners of each match from the results.
    """
    return [home if home_score > away_score else away for home, home_score, away_score, away in results]

def save_to_file(directory, filename, data):
    """
    Saves data to a file without adding a blank line at the end.
    """
    ensure_directory_exists(directory)
    with open(os.path.join(directory, filename), 'w') as file:
        for i, item in enumerate(data):
            if isinstance(item, (list, tuple)):
                file.write(", ".join(map(str, item)))
            else:
                file.write(str(item))
            if i < len(data) - 1:
                file.write("\n")

def simulate_tournament(groups):
    """
    Simulates the entire tournament through the round of 16, quarter-finals, semi-finals, and final.
    """
    winners = None
    previous_winners = []
    probabilities = [0.7, 0.5, 0.5, 0.5]
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    knockout_stage_dir = os.path.join(base_dir, "..", "knockout_stage")

    for i, round_name in enumerate(ROUND_NAMES):
        print(round_name.replace("_", " ").title())
        directory = os.path.join(knockout_stage_dir, round_name)
        ensure_directory_exists(directory)
        
        if i == 0:
            matches = create_round_of_16(groups)
        else:
            matches = create_other_rounds(previous_winners)
        
        save_to_file(directory, "matches.csv", matches)
        results = simulate_round(matches, probabilities[i])
        save_to_file(directory, "results.csv", results)
        winners = identify_winners(results)
        if round_name != "final":
            save_to_file(directory, "winners.csv", winners)
        previous_winners = winners
        
        print()

    print(f"Winner: {winners[0]}")
    save_to_file(directory, "winner.csv", [winners[0]])

def main_q5():
    try:
        groups = load_qualified()
        simulate_tournament(groups)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    os.chdir("..")
    main_q5()
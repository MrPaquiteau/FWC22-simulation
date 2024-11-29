import random
import os


def read_teams_from_csv(filename):
    """
    Reads teams from a CSV file and organizes them by pot.
    
    :param filename: Name of the CSV file containing the teams (format: team,pot)
    :return: Dictionary with pots as keys and lists of teams as values
    """
    
    teams = {}
    
    try:
        with open(filename, "r", encoding="utf-8") as teams_list_file:
            for line_num, line in enumerate(teams_list_file, start=1):
                line = line.strip()
                if not line or ',' not in line:  # Skip empty lines and lines without a comma
                    print(f"Line {line_num} ignored: '{line}' (expected format: team,pot)")
                    continue
                team, pot = line.split(",", 1)  # Split line at the first comma
                teams.setdefault(pot, []).append(team)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    
    return dict(sorted(teams.items()))  # Sort dictionary by keys

def create_group(teams, group_id, directory="group_stage/groups"):
    """
    Creates a group by randomly selecting a team from each pot.
    
    :param teams: Dictionary of pots with lists of teams
    :param group_id: Group identifier (used for the filename)
    """
    
    if not teams:  # Check if teams is empty
        print("No group to create: team list is empty.")
        return
    
    filename = f"{directory}/group_{chr(65+group_id)}.csv"
    try:
        with open(filename, "w", encoding="utf-8") as group_file:
            for pot, pot_teams in teams.items():
                if pot_teams:
                    selected_team = random.choice(pot_teams)
                    pot_teams.remove(selected_team)
                    group_file.write(f"{selected_team}\n")
                else:
                    print(f"No team available in pot {pot} for group {group_id}.")
    except Exception as e:
        print(f"Error creating group {group_id}: {e}")

def main_q1():
    filename = "FWC22_teams.csv"
    teams = read_teams_from_csv(filename)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_dir, "..", "group_stage", "groups")

    if not os.path.exists(directory):
        os.makedirs(directory)

    group_id = 0
    while any(teams.values()):
        create_group(teams, group_id)
        group_id += 1


if __name__ == "__main__":
    main_q1()
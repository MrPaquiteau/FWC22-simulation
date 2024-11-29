import random
import os


def create_results(group_id):
    """
    Generates match results for a given group and writes them to a file.
    This function reads a list of teams from a file named 'group_<letter>.csv', 
    where <letter> corresponds to the group_id (0 for 'A', 1 for 'B', etc.). 
    It then simulates match results between each pair of teams, generating random 
    scores for each match. The results are written to a file named 'result_group_<letter>.csv'.
    Args:
        group_id (int): The ID of the group (0 for 'A', 1 for 'B', etc.).
    Raises:
        FileNotFoundError: If the group file does not exist.
    Returns:
        None
    """
    
    try:
        with open(f"group_stage/groups/group_{chr(65+group_id)}.csv", "r", encoding="utf-8") as group_file:
            teams = [line.strip() for line in group_file]
    except FileNotFoundError:
        print(f"Error: The file 'group_{chr(65+group_id)}.csv' was not found.")
        return

    results = []
    for i in range(len(teams)-1):
        for j in range(i+1, len(teams)):
            home_team = teams[i]
            away_team = teams[j]
            home_score = random.randint(0, 3)
            away_score = random.randint(0, 3)
            results.append(f"{home_team},{home_score},{away_score},{away_team}\n")

    with open(f"group_stage/results/result_group_{chr(65+group_id)}.csv", "w", encoding="utf-8") as result_file:
        result_file.writelines(results)

def main_q2():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_dir, "..", "group_stage", "results")    
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(8):
        create_results(i)

if __name__ == "__main__":
    main_q2()
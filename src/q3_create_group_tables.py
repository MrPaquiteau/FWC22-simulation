import os


def add_points(match):
    """
    Calculate and assign points for home and away teams based on the match result.
    Parameters:
    match (tuple): A tuple containing the home team name, home team score, away team score, and away team name.
    Returns:
    dict: A dictionary with team names as keys and their respective statistics (goals for, goals against, goal difference, and points) as values.
    """

    home_team, home_score, away_score, away_team = match
    home = {"GF": int(home_score), "GA": int(away_score)}
    away = {"GF": int(away_score), "GA": int(home_score)}
    
    # Calculate goal differences
    home["GD"] = home["GF"] - home["GA"]
    away["GD"] = away["GF"] - away["GA"]
    
    # Assign points
    if home["GF"] > away["GF"]:
        home["Points"], away["Points"] = 3, 0
    elif home["GF"] < away["GF"]:
        away["Points"], home["Points"] = 3, 0
    else:
        home["Points"], away["Points"] = 1, 1
    
    return {home_team: home, away_team: away}

def update_table(table, match_result):
    """
    Updates the league table with the results of a match.
    Parameters:
    table (dict): The current league table where keys are team names and values are dictionaries containing team statistics.
    match_result (dict): A dictionary containing the match results where keys are team names and values are dictionaries with the following keys:
        - 'GF' (int): Goals For
        - 'GA' (int): Goals Against
        - 'GD' (int): Goal Difference
        - 'Points' (int): Points earned in the match (3 for a win, 1 for a draw, 0 for a loss)
    The function updates the following statistics for each team in the table:
        - 'Played' (int): Number of matches played
        - 'Won' (int): Number of matches won
        - 'Draw' (int): Number of matches drawn
        - 'Lost' (int): Number of matches lost
        - 'GF' (int): Total goals scored
        - 'GA' (int): Total goals conceded
        - 'GD' (int): Total goal difference
        - 'Points' (int): Total points earned
    """
    
    for team, stats in match_result.items():
        if team not in table:
            table[team] = {'Played': 0, 'Won': 0, 'Draw': 0, 'Lost': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Points': 0}
        
        table[team]["Played"] += 1
        table[team]["GF"] += stats["GF"]
        table[team]["GA"] += stats["GA"]
        table[team]["GD"] += stats["GD"]
        table[team]["Points"] += stats["Points"]
        
        # Update win, draw, and loss statistics
        if stats["Points"] == 3:
            table[team]["Won"] += 1
        elif stats["Points"] == 1:
            table[team]["Draw"] += 1
        else:
            table[team]["Lost"] += 1

def sort_table(table):
    """Sort the statistics table by points, goal difference, and goals scored"""
    return dict(sorted(table.items(), key=lambda item: (item[1]["Points"], item[1]["GD"], item[1]["GF"]), reverse=True))

def process_group_files(group_letter):
    """Processes the files of a group (matches, results, and writing the final table)"""
    filename_base = f"group_{group_letter}"

    # Initialize the table
    table = {}
    
    # Read and process the results
    with open(f"group_stage/results/result_{filename_base}.csv", "r", encoding="utf-8") as result_file:
        for line in result_file:
            match = line.strip().split(",")
            match_table = add_points(match)
            update_table(table, match_table)
    
    # Sort and write the final table
    table = sort_table(table)
    with open(f"group_stage/tables/table_{filename_base}.csv", "w", encoding="utf-8") as table_file:
        for team, stats in table.items():
            table_file.write(f"{team},{stats['Played']},{stats['Won']},{stats['Draw']},{stats['Lost']},{stats['GF']},{stats['GA']},{stats['GD']},{stats['Points']}\n")

def main_q3():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_dir, "..", "group_stage", "tables")

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(8):
        process_group_files(chr(65+i))

if __name__ == "__main__":
    main_q3()
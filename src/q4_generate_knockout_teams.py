import os

def generate_knockout_stage():
    """
    Generates the file for teams qualified for the knockout stage based on group stage tables.

    Args:
        group_stage_dir (str): Directory containing the group stage tables.
        knockout_stage_dir (str): Directory to save the file of qualified teams.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    group_stage_dir = os.path.join(base_dir, "..", "group_stage")
    knockout_stage_dir = os.path.join(base_dir, "..", "knockout_stage")

    table_directory = os.path.join(group_stage_dir, "tables")
    qualified_file_path = os.path.join(knockout_stage_dir, "qualified.csv")

    for i in range(8):  # Loop through groups A to H
        with open(os.path.join(table_directory, f"table_group_{chr(65+i)}.csv"), 'r', encoding="utf-8") as table_file:
            table = [line.strip().split(",") for line in table_file]
        with open(qualified_file_path, "w" if i == 0 else 'a', encoding="utf-8") as qualified_file:
            qualified_file.write(f"{table[0][0]},{chr(65+i)},1\n")  # First-place team
            qualified_file.write(f"{table[1][0]},{chr(65+i)},2\n")  # Second-place team

def main_q4():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    knockout_stage_dir = os.path.join(base_dir, "..", "knockout_stage")

    if not os.path.exists(knockout_stage_dir):
        os.makedirs(knockout_stage_dir)
    generate_knockout_stage()

if __name__ == "__main__":
    main_q4()
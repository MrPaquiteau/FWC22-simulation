import os
from src.q1_create_groups import main_q1
from src.q2_generate_groups_results import main_q2
from src.q3_create_group_tables import main_q3
from src.q4_generate_knockout_teams import main_q4
from src.q5_simulate_knockout_stage import main_q5

def main():
    main_q1()
    main_q2()
    main_q3()
    main_q4()
    main_q5()

if __name__ == "__main__":
    main()
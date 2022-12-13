"""
solve_part_1.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 4:28:57 pm

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""


from typing import Dict, List, Tuple


def operate_over_cpu(list_of_instructions: List[Tuple[str, str]], register_initial_state: int = 1) -> Dict[int, int]:

    register_state_per_cycle = {}
    register_state = register_initial_state
    cycle_no = 1
    while list_of_instructions:
        current_instruction = list_of_instructions.pop(0)

        if current_instruction[0] == "noop":
            register_state_per_cycle[cycle_no] = register_state
            cycle_no += 1
        elif current_instruction[0] == "addx":
            register_state_per_cycle[cycle_no] = register_state
            cycle_no += 1
            register_state_per_cycle[cycle_no] = register_state
            cycle_no += 1
            register_state += int(current_instruction[1])
            register_state_per_cycle[cycle_no] = register_state

        else:
            raise ValueError("Unexpected instruction")

    return register_state_per_cycle


def get_register_values_at_cycles(register_history: Dict[int, int], register_test_points: List[int]) -> List[int]:
    requested_register_values = [register_history[key] for key in register_test_points]
    return requested_register_values

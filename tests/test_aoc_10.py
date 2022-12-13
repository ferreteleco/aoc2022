"""
test_aoc_10.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 4:43:39 pm

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""


from aoc2022.functions.aoc10.solve_part_1 import (
    get_register_values_at_cycles,
    operate_over_cpu,
)


def test_cpu_execution() -> None:

    # Input data
    input_data = [("noop",), ("addx", "3"), ("addx", "-5")]

    register_states = operate_over_cpu(input_data)

    # At the start of the first cycle, the noop instruction begins execution. During the first cycle
    # X is 1. After the first cycle, the noop instruction finishes execution, doing nothing.
    # At the start of the second cycle, the addx 3 instruction begins execution. During the second
    # cycle, X is still 1.
    # During the third cycle, X is still 1. After the third cycle, the addx 3 instruction finishes
    # execution, setting X to 4.
    # At the start of the fourth cycle, the addx -5 instruction begins execution. During the fourth
    # cycle, X is still 4.
    # During the fifth cycle, X is still 4. After the fifth cycle, the addx -5 instruction finishes
    # execution, setting X to -1.

    assert len(register_states) == 6

    assert register_states[1] == 1
    assert register_states[2] == 1
    assert register_states[3] == 1
    assert register_states[4] == 4
    assert register_states[5] == 4
    assert register_states[6] == -1


def test_signal_strength() -> None:

    # Input data
    input_data = [("noop",), ("addx", "3"), ("addx", "-5")]

    register_states = operate_over_cpu(input_data)
    cpu_cycle_test_points = [1, 3, 4]

    register_values = get_register_values_at_cycles(register_states, cpu_cycle_test_points)

    result = sum([cycle * value for cycle, value in zip(cpu_cycle_test_points, register_values)])

    assert result == 20

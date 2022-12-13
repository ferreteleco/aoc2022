"""
aoc10.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 4:20:54 pm

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""

from pathlib import Path

from aoc2022.functions.aoc10.process_input import process_input, format_input
from aoc2022.functions.aoc10.solve_part_1 import (
    get_register_values_at_cycles,
    operate_over_cpu,
)
from aoc2022.functions.aoc10.solve_part_2 import operate_over_screen


def aoc10_1(file_path: Path):
    raw_lines = process_input(file_path)
    processed_instructions = format_input(raw_lines)

    cpu_register = operate_over_cpu(processed_instructions)
    cpu_cycle_test_points = [20, 60, 100, 140, 180, 220]
    register_values = get_register_values_at_cycles(cpu_register, cpu_cycle_test_points)

    result = sum([cycle * value for cycle, value in zip(cpu_cycle_test_points, register_values)])

    print(f"> The signal strength is: {result}")


def aoc10_2(file_path: Path) -> None:
    raw_lines = process_input(file_path)
    processed_instructions = format_input(raw_lines)

    cpu_register = operate_over_cpu(processed_instructions)
    screen = operate_over_screen(cpu_register)
    print(screen)

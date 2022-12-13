"""
solve_part_2.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 5:50:13 pm

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""

from typing import Dict


def operate_over_screen(cpu_registe_per_cycle: Dict[int, int]):

    MAX_PIXEL_COL = 40
    MAX_PIXEL_ROW = 6

    current_row = 0
    current_pixel = 0

    screen = [["." for _ in range(MAX_PIXEL_COL)] for _ in range(MAX_PIXEL_ROW)]

    for cycle, register_value in cpu_registe_per_cycle.items():

        print(f"Cycle: {cycle} => row: {current_row} - col: {current_pixel}")
        target_pixel = (register_value) % MAX_PIXEL_COL

        if current_pixel in [
            target_pixel - 1,
            target_pixel,
            target_pixel + 1,
        ]:
            screen[current_row][current_pixel] = "#"

        if current_pixel == MAX_PIXEL_COL - 1:
            current_row = (current_row + 1) % MAX_PIXEL_ROW
        current_pixel = (current_pixel + 1) % MAX_PIXEL_COL

    screen_str = "\n".join(["".join(line) for line in screen])

    return screen_str

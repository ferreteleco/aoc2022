"""
process_input.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 4:17:11 pm

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""

from pathlib import Path
from typing import List, Tuple


def process_input(file_path: Path) -> List[str]:

    lines = []
    with file_path.open("r") as f:
        lines = f.readlines()

    return lines


def format_input(raw_lines: List[str]) -> List[Tuple[str, str]]:

    list_of_instructions = []
    for line in raw_lines:
        list_of_instructions.append(tuple(line.strip().split(" ")))

    return list_of_instructions

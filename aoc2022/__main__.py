"""
__main__.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 11:23:27 am

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""


from pathlib import Path
from sys import argv

from rich import print as display

from aoc2022 import main
from aoc2022.data.constants import AoCDay

if __name__ == "__main__":

    try:
        aoc_day = AoCDay(argv[1])
        input_file_path = Path(argv[2])

        if len(argv) > 3:
            raise IndexError

        if not input_file_path.is_file():
            raise FileNotFoundError()

        main(aoc_day, input_file_path)

    except IndexError:
        display(f"[bold red]Incorrect number of input arguments. Expecting 2 input arguments, found {len(argv) - 1}")

    except ValueError:
        display(
            f"[bold red]Incorrect format for input value. Expecting int (AoC day), found {argv[1]} ({type(argv[1])})"
        )

    except FileNotFoundError:
        display(f"[bold red]Input file ({argv[2]}) is not a valid file")

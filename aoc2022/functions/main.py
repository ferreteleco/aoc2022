"""
main.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 11:23:27 am

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""


from pathlib import Path
from timeit import default_timer as timer

from rich import print as display

from aoc2022.data.constants import AoCDay
from aoc2022.functions.aoc10.aoc10 import aoc10_1, aoc10_2


def main(aoc_day: AoCDay, input_file_path: Path) -> None:
    """Main method, in charge of select the proper day and provide a solution for.

    Args:
        aoc_day (AoCDay): Day to solve.
        input_file_path (Path): Path to the input file for the specified day.

    Raises:
        NotImplementedError: Whenever a day's solution is not available.
    """

    display("\n\n[bold green]*** Welcome to AoC project ***\n")

    try:

        match aoc_day:
            case AoCDay.DAY_10:
                display("[blue]Entrypoint[/blue] for [blue]part I[/blue] goes [blue]here[/blue]")
                t_init = timer()
                aoc10_1(input_file_path)
                t_end = timer()
                elapsed_1 = t_end - t_init

                display("[blue]Entrypoint[/blue] for [blue]part II[/blue] goes [blue]here[/blue]")
                t_init = timer()
                aoc10_2(input_file_path)
                t_end = timer()
                elapsed_2 = t_end - t_init
            case _:
                raise NotImplementedError

        display("\n")
        display(f"Elapsed time for AoC-{aoc_day} part I was {elapsed_1} s")
        display(f"Elapsed time for AoC-{aoc_day} part II was {elapsed_2} s")

    except NotImplementedError:
        display(f"[bold red]This AoC ({aoc_day}) has not been solved")

    finally:
        display("\n[bold yellow]*** Finished! Bye Bye! ***\n\n")

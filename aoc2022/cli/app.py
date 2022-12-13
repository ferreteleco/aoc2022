"""
app.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 11:23:27 am

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""


from pathlib import Path
from typer import Typer, Argument

from aoc2022.data.constants import AoCDay
from aoc2022.functions.main import main

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = Typer(
    add_completion=True,
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=False,
)


@app.command()
def run(
    aoc_day: AoCDay = Argument(..., help="AoC day to get the solution for"),
    input_file_path: Path = Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
    ),
):
    """Entrypoint for the AoC2022 solver.

    Args:
        aoc_day (AoCDay): Target day from which to solve its problems.
        input_file_path (Path): Path to the input file for the selected day.
    """

    main(aoc_day, input_file_path)

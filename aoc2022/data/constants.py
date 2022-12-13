"""
constants.py

Project: aoc2022

Maintainer Andrés Ferreiro González (aferreiro@gradiant.org)
Created @ Tuesday, 13th December 2022 11:23:27 am

Copyright (c) 2022 GRADIANT
All Rights Reserved
"""


from enum import Enum, unique


@unique
class AoCDay(str, Enum):
    """This enum is used for providing typer a method of validating which days' solutions are available.

    The inheritance of both str and Enum is a requirement from Typer. With IntEnum / plain Enum, this does not work.
    """

    DAY_9 = 9

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)

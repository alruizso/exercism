"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the total time of preparation.

    :param number_of_layers: int - Total number of lasagna layers
    :return_ int - total amount of time expended making the lasagna

    Function that takes the total number of layers of lasagna as an argument and
    returns the total expend time based on the `PREPARATION_TIME`.
    """
    
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the total time to prepare a lasagna.

    :param number_of_layers: int - Total nomber of layers on the lasagna.
    :param elapsed_time: int - Time already expended backing the lasagna.
    :returns: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

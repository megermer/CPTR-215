# Meg Ermer
# CPTR 215 A, Lab B
# Sources:
    # Sliding puzzle from Ms. Sanchez's desk
    # No online sources used

"""Sliding Puzzle
Prof. O and _____
2021-09-16 first draft

A Sliding Puzzle is represented by a string
whose length is a perfect square
of an integer in [2, 6] (i.e., 4, 9, 16, 25, or 36).
It contains only digits (0-9) and capital letters (A-Z),
exactly ONE of which (typically 0) is "empty"
and is represented by a hyphen (-).

On screen, however, the layout is an NxN square.
Legal moves consist of sliding a tile
up, down, left, or right (but never diagonally)
into the empty spot (-).

The puzzle is in the "solved" state when
all its digits and letters are in ascending order
(with digits before letters, as in ASCII and Unicode)
and the empty spot is at the beginning or end
(never in the middle).

References:
https://mathworld.wolfram.com/15Puzzle.html
https://lorecioni.github.io/fifteen-puzzle-game/
https://15puzzle.netlify.app/
"""

from sys import int_info
from types import NoneType
from typing import Tuple
from xml.dom.expatbuilder import parseString

def get_row_size(length : int) -> int:
    """
    Given the length of the table, return how many indices the rows are
    :param length: int
    :return: int

    >>> get_row_size(4)
    2
    >>> get_row_size(9)
    3
    >>> get_row_size(16)
    4
    >>> get_row_size(25)
    5
    >>> get_row_size(36)
    6
    """
    if length == 4:
        return 2
    elif length == 9:
        return 3
    elif length == 16:
        return 4
    elif length == 25:
        return 5
    elif length == 36:
        return 6

def is_corner_top_left(index : int) -> bool:
    """
    Given the number of the index, determines if the index is the top left corner
    :param index: int
    :return: bool

    >>> is_corner_top_left(0)
    True
    >>> is_corner_top_left(8)
    False
    """
    if index == 0:
        return True
    return False

def is_corner_top_right(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is the top right corner
    :param length: int
    :param index: int
    :return: bool

    >>> is_corner_top_right(9, 2)
    True
    >>> is_corner_top_right(9, 3)
    False
    """
    row_size = get_row_size(length)
    if index == row_size - 1:
        return True
    return False

def is_corner_bottom_left(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is the bottom left corner
    :param length: int
    :param index: int
    :return: bool

    >>> is_corner_bottom_left(9, 6)
    True
    >>> is_corner_bottom_left(9, 5)
    False
    """
    row_size = get_row_size(length)
    if index == length - row_size:
        return True
    return False

def is_corner_bottom_right(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is the bottom right corner
    :param length: int
    :param index: int
    :return: bool

    >>> is_corner_bottom_right(9, 8)
    True
    >>> is_corner_bottom_right(9, 2)
    False
    """
    if index == length - 1:
        return True
    return False

def is_top_edge(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is along the top edge
    :param length: int
    :param index: int
    :return: bool

    >>> is_top_edge(9, 1)
    True
    >>> is_top_edge(9, 6)
    False
    """
    row_size = get_row_size(length)
    if (index > 0) and (index < row_size):
        return True
    return False

def is_right_edge(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is along the right edge
    :param length: int
    :param index: int
    :return: bool

    >>> is_right_edge(9, 5)
    True
    >>> is_top_edge(9, 6)
    False
    """
    row_size = get_row_size(length)
    if (index == (length - 1) - row_size) or (index == (length - 1) - (2 * row_size)) or (index == (length - 1) - (3 * row_size)) or (index == (length - 1) - (4 * row_size)):
        return True
    return False

def is_bottom_edge(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is along the bottom edge
    :param length: int
    :param index: int
    :return: bool

    >>> is_bottom_edge(9, 7)
    True
    >>> is_bottom_edge(9, 6)
    False
    """
    row_size = get_row_size(length)
    if (index > (length - row_size)) and (index < (length - 1)):
        return True
    return False

def is_left_edge(length : int, index : int) -> bool:
    """
    Given the length and number of the index, determines if the index is along the left edge
    :param length: int
    :param index: int
    :return: bool

    >>> is_left_edge(9, 3)
    True
    >>> is_left_edge(9, 7)
    False
    """
    row_size = get_row_size(length)
    if (index == row_size) or (index == row_size * 2) or (index == row_size * 3) or (index == row_size * 4):
        return True
    return False

def rows_from_puzzle(puzzle : str) -> str:
    """
    Returns a string with a newline between rows of the puzzle.
    :param puzzle: str
    :return: str

    >>> rows_from_puzzle('1234123412341234')
    '1234\\n1234\\n1234\\n1234'
    >>> rows_from_puzzle('1234')
    '12\\n34'
    >>> rows_from_puzzle('123456789')
    '123\\n456\\n789'
    >>> rows_from_puzzle('1234512345123451234512345')
    '12345\\n12345\\n12345\\n12345\\n12345'
    >>> rows_from_puzzle('123456123456123456123456123456123456')
    '123456\\n123456\\n123456\\n123456\\n123456\\n123456'
    """
    new_puzzle_string = ""
    row_size = get_row_size(len(puzzle))
    for i in range(len(puzzle)):
        new_puzzle_string += puzzle[i]
        if (i + 1) == len(puzzle):
            break
        if (i + 1) % row_size == 0:
            new_puzzle_string += "\n"
    return new_puzzle_string 

def is_solved(puzzle : str) -> bool:
    """
    Determines whether puzzle is solved (as defined above).
    :param puzzle: str
    :return: bool

    >>> is_solved('123-')
    True
    >>> is_solved('-123')
    True
    >>> is_solved('1-23')
    False
    >>> is_solved('-12345678')
    True
    >>> is_solved('-26183627')
    False
    >>> is_solved('12345678-')
    True
    >>> is_solved('17382927-')
    False
    >>> is_solved('123-45678')
    False
    """
    counter = 0
    if (puzzle[0] == "-") or (puzzle[-1] == "-"):
        if puzzle[-1] == "-":
            for i in range(len(puzzle)-2):
                if puzzle[i] > puzzle[i+1]:
                    return False
                counter += 1
        else:
            for i in range(len(puzzle)-2):
                if puzzle[i+1] > puzzle[i+2]:
                    return False
                counter += 1
    if counter > 0:
        return True    
    return False 

def is_legal_move(puzzle : str, tile_to_move : str) -> bool:
    """
    Determines whether it is possible to move tile_to_move into the empty spot.
    :param puzzle: str
    :param tile_to_move: str
    :return: bool

    >>> is_legal_move('E79-C48B26D53AF1', '5')
    False

    >>> is_legal_move('1-34', '1')
    True
    >>> is_legal_move('12-4', '1')
    True
    >>> is_legal_move('123-', '1')
    False
    >>> is_legal_move('123-56789', '1')
    True
    >>> is_legal_move('1234-6789', '1')
    False

    >>> is_legal_move('-234', '2')
    True
    >>> is_legal_move('123-', '2')
    True
    >>> is_legal_move('12-4', '2')
    False
    >>> is_legal_move('12345612345-123456123456123456123456', '6')
    True

    >>> is_legal_move('123-', '3')
    True
    >>> is_legal_move('1-34', '3')
    False
    >>> is_legal_move('-234', '3')
    True
    >>> is_legal_move('123456789ABCDEF-HIJKLMNOP', 'L')
    True

    >>> is_legal_move('1-34', '4')
    True
    >>> is_legal_move('12-4', '4')
    True
    >>> is_legal_move('-234', '4')
    False
    >>> is_legal_move('123456789ABCDEFGHIJ-LMNOP', 'P')
    True
    >>> is_legal_move('123456789ABCDEFG-IJKLMNOP', 'P')
    False

    >>> is_legal_move('1234-6789', '2')
    True
    >>> is_legal_move('-23456789', '2')
    True
    >>> is_legal_move('12-456789', '2')
    True
    >>> is_legal_move('12345678-', '2')
    False

    >>> is_legal_move('12-456789', '6')
    True
    >>> is_legal_move('1234-6789', '6')
    True
    >>> is_legal_move('12345678-', '6')
    True
    >>> is_legal_move('123-56789', '6')
    False

    >>> is_legal_move('123456-89', '8')
    True
    >>> is_legal_move('12345678-', '8')
    True
    >>> is_legal_move('1234-6789', '8')
    True
    >>> is_legal_move('1-3456789', '8')
    False
    >>> is_legal_move('123456789ABCDEFGHI-KLMNOP', 'O')
    True
    >>> is_legal_move('123456789-BCDEFGHIJKLMNOP', 'O')
    False

    >>> is_legal_move('1234-6789', '4')
    True
    >>> is_legal_move('-23456789', '4')
    True
    >>> is_legal_move('123456-89', '4')
    True
    >>> is_legal_move('1-3456789', '4')
    False
    >>> is_legal_move('123456789A-CDEFGHIJKLMNOP', '6')
    True
    >>> is_legal_move('123456789ABCDEFGHIJK-MNOP', 'G')
    True
    >>> is_legal_move('123456789-BCDEFGHIJKLMNOP', 'B')
    False

    >>> is_legal_move('12345678-ABCDEFGHIJKLMNOP', 'E')
    True
    >>> is_legal_move('123456789ABCDEFGHIJKL-NOP', 'H')
    True
    >>> is_legal_move('123456789ABCDEFGHIJ-LMNOP', '7')
    False

    """
    puzzle_list = list(puzzle)
    length = len(puzzle)
    row_size = get_row_size(length)
    tile_index = puzzle_list.index(tile_to_move)
    dash_index = puzzle_list.index("-")
    if tile_to_move == "-": 
        return False
    elif is_corner_top_left(tile_index):
        if (dash_index == tile_index + 1) or (dash_index == tile_index + row_size):
            return True
    elif is_corner_top_right(length, tile_index):
        if (dash_index == tile_index - 1) or (dash_index == tile_index + row_size):
            return True
    elif is_corner_bottom_left(length, tile_index):
        if (dash_index == tile_index + 1) or (dash_index == tile_index - row_size):
            return True
    elif is_corner_bottom_right(length, tile_index):
        if (dash_index == length - 2) or (dash_index == length - row_size - 1):
            return True
    elif is_top_edge(length, tile_index):
        if (dash_index == tile_index - 1) or (dash_index == tile_index + 1) or (dash_index == tile_index + row_size):
            return True
    elif is_right_edge(length, tile_index):
        if (dash_index == tile_index - 1) or (dash_index == tile_index + row_size) or (dash_index == tile_index - row_size):
            return True
    elif is_bottom_edge(length, tile_index):
        if (dash_index == tile_index - 1) or (dash_index == tile_index + 1) or (dash_index == tile_index - row_size):
            return True
    elif is_left_edge(length, tile_index):
        if (dash_index == tile_index + 1) or (dash_index == tile_index + row_size) or (dash_index == tile_index - row_size):
            return True
    else:
        if (dash_index == tile_index + 1) or (dash_index == tile_index - 1) or (dash_index == tile_index + row_size) or (dash_index == tile_index - row_size):
            return True
    return False 

def puzzle_with_move(puzzle : str, tile_to_move : str) -> str:
    """
    Move tile_to_move into the empty slot (-).
    :param puzzle: str
    :param tile_to_move: str
    :return: str

    >>> puzzle_with_move('12-4', '4')
    '124-'
    >>> puzzle_with_move('12345-789', '9')
    '12345978-'
    """
    puzzle_list = list(puzzle)
    tile_index = puzzle_list.index(tile_to_move)
    dash_index = puzzle_list.index("-")
    puzzle_list[dash_index] = puzzle_list[tile_index]
    puzzle_list[tile_index] = "-"
    new_puzzle_string = ""
    for index in puzzle_list:
        new_puzzle_string += index
    return new_puzzle_string 

def space_puzzle(puzzle : str) -> str:
    return " " + " ".join(rows_from_puzzle(puzzle))

def play_puzzle(puzzle : str) -> None:
    moves = 0
    while not is_solved(puzzle):
        print(f"\nCurrent puzzle state:\n{space_puzzle(puzzle)}")
        tile_to_move = "-"
        moves += 1
        print(f"Move #{moves}")
        while not is_legal_move(puzzle, tile_to_move):
            tile_to_move = input("Which tile would you like to move into the empty spot? ")        
        puzzle = puzzle_with_move(puzzle, tile_to_move)
    print(f"\nSolved!\n{space_puzzle(puzzle)}")
    print(f"You solved the puzzle in {moves} moves!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    play_puzzle("178-65234")
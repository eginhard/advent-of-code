import itertools
import re
from collections.abc import Iterable, Iterator
from typing import Any, TypeVar

import numpy as np
import numpy.typing as npt

_T = TypeVar("_T")

DIRECTIONS = {
    "4": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "diagonals": [(1, 1), (1, -1), (-1, -1), (-1, 1)],
}
DIRECTIONS["8"] = [*DIRECTIONS["4"], *DIRECTIONS["diagonals"]]
DIRECTIONS["9"] = [*DIRECTIONS["8"], (0, 0)]


def det2x2(a: int, b: int, c: int, d: int) -> int:
    """Determinant of a 2x2 matrix.

    | a b |
    | c d |  = ad - bc
    """
    return a * d - b * c


def diff_consecutive(xs: list[int]) -> list[int]:
    """Get differences of consecutive integers in the list.

    [0, 3, 6] -> [3, 3]
    """
    return [y - x for x, y in itertools.pairwise(xs)]


def grouper(
    iterable: Iterable[_T],
    n_chunks: int,
    *,
    incomplete: str = "fill",
    fillvalue: _T | None = None,
) -> Iterator[tuple[_T, ...]]:
    """Collect data into non-overlapping fixed-length chunks or blocks.

    Adapted from:
    https://docs.python.org/3/library/itertools.html#itertools-recipes
    """
    # grouper("ABCDEFG", 3, fillvalue="x") --> ABC DEF Gxx
    # grouper("ABCDEFG", 3, incomplete="strict") --> ABC DEF ValueError
    # grouper("ABCDEFG", 3, incomplete="ignore") --> ABC DEF
    # This passes the _same_ iterator multiple times, so it reads successive values
    args = [iter(iterable)] * n_chunks
    if incomplete == "fill":
        return itertools.zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args, strict=False)
    msg = "`incomplete` must be one of: fill, strict, ignore"
    raise ValueError(msg)


def find_cycle(xs: list[Any], min_length: int = 2) -> None | tuple[int, int]:
    """Find a repeating cycle start index and its length in the list.

    [1, 2, 3, 4, 2, 3, 4] -> (1, 3)
    """
    for k in range(min_length, len(xs) // 2 + 1):
        for i in range(len(xs) - k):
            if xs[i : i + k] == xs[i + k : i + k + k]:
                return i, k
    return None


def find_numbers(string: str) -> list[int]:
    """Find numbers in a string.

    "adcv93 bb7c 82 1" -> [93, 7, 82, 1]
    """
    return [int(d) for d in re.findall(r"\d+", string)]


def lines_to_numpy(lines: list[str]) -> npt.NDArray[np.int_]:
    """Converts an array of integer strings into a numpy array.

    ["123", "456", "789"] -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return np.array([list(line) for line in lines], dtype=int)


def rotate_90deg(dx: int, dy: int, *, clockwise: bool = True) -> tuple[int, int]:
    """Rotate the given directions by 90 degrees."""
    if clockwise:
        return dy, -dx
    return -dy, dx

import itertools
import re
from collections.abc import Iterable, Iterator
from typing import TypeVar

import numpy as np
import numpy.typing as npt

_T = TypeVar("_T")

DIRECTIONS = {
    "4": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "diagonals": [(1, 1), (1, -1), (-1, -1), (-1, 1)],
}
DIRECTIONS["8"] = [*DIRECTIONS["4"], *DIRECTIONS["diagonals"]]
DIRECTIONS["9"] = [*DIRECTIONS["8"], (0, 0)]


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

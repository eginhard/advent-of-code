import pytest

from aoc.utils import merge_ranges


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        ([(3, 5), (10, 14), (16, 20), (12, 18)], [(3, 5), (10, 20)]),
        ([(3, 5), (12, 18), (16, 20), (10, 14)], [(3, 5), (10, 20)]),
        ([(3, 5), (10, 14), (16, 20)], [(3, 5), (10, 14), (16, 20)]),
        ([(1, 10), (2, 5), (3, 7), (4, 10)], [(1, 10)]),
        ([(2, 4), (2, 4), (2, 4)], [(2, 4)]),
        ([(1, 5), (5, 10), (10, 15)], [(1, 15)]),
        ([], []),
    ],
)
def test_merge_ranges(
    test_input: list[tuple[int, int]],
    expected: list[tuple[int, int]],
) -> None:
    assert merge_ranges(test_input) == expected

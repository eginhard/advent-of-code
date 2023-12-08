from pathlib import Path

import aocd
from aocd.examples import Example
from aocd.models import Puzzle

INPUT_DIR = Path("input")


def get_data(filename: str) -> tuple[list[str], str, str, list[Example]]:
    """Download data."""
    year, day = Path(filename).stem.split("_")
    INPUT_DIR.mkdir(exist_ok=True, parents=True)
    input_file = INPUT_DIR / f"{year}_{day}"

    puzzle = Puzzle(year=int(year), day=int(day))

    data = aocd.get_data(day=int(day), year=int(year))
    with input_file.open("w") as f:
        f.write(data)
    return data.splitlines(), year, day, puzzle.examples


def print_examples(examples: list[Example], w: int = 80) -> None:
    for i, example in enumerate(examples, start=1):
        print(f" Example data {i}/{len(examples)} ".center(w, "-"))
        print(example.input_data)
        print("-" * w)
        print("answer_a:", example.answer_a or "-")
        print("answer_b:", example.answer_b or "-")
        if example.extra:
            print("extra:", example.extra)
            print("-" * w)
            print()
            print()

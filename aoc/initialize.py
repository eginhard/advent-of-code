import argparse
import importlib.resources
import shutil
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int, default=datetime.today().day)
    parser.add_argument("-y", "--year", type=int, default=datetime.today().year)
    return parser.parse_args()


def initialize() -> None:
    args = parse_args()
    print(f"Setting up AOC puzzle {args.year}-{args.day:02}")
    puzzle_dir = Path(str(args.year))
    puzzle_dir.mkdir(exist_ok=True)
    puzzle_fn = puzzle_dir / f"{args.year}_{args.day:02}.org"
    with importlib.resources.as_file(importlib.resources.files("aoc")) as pkg_dir:
        template_fn = pkg_dir / "template.org"
        shutil.copyfile(template_fn, puzzle_fn)


if __name__ == "__main__":
    initialize()

""" Day 4: Camp Cleanup
    https://adventofcode.com/2022/day/4
"""

def read_input() -> str:
    """Read the inputs from inputs.txt

    Returns:
        str: A raw string of the inputs
    """
    with open("4-camp_cleanup/input.txt", "r", encoding="utf-8") as input_file:
        return input_file.read()

class Elf:
    """A class to hold attributes about an elf
    """
    min: int
    max: int

    range: set

    def __init__(self, min_max: tuple[int, int]):
        self.min = min_max[0]
        self.max = min_max[1]

        self.range = set(range(self.min, self.max+1))

def split_pairs(inp: str) -> list:
    """Splits each of the entires into their pair groups

    Args:
        inp (str): The raw input string

    Returns:
        list: A list of pair groups
    """
    return inp.split("\n")

def split_elves(inp: str) -> tuple[str, str]:
    """Splits each pair into individual elves

    Args:
        inp (str): The pair group string

    Returns:
        tuple[str, str]: The two elves (left and right)
    """
    elves: list = inp.split(",")
    return elves[0], elves[1]

def split_min_and_max(inp: str) -> tuple[int, int]:
    """Splits the elf's ranges into a min and max value

    Args:
        inp (str): The elf's range

    Returns:
        tuple[int, int]: Their minimum and maximum value
    """
    values: list = inp.split("-")
    return int(values[0]), int(values[1])

def is_intersect(reoccuring: list, elf1: Elf, elf2: Elf) -> bool:
    """Logic for whether the two elf's ranges intersect
    If first item and last item of range == elf1 min and max
    or 
    If first item and last item of range == elf 2 min and max
    We know that they must wholly contain eachother

    Args:
        reoccuring (list): A list of values that appear in both elves ranges
        elf1 (Elf): The first elf's object
        elf2 (Elf): The second elf's object

    Returns:
        bool: A boolean to indicate whether one of the elf's range wholly contains the other
    """
    reoccuring.sort()
    if len(reoccuring) == 0:
        return False

    return (
        (reoccuring[0] == elf1.min and reoccuring[-1] == elf1.max) or
        (reoccuring[0] == elf2.min and reoccuring[-1] == elf2.max)
    )

def count_fully_contain(inp: str) -> int:
    """Find the count of elf pairs whose assignments fully contain the other

    Args:
        inp (str): The raw string of all elf pairs

    Returns:
        int: The number of elf pairs whose assignments fully contain the other
    """
    pairs = split_pairs(inp)

    total: int = 0

    for pair in pairs:
        left, right = split_elves(pair)

        elf1: Elf = Elf(split_min_and_max(left))
        elf2: Elf = Elf(split_min_and_max(right))

        elf_set: set = set(elf1.range & elf2.range)

        total += 1 if is_intersect(list(elf_set), elf1, elf2) else 0

    return total

def main():
    """Main function - do logic
    """
    count_fully_contained: int = count_fully_contain(read_input())

    print(count_fully_contained)

if __name__ == "__main__":
    main()

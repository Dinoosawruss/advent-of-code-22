""" Day 3: Rucksack Reorganization
    https://adventofcode.com/2022/day/3
"""

def read_input() -> str:
    """Read the inputs from inputs.txt

    Returns:
        str: A raw string of the inputs
    """
    with open("3-rucksack_reorganization/input.txt", "r", encoding="utf-8") as input_file:
        return input_file.read()

def split_rucksacks(inp: str) -> list:
    """Split the raw input string into a list of rucksacks

    Args:
        inp (str): The raw input string

    Returns:
        list: A list of rucksacks as strings
    """
    return inp.split("\n")

def split_compartment(inp: str) -> str and str:
    """Split each rucksack into its compartments (split in middle)

    Args:
        inp (str): The rucksack as a string

    Returns:
        str and str: The left compartment and right compartment
    """
    middle_index = len(inp)//2

    return inp[middle_index:], inp[:middle_index]

def items_in_both_compartments(rucksack_raw: str) -> list:
    """Find the reoccuring item in each rucksack

    Args:
        rucksack_raw (str): The raw string of rucksacks

    Returns:
        list: A list of items that reoccur in a rucksack
    """
    items_in_both: list = []

    rucksacks: list = split_rucksacks(rucksack_raw)

    for rucksack in rucksacks:
        left_comp, right_comp = split_compartment(rucksack)

        items_in_both += set(left_comp) & set(right_comp)

    return items_in_both

def calculate_priority(item: chr) -> int:
    """Calculate the priority of an item 

    Args:
        item (chr): The item to calculate the priority of

    Returns:
        int: The priority of that item
    """
    item = item.swapcase() # Uppercase are lower in ASCII values so lets swap them
    steps_down: int = 70 if item.islower() else 64

    return ord(item) - steps_down

def priority_sum(items: list) -> int:
    """Find the sum of priorities of a list of items

    Args:
        items (list): The list of items

    Returns:
        int: The sum of priorities
    """
    total: int = 0

    for item in items:
        total += calculate_priority(item)

    return total

def main():
    """Main function - read input and do logic
    """
    items_in_both: list = items_in_both_compartments(read_input())

    total_priority = priority_sum(items_in_both)

    print(total_priority)


if __name__ == "__main__":
    main()

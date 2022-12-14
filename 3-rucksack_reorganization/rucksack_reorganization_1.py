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

def split_groups(rucksack_raw: str) -> list:
    """Split the raw input into groups of 3

    Args:
        rucksack_raw (str): The raw rucksack input

    Returns:
        list: Each group of 3 rucksacks
    """
    outp: list = []

    rucksacks: list = split_rucksacks(rucksack_raw)

    for i in range(len(rucksacks)//3):
        index: int = i*3

        outp.append([
            rucksacks[index],
            rucksacks[index + 1],
            rucksacks[index + 2]
        ])

    return outp

def identifiers_common_between_groups(rucksack_raw: str) -> list:
    """Find all of the identifiers common between groups

    Args:
        rucksack_raw (str): The raw string of input

    Returns:
        list: A list of all common identifiers
    """
    group_identifiers: list = []

    groups: list = split_groups(rucksack_raw)

    for group in groups:
        group_identifiers += set(group[0]) & set(group[1]) & set(group[2])

    return group_identifiers

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
    print(f"1: {total_priority}")

    group_identifiers: list = identifiers_common_between_groups(read_input())
    total_priority = priority_sum(group_identifiers)
    print(f"2: {total_priority}")

if __name__ == "__main__":
    main()

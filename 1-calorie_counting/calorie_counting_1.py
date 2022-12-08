""" Day 1: Calorie Counting
    https://adventofcode.com/2022/day/1
"""

def read_input() -> str:
    """Read the inputs from inputs.txt

    Returns:
        str: A raw string of the inputs
    """
    with open("1-calorie_counting/input.txt", "r", encoding="utf-8") as input_file:
        return input_file.read()

def split_elf(inp: str) -> list:
    """Split the inputs into strings of elves

    Args:
        inp (str): The raw string input

    Returns:
        list: A list of each elf's string inventory
    """
    return inp.split("\n\n")

def split_elves_inventory(inp: str) -> list:
    """Split each elves string inventory into an individual list

    Args:
        inp (str): The string inventory of the elves

    Returns:
        list: The list of calories in their inventory
    """
    return inp.split("\n")

def get_highest_calories(elf_inventories_str: str) -> int:
    """Get the highest total calories

    Args:
        elf_inventories_str (str): The raw list of elf inventories

    Returns:
        int: The highest total calories an elf has as an integer
    """
    curr_max: int = -1

    elves: list = split_elf(elf_inventories_str)

    for elf in elves:
        inventory: list = [int(x) for x in split_elves_inventory(elf)] 
        sum_inv: int = sum(inventory)

        curr_max = sum_inv if sum_inv > curr_max else curr_max

    return curr_max

def main():
    """Main function - execute logic and print result
    """
    highest_calories = get_highest_calories(read_input())

    print(highest_calories)


if __name__ == "__main__":
    main()

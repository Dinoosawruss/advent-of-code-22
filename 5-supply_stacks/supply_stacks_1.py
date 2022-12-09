""" Day 5: Supply Stacks
    https://adventofcode.com/2022/day/5
"""

def read_input() -> str:
    """Read the inputs from inputs.txt

    Returns:
        str: A raw string of the inputs
    """
    with open("5-supply_stacks/input.txt", "r", encoding="utf-8") as input_file:
        return input_file.read()

def split_lines(inp: str) -> list:
    """Split the raw input into lines

    Args:
        inp (str): The raw input

    Returns:
        list: Each line of the input
    """
    return inp.split("\n")

def find_blank_line_index(lines: list) -> int:
    """Find the index of the blank line - thus the index of the instruction start is 1 further

    Args:
        lines (list): The lines of the input

    Returns:
        int: The index of the blank line
    """
    return lines.index("")

def split_instructions_and_current_state(lines: list) -> tuple[list, list]:
    """Split the input into the instructions and the current state of the towers

    Args:
        lines (list): The lines of the input

    Returns:
        tuple[list, list]: First list - current state, Second list - instructions
    """
    start_of_instructions: int = find_blank_line_index(lines)

    return lines[:start_of_instructions], lines[start_of_instructions+1:]

def split_row_into_crates(row: str) -> list:
    """Splits the row into sections of 4 (its crates)

    Args:
        row (str): The row to split

    Returns:
        list: A list of crates in that row (index = tower)
    """
    return [row[y-4:y] for y in range(4, len(row)+4,4)]

def populate_towers(current_state: list) -> list:
    """Populate the towers based on the current state

    Args:
        current_state (list): The current state in lines as a list

    Returns:
        list: The towers as a 2D list
        1st dimention - tower num
        2nd dimention - crates on the tower
    """
    outp: list = []
    counter: int

    current_state.reverse()

    first_run: bool = True

    for state_row in current_state:
        crates: list = split_row_into_crates(state_row)

        outp = [[] for _ in range(len(crates))] if first_run else outp
        first_run = False

        counter = 0
        for crate in crates:
            cleaned_chunk = crate.replace(" ", "")

            if cleaned_chunk != "":
                outp[counter].append(cleaned_chunk)

            counter += 1

    return outp

def instruction_components(instruction: str) -> tuple[int, int, int]:
    """Split each instruction into its components

    Args:
        instruction (str): The instruction itself

    Returns:
        tuple[int, int, int]: Three integers, quantity, move from, move to
    """
    new_instruction: str = instruction.replace("move", "").replace("from", "").replace("to", "")

    return [int(x) for x in new_instruction.split("  ")]

def compute_rearrangement(inp: str) -> list:
    """Work out the final state of the towers based on the instructions

    Args:
        inp (str): The raw input

    Returns:
        list: The final state of the towers
    """
    lines: list = split_lines(inp)

    current_state, instructions = split_instructions_and_current_state(lines)
    current_state.pop()

    towers: list = populate_towers(current_state)

    for inst in instructions:
        quantity, where_from, where_to = instruction_components(inst)
        where_from -= 1
        where_to -= 1

        for _ in range(quantity):
            crate: str = towers[where_from].pop()
            towers[where_to].append(crate)

    return towers

def find_message(towers: list) -> str:
    """Turn the towers final state into the flag

    Args:
        towers (list): The towers final state

    Returns:
        str: The flag for AOC
    """
    outp: str = ""

    for tower in towers:
        outp += tower[-1].replace("[", "").replace("]", "")

    return outp

def main():
    """Main function - do logic
    """
    towers: list = compute_rearrangement(read_input())

    print(find_message(towers))

if __name__ == "__main__":
    main()

""" Day 6: Tuning Trouble
    https://adventofcode.com/2022/day/6
"""

def read_input() -> str:
    """Read the inputs from inputs.txt

    Returns:
        str: A raw string of the inputs
    """
    with open("6-tuning_trouble/input.txt", "r", encoding="utf-8") as input_file:
        return input_file.read()

def find_start_of_packet(recieved_data: str) -> int:
    """Find the first group of 4 non-repeating characters (and thus start of packet)

    Args:
        recieved_data (str): The raw input data

    Returns:
        int: The index of the last item in the group of 4 non-repeating characters
    """
    window: list = [None, None, None, None]

    for start_window_index in range(len(recieved_data)-4):
        window = [
            recieved_data[start_window_index],
            recieved_data[start_window_index+1],
            recieved_data[start_window_index+2],
            recieved_data[start_window_index+3]
        ]

        unique: set = set(window)

        if len(unique) == 4:
            return start_window_index+4 # Final value

    return -1 # Couldn't find any

def main():
    """Main function - do logic
    """
    start_index: int = find_start_of_packet(read_input())
    print(start_index)

if __name__ == "__main__":
    main()

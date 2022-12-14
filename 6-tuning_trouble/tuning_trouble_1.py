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

def find_start_of_x(recieved_data: str, unique_chars_required: int) -> int:
    """Find the start of a marker in a string based on x unique chars

    Args:
        recieved_data (str): The raw input data
        unique_chars_required (int): The under of unique characters required to be correct

    Returns:
        int: The index of the final item in the location found
    """
    window: list = [None, None, None, None]

    for start_window_index in range(len(recieved_data)-unique_chars_required):
        window = [
            recieved_data[start_window_index+index] for index in range(unique_chars_required)
        ]

        unique: set = set(window)

        if len(unique) == unique_chars_required:
            return start_window_index+unique_chars_required # Final value

    return -1 # Couldn't find any

def find_start_of_packet(recieved_data: str) -> int:
    """Find the start of a packet (4 unique chars in a row)

    Args:
        recieved_data (str): The raw input data

    Returns:
        int: The index of the last item in the start of the packet flag
    """
    return find_start_of_x(recieved_data, 4)

def find_start_of_message_marker(recieved_data: str) -> int:
    """Find the start of a message marker (14 unique chars in a row)

    Args:
        recieved_data (str): The raw input data

    Returns:
        int: The index of the last item in the start of message marker flag
    """
    return find_start_of_x(recieved_data, 14)

def main():
    """Main function - do logic
    """
    start_packet_index: int = find_start_of_packet(read_input())
    print(start_packet_index)

    start_of_message_marker: int = find_start_of_message_marker(read_input())
    print(start_of_message_marker)

if __name__ == "__main__":
    main()

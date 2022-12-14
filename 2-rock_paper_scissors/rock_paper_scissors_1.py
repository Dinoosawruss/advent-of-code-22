""" Day 2: Rock Paper Scissors
    https://adventofcode.com/2022/day/2
"""

wins: dict[chr, chr] = {
    'A': 'Y', # Rock     - Paper
    'B': 'Z', # Paper    - Scissors
    'C': 'X', # Scissors - Rock
}

loses: dict[chr, chr] = {
    'A': 'Z', # Rock     - Scissors
    'B': 'X', # Paper    - Rock
    'C': 'Y'  # Scissors - Paper
}

draws: dict[chr, chr] = {
    'A': 'X', # Rock     - Rock
    'B': 'Y', # Paper    - Paper
    'C': 'Z'  # Scissors - Scissors
}

points: dict[chr, int] = {
    'X': 1, # Rock      - 1
    'Y': 2, # Paper     - 2
    'Z': 3, # Scissors  - 3
    'U': 6, # You win   - 6
    'D': 3, # Draw      - 3
    'E': 0  # Enemy win - 0
}

def read_input() -> str:
    """Read the inputs from inputs.txt

    Returns:
        str: A raw string of the inputs
    """
    with open("2-rock_paper_scissors/input.txt", "r", encoding="utf-8") as input_file:
        return input_file.read()

def get_rounds(inp: str) -> list:
    """Splits the raw string into individual rounds

    Args:
        inp (str): The raw input string

    Returns:
        list: A list of each rock paper scissor round
    """
    return inp.split("\n")

def get_move(inp: str, standard_rule_set: bool) -> chr and chr:
    """Work out the enemies and your move based on current conditions

    Args:
        inp (str): The move line string
        standard_rule_set (bool, optional): Whether the standard or problem 2 rule set are in use

    Returns:
        chr and chr: The enemies move, your move
    """
    enemy_move = inp[0]
    instruction = inp[-1]

    your_move: str = \
        instruction if standard_rule_set \
    else loses[enemy_move] if instruction == "X" \
    else draws[enemy_move] if instruction == "Y" \
    else wins[enemy_move] if instruction == "Z" \
    else ""

    return enemy_move, your_move


def is_winner_you(enemy_move: chr, your_move: chr) -> chr:
    """Calculate whether you are the winner

    Args:
        enemy_move (chr): The enemies move as a char
        your_move (chr): Your move as a char

    Returns:
        chr: Returns who win 'U' for you, 'D' for draw, 'E' for enemy
    """
    enemy_converted: chr = chr(ord(enemy_move) + 23) # Align enemies moves to yours for draw check

    return 'U' if wins[enemy_move] == your_move else 'D' if enemy_converted == your_move else 'E'

def calculate_points(your_move: chr, winner: chr) -> int:
    """Calculates the points from a round

    Args:
        your_move (chr): The move you made
        winner (chr): Winning state

    Returns:
        int: The number of points based on these conditions
    """
    return points[your_move] + points[winner]

def guided_total_score(guide: str, standard_rule_set: bool=True) -> int:
    """Calculate the total score the guide will net you

    Args:
        guide (str): The guide as a raw string

    Returns:
        int: The total score the guide will net
    """
    rounds: list = get_rounds(guide)

    enemy_move: chr
    your_move: chr
    winner: bool

    total_points: int = 0

    for rnd in rounds:
        enemy_move, your_move = get_move(rnd, standard_rule_set)
        winner = is_winner_you(enemy_move, your_move)
        total_points += calculate_points(your_move, winner)

    return total_points

def main():
    """Main function - Do logic and print total score
    """
    total_score: int = guided_total_score(read_input())
    print(f"1: {total_score}")

    total_score: int = guided_total_score(read_input(), False)
    print(f"2: {total_score}")

if __name__ == "__main__":
    main()

""" Day 2: Rock Paper Scissors
    https://adventofcode.com/2022/day/2
"""

rules: dict[chr, chr] = {
    'A': 'Y', # Rock     - Paper
    'B': 'Z', # Paper    - Scissors
    'C': 'X'  # Scissors - Rock
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

def get_play(inp: str) -> chr and chr:
    """Get the play that was made in a round by each player

    Args:
        inp (str): That round as a string

    Returns:
        chr and chr: The enemies move, your move
    """
    return inp[0], inp[-1] # Enemy, You

def is_winner_you(enemy_move: chr, your_move: chr) -> chr:
    """Calculate whether you are the winner

    Args:
        enemy_move (chr): The enemies move as a char
        your_move (chr): Your move as a char

    Returns:
        chr: Returns who win 'U' for you, 'D' for draw, 'E' for enemy
    """
    enemy_converted: chr = chr(ord(enemy_move) + 23) # Align enemies moves to yours for draw check

    return 'U' if rules[enemy_move] == your_move else 'D' if enemy_converted == your_move else 'E'

def calculate_points(your_move: chr, winner: chr) -> int:
    """Calculates the points from a round

    Args:
        your_move (chr): The move you made
        winner (chr): Winning state

    Returns:
        int: The number of points based on these conditions
    """
    return points[your_move] + points[winner]

def guided_total_score(guide: str) -> int:
    """Calculate the total score the guide will net you

    Args:
        guide (str): The guide as a raw string

    Returns:
        int: The total score the guide will net
    """
    rounds: list = get_rounds(guide)
    rounds.pop() # Remove last blank line

    enemy_move: chr
    your_move: chr
    winner: bool

    total_points: int = 0

    for rnd in rounds:
        enemy_move, your_move = get_play(rnd)
        winner = is_winner_you(enemy_move, your_move)
        total_points += calculate_points(your_move, winner)

    return total_points

def main():
    """Main function - Do logic and print total score
    """
    total_score: int = guided_total_score(read_input())

    print(total_score)

if __name__ == "__main__":
    main()

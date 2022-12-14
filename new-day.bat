@echo off
(
echo """ Day : 
echo     https://adventofcode.com/2022/day/
echo """
echo.
echo def read_input^(^) ^-^> str:
echo     """Read the inputs from inputs.txt
echo.
echo     Returns:
echo         str: A raw string of the inputs
echo     """
echo     with open^("6-tuning_trouble/input.txt", "r", encoding="utf-8"^) as input_file:
echo         return input_file.read^(^)
echo.
echo def main^(^):
echo     """Main function - do logic
echo     """
echo     print^(^)
echo.
echo if __name__ == "__main__":
echo     main^(^)
)

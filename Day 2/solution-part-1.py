import re

from Utils.Color import print_color, Color

RED_PATTERN = re.compile(r'(\d+) red', re.IGNORECASE)
GREEN_PATTERN = re.compile(r'(\d+) green', re.IGNORECASE)
BLUE_PATTERN = re.compile(r'(\d+) blue', re.IGNORECASE)
GAME_PATTERN = re.compile(r'Game (\d+)', re.IGNORECASE)
RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

valid_games_sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        is_valid_red = len([cubes for cubes in RED_PATTERN.findall(line) if int(cubes) > RED_LIMIT]) == 0
        is_valid_green = len([cubes for cubes in GREEN_PATTERN.findall(line) if int(cubes) > GREEN_LIMIT]) == 0
        is_valid_blue = len([cubes for cubes in BLUE_PATTERN.findall(line) if int(cubes) > BLUE_LIMIT]) == 0

        if is_valid_green and is_valid_red and is_valid_blue:
            valid_games_sum += int(GAME_PATTERN.findall(line)[0])

print(f'The sum of the numbers of the valid games is {print_color(valid_games_sum, Color.GREEN)}.')

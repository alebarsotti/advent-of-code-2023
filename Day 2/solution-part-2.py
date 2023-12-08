import re

from Utils.Color import print_color, Color

RED_PATTERN = re.compile(r'(\d+) red', re.IGNORECASE)
GREEN_PATTERN = re.compile(r'(\d+) green', re.IGNORECASE)
BLUE_PATTERN = re.compile(r'(\d+) blue', re.IGNORECASE)

cube_sets_power_sum = 0


def get_min_cube_count(pattern):
    return max([int(cubes) for cubes in pattern.findall(line)])


with open('input.txt', 'r') as file:
    for line in file:
        min_red_count = get_min_cube_count(RED_PATTERN)
        min_green_count = get_min_cube_count(GREEN_PATTERN)
        min_blue_count = get_min_cube_count(BLUE_PATTERN)

        cube_sets_power_sum += min_red_count * min_green_count * min_blue_count

print(f'The sum of the powers of the sets of cubes is {print_color(cube_sets_power_sum, Color.RED)}.')

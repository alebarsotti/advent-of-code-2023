import re
import uuid
import numpy
from Utils.Color import print_color, Color

NUMBER_PATTERN = re.compile(r'(\d+)')
GEAR_PATTERN = re.compile(r'[*]')

row_count = 0
col_count = 0
gear_ratio = 0


def find_parts(lines):
    part_numbers = {}
    for row_index, line in enumerate(lines):
        matches = NUMBER_PATTERN.finditer(line)
        for match in matches:
            part_numbers[f'{uuid.uuid4().hex}-{match.group()}'] = [(row_index, col_index) for col_index in
                                                                   range(match.start(), match.end())]
    return part_numbers


def find_gears(lines):
    part_numbers = {}
    for row_index, line in enumerate(lines):
        matches = GEAR_PATTERN.finditer(line)
        for match in matches:
            part_numbers[f'{uuid.uuid4().hex}-{match.group()}'] = [(row_index, col_index) for col_index in
                                                                   range(match.start(), match.end())]
    return part_numbers


def is_valid_coordinate(coord):
    x, y = coord

    return 0 <= x < row_count and 0 <= y < col_count


def get_adjacent_coordinates(coord):
    x, y = coord
    adjacent_coordinates = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ]
    valid_adjacent_coordinates = [coord for coord in adjacent_coordinates if is_valid_coordinate(coord)]

    return valid_adjacent_coordinates


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        valid_parts_sum = 0
        file_lines = file.readlines()
        row_count = len(file_lines)
        col_count = len(file_lines[0].strip())
        parts = find_parts(file_lines)
        gears = find_gears(file_lines)
        for gear in gears.keys():
            for gear_coord in gears[gear]:
                adjacent_coords = get_adjacent_coordinates(gear_coord)
                valid_part = []
                for part in parts.keys():
                    part_number = int(part.split("-")[1])
                    for part_coord in parts[part]:
                        if part_coord in adjacent_coords and part_number not in valid_part:
                            valid_part.append(part_number)
                if len(valid_part) == 2:
                    gear_ratio += numpy.prod(valid_part)
                    break
    print(f'The sum of all the gear ratios is {print_color(gear_ratio, Color.ORANGE)}.')

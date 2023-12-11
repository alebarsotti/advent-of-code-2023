import re
import uuid
from Utils.Color import print_color, Color

NUMBER_PATTERN = re.compile(r'(\d+)')
SYMBOL_PATTERN = re.compile(r'[^0-9.]')

row_count = 0
col_count = 0


def find_parts(lines):
    part_numbers = {}
    for row_index, line in enumerate(lines):
        matches = NUMBER_PATTERN.finditer(line)
        for match in matches:
            part_numbers[f'{uuid.uuid4().hex}-{match.group()}'] = [(row_index, col_index) for col_index in range(match.start(), match.end())]
    return part_numbers


def is_valid_coordinate(coord):
    x, y = coord

    return 0 <= x < row_count and 0 <= y < col_count


def get_adjacent_coordinates(coord):
    x, y = coord
    adjacent_coordinates = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y),                 (x + 1, y),
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
        for part in parts.keys():
            is_valid_part = False
            for part_coord in parts[part]:
                adjacent_coords = get_adjacent_coordinates(part_coord)
                for adj in adjacent_coords:
                    if SYMBOL_PATTERN.match(file_lines[adj[0]][adj[1]]):
                        is_valid_part = True
                        break
                if is_valid_part:
                    break
            if is_valid_part:
                valid_parts_sum += int(part.split('-')[1])
    print(f'The sum of the valid part numbers is {print_color(valid_parts_sum, Color.ORANGE)}.')


import re

from Utils.Color import print_color, Color

DIGITS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

PATTERN = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)', re.IGNORECASE)

calibration_sum = 0


def convert_to_digit(match):
    # Convert word to lowercase to handle case-insensitivity
    match_lower = match.lower()

    # # Use the dictionary to convert words to digits if needed
    return DIGITS[match_lower] if match_lower in DIGITS else match


with open('input.txt', 'r') as file:
    for line in file:
        line_digits = []
        for index in range(len(line)):
            match = PATTERN.match(line, index)
            if match:
                line_digits.append(match.group())

        calibration_value = convert_to_digit(line_digits[0]) + convert_to_digit(line_digits[-1])
        calibration_sum += int(calibration_value)

print(f'The sum of the calibration values of each line is {print_color(calibration_sum, Color.GREEN)}.')

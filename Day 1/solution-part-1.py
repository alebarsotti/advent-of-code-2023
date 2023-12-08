from Utils.Color import print_color, Color

calibration_sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        line_digits = [char for char in line if char.isdigit()]
        calibration_value = line_digits[0] + line_digits[-1]
        calibration_sum += int(calibration_value)

print(f'The sum of the calibration values of each line is {print_color(calibration_sum, Color.GREEN)}.')

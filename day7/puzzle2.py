def calculate_fuel_needed_to_position(target_position):
    fuel = 0
    for starting_position, number_of_subs in enumerate(number_of_positions):
        fuel_for_each_sub = sum(range(1, abs(starting_position - target_position) + 1))
        fuel += (fuel_for_each_sub * number_of_subs)
    return fuel


with open("input.txt") as f:
    puzzle_input = [int(val) for val in f.read().split(",")]

highest_position = max(puzzle_input)
number_of_positions = [0] * (highest_position + 1)
optimal_position = None
fuel_on_optimal_position = None

for position in puzzle_input:
    number_of_positions[position] += 1

for target_position in range(highest_position + 1):
    fuel_for_target_position = calculate_fuel_needed_to_position(target_position)
    if fuel_on_optimal_position is None or fuel_for_target_position < fuel_on_optimal_position:
        fuel_on_optimal_position = fuel_for_target_position
        optimal_position = target_position

print(fuel_on_optimal_position)

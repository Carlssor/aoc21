def find_value(numbers, type_of_reading):
    for bit_position in range(len(numbers[0])):
        if len(numbers) == 1:
            break
        values_with_ones = list(filter(lambda val: val[bit_position] == "1", numbers))
        values_with_zeros = list(filter(lambda val: val[bit_position] == "0", numbers))
        if type_of_reading == "oxygen":
            if len(values_with_ones) >= len(values_with_zeros):
                numbers = values_with_ones[:]
            else:
                numbers = values_with_zeros[:]
        elif type_of_reading == "co2":
            if len(values_with_zeros) <= len(values_with_ones):
                numbers = values_with_zeros[:]
            else:
                numbers = values_with_ones[:]
    if len(numbers) != 1:
        raise ValueError(f"{len(numbers)} items remaining, expected 1")
    return int(numbers[0], 2)


with open("input.txt") as f:
    puzzle_input = f.read().split()
oxygen_generator_rating = find_value(puzzle_input, "oxygen")
co2_scrubber_rating = find_value(puzzle_input, "co2")

print(oxygen_generator_rating * co2_scrubber_rating)

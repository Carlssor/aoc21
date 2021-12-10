with open("input.txt") as f:
    puzzle_input = f.read().split("\n")

number_of_digits = 0

for line in puzzle_input:
    output_values = line.split("|")[1].split()
    number_of_digits += sum([1 if (len(digit) in (2, 3, 4, 7)) else 0 for digit in output_values])

print(number_of_digits)

with open("input.txt") as f:
    puzzle_input = [int(val) for val in f.readlines()]

increases = 0

for index in range(1, len(puzzle_input)):
    if puzzle_input[index] > puzzle_input[index - 1]:
        increases += 1

print(increases)

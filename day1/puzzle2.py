with open("input.txt") as f:
    puzzle_input = [int(val) for val in f.readlines()]

sums = [sum(puzzle_input[index - 3: index]) for index in range(3, len(puzzle_input) + 1)]
increases = 0

for index in range(1, len(sums)):
    if sums[index] > sums[index - 1]:
        increases += 1

print(increases)

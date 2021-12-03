with open("input.txt") as f:
    puzzle_input = f.read().split()

gamma_rate = 0
epsilon_rate = 0

for index, values in enumerate(reversed(list(zip(*puzzle_input)))):
    if values.count("1") > values.count("0"):
        gamma_rate += (1 << index)
    else:
        epsilon_rate += (1 << index)

print(gamma_rate * epsilon_rate)

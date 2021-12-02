with open("input.txt") as f:
    puzzle_input = f.readlines()

horizontal_position = 0
depth = 0

for command in puzzle_input:
    direction, amount = command.split()
    amount = int(amount)
    if direction == "forward":
        horizontal_position += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount
    else:
        raise ValueError(f"Direction {direction} not supported")

print(horizontal_position * depth)

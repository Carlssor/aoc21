with open("input.txt") as f:
    puzzle_input = f.read()

lines = puzzle_input.split("\n")
vent_positions = [[0]]

for line in lines:
    x1, y1, x2, y2 = [int(pos) for pos in ",".join(line.split(" -> ")).split(",")]
    number_of_rows = len(vent_positions)
    number_of_cols = len(vent_positions[0])
    for _ in range(max(y1, y2) - number_of_rows + 1):
        vent_positions.append([0] * number_of_cols)
    for _ in range(max(x1, x2) - number_of_cols + 1):
        for row in vent_positions:
            row.append(0)

    if x1 <= x2:
        x_pos = list(range(x1, x2 + 1))
    else:
        x_pos = list(range(x1, x2 - 1, -1))
    if y1 <= y2:
        y_pos = list(range(y1, y2 + 1))
    else:
        y_pos = list(range(y1, y2 - 1, -1))
    if x1 == x2:
        x_pos *= len(y_pos)
    if y1 == y2:
        y_pos *= len(x_pos)
    for x, y in zip(x_pos, y_pos):
        vent_positions[y][x] += 1

overlapping = 0
for row in vent_positions:
    overlapping += len([num for num in row if num >= 2])

print(overlapping)

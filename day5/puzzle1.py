with open("input.txt") as f:
    puzzle_input = f.read()

lines = puzzle_input.split("\n")
vent_positions = [[0]]

for line in lines:
    x1, y1, x2, y2 = [int(pos) for pos in ",".join(line.split(" -> ")).split(",")]
    x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
    y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)
    number_of_rows = len(vent_positions)
    number_of_cols = len(vent_positions[0])
    for _ in range(y2 - number_of_rows + 1):
        vent_positions.append([0] * number_of_cols)
    for _ in range(x2 - number_of_cols + 1):
        for row in vent_positions:
            row.append(0)

    if x1 == x2 or y1 == y2:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                vent_positions[y][x] += 1

overlapping = 0
for row in vent_positions:
    overlapping += len([num for num in row if num >= 2])

print(overlapping)

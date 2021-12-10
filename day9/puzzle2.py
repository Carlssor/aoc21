import functools


with open("input.txt") as f:
    puzzle_input = f.read().split("\n")


def calculate_basin_size(start_row, start_col):
    size = 1

    start_height = heights[start_row][start_col]
    heights[start_row][start_col] = -1
    if start_height == 9:
        return 0

    up_height = heights[start_row - 1][start_col] if start_row > 0 else -1
    if up_height > start_height:
        size += calculate_basin_size(start_row - 1, start_col)

    down_height = heights[start_row + 1][start_col] if start_row < rows - 1 else -1
    if down_height > start_height:
        size += calculate_basin_size(start_row + 1, start_col)

    left_height = heights[start_row][start_col - 1] if start_col > 0 else -1
    if left_height > start_height:
        size += calculate_basin_size(start_row, start_col - 1)

    right_height = heights[start_row][start_col + 1] if start_col < cols - 1 else -1
    if right_height > start_height:
        size += calculate_basin_size(start_row, start_col + 1)

    return size


heights = []

for line in puzzle_input:
    heights.append([int(val) for val in line])

rows = len(heights)
cols = len(heights[0])
basin_sizes = []

for row in range(rows):
    for col in range(cols):
        height = heights[row][col]
        if row > 0 and height >= heights[row - 1][col]:
            continue
        elif row + 1 < rows and height >= heights[row + 1][col]:
            continue
        elif col > 0 and height >= heights[row][col - 1]:
            continue
        elif col + 1 < cols and height >= heights[row][col + 1]:
            continue

        basin_sizes.append(calculate_basin_size(row, col))

print(functools.reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:]))

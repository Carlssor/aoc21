with open("input.txt") as f:
    puzzle_input = f.read().split("\n")

heights = []

for line in puzzle_input:
    heights.append([int(val) for val in line])

rows = len(heights)
cols = len(heights[0])
risk_level = 0

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
        risk_level += heights[row][col] + 1

print(risk_level)

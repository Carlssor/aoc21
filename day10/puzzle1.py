with open("input.txt") as f:
    puzzle_input = f.read().split("\n")

opening_delimiters_found = []
delimiter_openers = "([{<"
delimiter_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
illegal_delimiter_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
points = 0

for line in puzzle_input:
    for delimiter in line:
        if delimiter in delimiter_openers:
            opening_delimiters_found.append(delimiter)
        elif delimiter == delimiter_pairs.get(opening_delimiters_found[-1], None):
            opening_delimiters_found.pop(-1)
        else:
            points += illegal_delimiter_points[delimiter]
            break

print(points)

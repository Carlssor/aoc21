with open("input.txt") as f:
    puzzle_input = f.read().split("\n")

delimiter_openers = "([{<"
delimiter_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
missing_delimiter_points = {")": 1, "]": 2, "}": 3, ">": 4}
points = []


def calculate_missing_delimiter_closers(line):
    opening_delimiters_found = []
    for delimiter in line:
        if delimiter in delimiter_openers:
            opening_delimiters_found.append(delimiter)
        elif delimiter == delimiter_pairs.get(opening_delimiters_found[-1], None):
            opening_delimiters_found.pop(-1)
        else:
            return None
    return [delimiter_pairs[delimiter] for delimiter in reversed(opening_delimiters_found)]


for line in puzzle_input:
    missing_delimiter_closers = calculate_missing_delimiter_closers(line)
    if missing_delimiter_closers is None:
        continue

    current_points = 0
    for delimiter in missing_delimiter_closers:
        current_points = current_points * 5 + missing_delimiter_points[delimiter]
    points.append(current_points)

print(sorted(points)[len(points) // 2])

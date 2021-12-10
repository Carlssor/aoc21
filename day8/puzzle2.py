with open("input.txt") as f:
    puzzle_input = f.read().split("\n")


def get_number_candidates_by_length(signal_patterns, length):
    return list(filter(lambda pattern: len(pattern) == length, signal_patterns))


def get_number_candidates_by_containing(signal_patterns, letters_to_contain):
    return list(filter(lambda pattern: set(letters_to_contain).issubset(set(pattern)), signal_patterns))


def get_number_candidates_by_not_containing(signal_patterns, letters_to_not_contain):
    containing_candidates = get_number_candidates_by_containing(signal_patterns, letters_to_not_contain)
    return list(set(signal_patterns) - set(containing_candidates))


def to_sorted_string(input_string):
    return "".join(sorted(list(input_string)))


def determine_numbers(signal_patterns):
    signal_patterns = signal_patterns.split()
    digit_to_pattern = dict()

    digit_to_pattern[1] = get_number_candidates_by_length(signal_patterns, 2)[0]
    digit_to_pattern[4] = get_number_candidates_by_length(signal_patterns, 4)[0]
    digit_to_pattern[7] = get_number_candidates_by_length(signal_patterns, 3)[0]
    digit_to_pattern[8] = get_number_candidates_by_length(signal_patterns, 7)[0]
    five_segment_patterns = get_number_candidates_by_length(signal_patterns, 5)
    six_segment_patterns = get_number_candidates_by_length(signal_patterns, 6)
    digit_to_pattern[3] = get_number_candidates_by_containing(five_segment_patterns, digit_to_pattern[1])[0]
    digit_to_pattern[9] = get_number_candidates_by_containing(six_segment_patterns, digit_to_pattern[4])[0]
    e_segment_wire = list(set(digit_to_pattern[8]) - set(digit_to_pattern[9]))[0]
    digit_to_pattern[5] = get_number_candidates_by_not_containing(
        get_number_candidates_by_not_containing(five_segment_patterns, digit_to_pattern[3]),
        e_segment_wire)[0]
    digit_to_pattern[2] = get_number_candidates_by_not_containing(
        get_number_candidates_by_not_containing(five_segment_patterns, digit_to_pattern[3]),
        digit_to_pattern[5]
    )[0]
    digit_to_pattern[0] = get_number_candidates_by_containing(
        get_number_candidates_by_not_containing(six_segment_patterns, digit_to_pattern[5]),
        digit_to_pattern[1]
    )[0]
    digit_to_pattern[6] = get_number_candidates_by_not_containing(six_segment_patterns, digit_to_pattern[1])[0]

    return dict((to_sorted_string(v), k) for k, v in digit_to_pattern.items())


result = 0
for input_row in puzzle_input:
    signal_patterns, digits = input_row.split("|")
    pattern_to_digit = determine_numbers(signal_patterns)
    pattern_result = ""
    for pattern in digits.split():
        pattern_result += str(pattern_to_digit[to_sorted_string(pattern)])
    result += int(pattern_result)

print(result)

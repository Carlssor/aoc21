with open("input.txt") as f:
    puzzle_input = [int(val) for val in f.read().split(",")]

number_of_fish_on_timer_value = []
days = 256

for timer_value in range(9):
    number_of_fish_on_timer_value.append(puzzle_input.count(timer_value))

for day in range(days):
    number_of_fish_on_timer_value.append(number_of_fish_on_timer_value[0])
    number_of_fish_on_timer_value.pop(0)
    number_of_fish_on_timer_value[6] += number_of_fish_on_timer_value[-1]

print(sum(number_of_fish_on_timer_value))

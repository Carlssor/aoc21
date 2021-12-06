with open("input.txt") as f:
    puzzle_input = f.read()

lanternfish_timers = [int(val) for val in puzzle_input.split(",")]
days = 80

for _ in range(days):
    for index in range(len(lanternfish_timers)):
        lanternfish_timers[index] -= 1
        if lanternfish_timers[index] < 0:
            lanternfish_timers[index] = 6
            lanternfish_timers.append(8)

print(len(lanternfish_timers))

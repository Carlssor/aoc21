from util import get_list_of_octopuses

octopuses = get_list_of_octopuses()

for _ in range(100):
    for octopus in octopuses:
        octopus.increase_energy()
    for octopus in octopuses:
        octopus.finish_step()

total_flashes = 0
for octopus in octopuses:
    total_flashes += octopus.get_flashes()

print(total_flashes)

from util import get_list_of_octopuses

octopuses = get_list_of_octopuses()
all_flash_on_step = 0

while True:
    all_flash_on_step += 1
    if all_flash_on_step > 1000000:
        raise ValueError("Does this puzzle have a solution?")
    for octopus in octopuses:
        octopus.increase_energy()
    if all([octopus.have_flashed() for octopus in octopuses]):
        break
    for octopus in octopuses:
        octopus.finish_step()

print(all_flash_on_step)

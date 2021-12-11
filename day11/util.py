from dumbo_octopus import DumboOctopus


def get_list_of_octopuses():
    with open("input.txt") as f:
        puzzle_input = f.read().split("\n")

    octopuses_grid = []

    for line in puzzle_input:
        octopuses_grid.append([DumboOctopus(int(energy)) for energy in line])

    octopus_rows = len(octopuses_grid)
    octopus_cols = len(octopuses_grid[0])

    for row in range(octopus_rows):
        for col in range(octopus_cols):
            current_octopus = octopuses_grid[row][col]
            if row > 0:
                current_octopus.add_adjacent_octopus(octopuses_grid[row - 1][col])
            if row > 0 and col < octopus_cols - 1:
                current_octopus.add_adjacent_octopus(octopuses_grid[row - 1][col + 1])
            if col < octopus_cols - 1:
                current_octopus.add_adjacent_octopus(octopuses_grid[row][col + 1])
            if col < octopus_cols - 1 and row < octopus_rows - 1:
                current_octopus.add_adjacent_octopus(octopuses_grid[row + 1][col + 1])
            if row < octopus_rows - 1:
                current_octopus.add_adjacent_octopus(octopuses_grid[row + 1][col])
            if row < octopus_rows - 1 and col > 0:
                current_octopus.add_adjacent_octopus(octopuses_grid[row + 1][col - 1])
            if col > 0:
                current_octopus.add_adjacent_octopus(octopuses_grid[row][col - 1])
            if col > 0 and row > 0:
                current_octopus.add_adjacent_octopus(octopuses_grid[row - 1][col - 1])

    return [octopus for octopus_row in octopuses_grid for octopus in octopus_row]

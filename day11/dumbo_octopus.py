class DumboOctopus:
    def __init__(self, initial_energy):
        self._energy = initial_energy
        self._have_flashed_this_step = False
        self._number_flashes = 0
        self._adjacent_octopuses = []

    def __str__(self):
        return f"{self._energy} ({'X' if self._have_flashed_this_step else '-'})"

    __repr__ = __str__

    def add_adjacent_octopus(self, adjacent_octopus):
        self._adjacent_octopuses.append(adjacent_octopus)

    def increase_energy(self):
        if self._have_flashed_this_step:
            return

        self._energy += 1
        if self._energy >= 10:
            self._have_flashed_this_step = True
            self._number_flashes += 1
            for octopus in self._adjacent_octopuses:
                octopus.increase_energy()

    def finish_step(self):
        if self._have_flashed_this_step:
            self._energy = 0
            self._have_flashed_this_step = False

    def get_flashes(self):
        return self._number_flashes

    def have_flashed(self):
        return self._have_flashed_this_step

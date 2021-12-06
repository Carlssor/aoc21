class Board:
    def __init__(self, number_input):
        self._bingo_numbers_rows = []
        for row in number_input.split("\n"):
            self._bingo_numbers_rows.append([BingoNumber(int(number)) for number in row.split()])
        self._bingo_numbers_cols = list(zip(*self._bingo_numbers_rows))

    def pick_number(self, number):
        for bingo_row in self._bingo_numbers_rows:
            for bingo_number in bingo_row:
                if bingo_number == number:
                    bingo_number.pick()

    def check_if_board_has_won(self):
        for row_column in range(5):
            if all([number.get_picked() for number in self._bingo_numbers_rows[row_column]]):
                return True
            if all([number.get_picked() for number in self._bingo_numbers_cols[row_column]]):
                return True
        return False

    def get_unpicked_numbers(self):
        for bingo_row in self._bingo_numbers_rows:
            for bingo_number in bingo_row:
                if not bingo_number.get_picked():
                    yield bingo_number.get_value()


class BingoNumber:
    def __init__(self, value):
        self._value = value
        self._picked = False

    def __eq__(self, other):
        return self._value == other

    def __repr__(self):
        return f"{self._value} ({'' if self._picked else 'un'}picked)"

    def get_value(self):
        return self._value

    def pick(self):
        self._picked = True

    def get_picked(self):
        return self._picked

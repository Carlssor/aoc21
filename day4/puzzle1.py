from bingo import Board


def play_until_win():
    for picked_number in picked_numbers:
        for board in boards:
            board.pick_number(picked_number)
            if board.check_if_board_has_won():
                return picked_number, board

    raise RuntimeError("No winning board found")


with open("input.txt") as f:
    puzzle_input = f.read().split("\n\n")

picked_numbers = [int(number) for number in puzzle_input[0].split(",")]
boards = [Board(board_input) for board_input in puzzle_input[1:]]

last_number, winning_board = play_until_win()
print(last_number * sum(list(winning_board.get_unpicked_numbers())))

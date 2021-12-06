from bingo import Board


def play_until_one_remaining():
    boards_still_playing = len(boards)
    board_indices_won = []
    for picked_number in picked_numbers:
        for board_index, board in enumerate(boards):
            if board_index in board_indices_won:
                continue
            board.pick_number(picked_number)
            if board.check_if_board_has_won():
                board_indices_won.append(board_index)
                boards_still_playing -= 1
            if boards_still_playing == 0:
                return picked_number, board

    raise RuntimeError("No winning board found")


with open("input.txt") as f:
    puzzle_input = f.read().split("\n\n")

picked_numbers = [int(number) for number in puzzle_input[0].split(",")]
boards = [Board(board_input) for board_input in puzzle_input[1:]]

last_number, last_winning_board = play_until_one_remaining()
print(last_number * sum(list(last_winning_board.get_unpicked_numbers())))

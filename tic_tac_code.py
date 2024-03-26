def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings


def row_winner(board):
    for row in board:
        all_equal = True
        first_char = row[0]
        for char in row:
            if first_char == " " or char != first_char:
                all_equal = False
                break
        if all_equal:
            return True
    return False


def column_winner(board):
    for i in range(len(board[0])):
        all_equal = True
        first_char = board[0][i]
        for row in board:
            if row[i] == " " or row[i] != first_char:
                all_equal = False
                break
        if all_equal:
            return True
    return False


def diagonal_winner(board):
    all_equal1 = True
    all_equal2 = True
    first_char = board[0][0]
    topleft = board[0][0]
    topright = board[0][-1]
    for i in range(len(board)):
        if board[i][i] == " " or board[i][i] != topleft:
            all_equal1 = False
        if board[i][-i - 1] == " " or board[i][-i - 1] != topright:
            all_equal2 = False
    return all_equal1 or all_equal2


def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)


def format_board(board):
    first_row = " "
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + "".join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)


def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    column = int(input()) - 1
    board[row][column] = player
    print(format_board(board))


def make_board(size):
    return [[' '] * size for _ in range(size)]


def print_winner(player):
    print(f'{player} wins!')


def print_draw():
    print("It's a draw!")


def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))

    player = player1
    for _ in range(board_size * board_size):
        play_move(board, player)

        if winner(board):
            print_winner(player)
            return

        if player == player1:
            player = player2
        else:
            player = player1

    print_draw()


play_game(3, 'X', 'O')
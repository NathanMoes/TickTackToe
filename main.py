tick_tack_toe_board = [
    '  ', '|', '  ', ' |', '  \n'
    '- ', '*', ' - ', '*', ' -\n',
    '  ', '|', '  ', ' |', '  \n',
    '- ', '*', ' - ', '*', ' -\n',
    '  ', '|', '  ', ' |', '  \n'
]
tick_tack_toe = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]


def printBoard(old_board, score_board_l):
    new_board = []
    count = 0
    to_print = ''
    if score_board_l[0] == 0:
        new_board.append('  ')
    elif score_board_l[0] == 1:
        new_board.append(' x')
    elif score_board_l[0] == -1:
        new_board.append(' o')
    new_board.append('|')
    if score_board_l[1] == 0:
        new_board.append('  ')
    elif score_board_l[1] == 1:
        new_board.append(' x')
    elif score_board_l[1] == -1:
        new_board.append(' o')
    new_board.append(' |')
    if score_board_l[2] == 0:
        new_board.append('  \n')
    elif score_board_l[2] == 1:
        new_board.append(' x\n')
    elif score_board_l[2] == -1:
        new_board.append(' o\n')
    new_board.append('- ')
    new_board.append('*')
    new_board.append(' - ')
    new_board.append('*')
    new_board.append(' -\n')
    if score_board_l[3] == 0:
        new_board.append('  ')
    elif score_board_l[3] == 1:
        new_board.append(' x')
    elif score_board_l[3] == -1:
        new_board.append(' o')
    new_board.append('|')
    if score_board_l[4] == 0:
        new_board.append('  ')
    elif score_board_l[4] == 1:
        new_board.append(' x')
    elif score_board_l[4] == -1:
        new_board.append(' o')
    new_board.append(' |')
    if score_board_l[5] == 0:
        new_board.append('  \n')
    elif score_board_l[5] == 1:
        new_board.append(' x\n')
    elif score_board_l[5] == -1:
        new_board.append(' o\n')
    new_board.append('- ')
    new_board.append('*')
    new_board.append(' - ')
    new_board.append('*')
    new_board.append(' -\n')
    if score_board_l[6] == 0:
        new_board.append('  ')
    elif score_board_l[6] == 1:
        new_board.append(' x')
    elif score_board_l[6] == -1:
        new_board.append(' o')
    new_board.append('|')
    if score_board_l[7] == 0:
        new_board.append('  ')
    elif score_board_l[7] == 1:
        new_board.append(' x')
    elif score_board_l[7] == -1:
        new_board.append(' o')
    new_board.append(' |')
    if score_board_l[8] == 0:
        new_board.append('  \n')
    elif score_board_l[8] == 1:
        new_board.append(' x\n')
    elif score_board_l[8] == -1:
        new_board.append(' o\n')
    for char_in in new_board:
        to_print += char_in
    print(to_print)
    return new_board


def update_board(position, mark, board_l):
    new_board = board_l
    if mark == 'x':
        new_board[int(position)] = 1
    else:
        new_board[int(position)] = -1
    return new_board


def win_condition_check(score_board):
    # length wise wins
    cond1 = score_board[0] + score_board[1] + score_board[2]
    if cond1 == -3:
        print('o wins')
        return True
    elif cond1 == 3:
        print('x wins')
        return True
    cond2 = score_board[3] + score_board[4] + score_board[5]
    if cond2 == -3:
        print('o wins')
        return True
    elif cond2 == 3:
        print('x wins')
        return True
    cond3 = score_board[6] + score_board[7] + score_board[8]
    if cond3 == -3:
        print('o wins')
        return True
    elif cond3 == 3:
        print('x wins')
        return True
    # column wise wins
    cond4 = score_board[0] + score_board[3] + score_board[6]
    if cond4 == -3:
        print('o wins')
        return True
    elif cond4 == 3:
        print('x wins')
        return True
    cond5 = score_board[1] + score_board[4] + score_board[7]
    if cond5 == -3:
        print('o wins')
        return True
    elif cond5 == 3:
        print('x wins')
        return True
    cond6 = score_board[2] + score_board[5] + score_board[8]
    if cond6 == -3:
        print('o wins')
        return True
    elif cond6 == 3:
        print('x wins')
        return True
    # diagonal wins
    cond7 = score_board[0] + score_board[4] + score_board[8]
    if cond7 == -3:
        print('o wins')
        return True
    elif cond7 == 3:
        print('x wins')
        return True
    cond8 = score_board[2] + score_board[4] + score_board[6]
    if cond8 == -3:
        print('o wins')
        return True
    elif cond8 == 3:
        print('x wins')
        return True


def valid_mark(posn, score_board_l):
    if score_board_l[int(posn)] != 0:
        return True
    return False


if __name__ == '__main__':
    print("input to the game is via text. The value 0 responds to the first blank in between the lines"
          "and 8 being the last")
    begin_score = tick_tack_toe
    begin_board = tick_tack_toe_board
    board = printBoard(begin_board, begin_score)
    score_board = begin_score
    while not win_condition_check(begin_score):
        test = input('enter input for x\n')
        while valid_mark(test, score_board):
            test = input('enter input for x\n')
        score_board = update_board(test, 'x', begin_score)
        printBoard(board, score_board)
        if win_condition_check(begin_score):
            break
        test = input('enter input for o\n')
        while valid_mark(test, score_board):
            test = input('enter input for o\n')
        score_board = update_board(test, 'o', begin_score)
        printBoard(board, score_board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

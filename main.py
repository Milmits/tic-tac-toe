# Код написан 09.11.2023
# Автор: Кучук Милан Михайлович
print("\t\tПрограмма Кучук")
print("\t\tКрестики нолики")

X = "X"
O = "0"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def display_instruct():
    """Выводит на экран инструкцию для игрока"""
    print(
        """
        Добро пожаловать на ринг
        Чтобы сделать ход введи число от 0 до 8
        0 ! 1 ! 2 
        ---------
        3 ! 4 ! 5
        ---------
        6 ! 7 ! 8
        """
    )


def ask_yes_no(question):
    """"
    Выводит на экран вопрос с ответом да или нет
    """
    otvet = None
    while otvet not in ("y", "n"):
        otvet = input(question)
    return otvet


def ask_number(question, low, hight):
    """
    просит ввести число из диапозона
    """
    otvet = None
    while otvet not in range(low, hight):
        otvet = input(question)
    return otvet


def pieces():
    """
    Определяет превый ход
    """
    go_first = ask_yes_no("Хочешь ходить первым? (y/n)")
    if go_first == "y":
        human = X
        computer = O
    else:
        human = O
        computer = X


def new_board():
    """
    создает новую игровую доску
    """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Отображает игровую доску на экране
    """
    print("\n", board[0], "!", board[1], "!", board[2])
    print("\n", "---------")
    print("\n", board[3], "!", board[4], "!", board[5])
    print("\n", "---------")
    print("\n", board[6], "!", board[7], "!", board[8])


def legal_moves():
    """
    Создает список доступных ходов
    """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner():
    """
    Опредляет победителя в игре
    """
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8,),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        elif EMPTY not in board:
            return TIE
        return None


def human_move(board, human):
    """
    Получает ход человека
    """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход, выбери одно из полей(0-8): ", NUM_SQUARES)
        if move not in legal:
            print("Это поле уже занято")
    print("Ладно")
    return move


def computer_move(board, computer, human):
    """
    Делает ход за компьютер
    """
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] == human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)


def next_turn(turn):
    """
    Осуществляет переход хода
    """
    if turn == X:
        return 0
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """
    Поздравляет победителя игры
    """
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!")
    else:
        print("Ничья!")
    if the_winner == computer:
        print("ПОбедил комп")
    elif the_winner == human:
        print("ПОбедил человек")
    elif the_winner == TIE:
        print("Ничья!!!")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
        else:
            move = computer_move(board, computer, human)
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()

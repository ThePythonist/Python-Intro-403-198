def main():
    end = False
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def table():
        print('''
                 {} | {} | {}
                -----------
                 {} | {} | {}
                -----------
                 {} | {} | {}
                '''.format(
            board[0],
            board[1],
            board[2],
            board[3],
            board[4],
            board[5],
            board[6],
            board[7],
            board[8],
        ))

    def choice1():
        return int(input("Choose : "))

    def choice2():
        return int(input("Choose : "))

    def move1():
        n = choice1()

    def move2():
        n = choice2()

    def check_board():
        pass

    while not end:
        table()

main()
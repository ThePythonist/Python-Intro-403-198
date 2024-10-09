from tkinter import ttk, messagebox


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
        while True:
            place = input("Player 1 Choice : ")
            try:
                place = int(place)
                place = place - 1

                if place in range(0, 9):
                    if board[place] in ["X", "Y"]:
                        # print("You can't go there. Try again")
                        messagebox.showerror("Invalid Entry", "You can't go there. Try again")
                    else:
                        return place
            except ValueError:
                # print("Entry must be a number. Try again")
                messagebox.showerror("Invalid Entry", "Entry must be a number. Try again")

    def choice2():
        while True:
            place = input("Player 2 Choice : ")
            try:
                place = int(place)
                place = place - 1

                if place in range(0, 9):
                    if board[place] in ["X", "Y"]:
                        # print("You can't go there. Try again")
                        messagebox.showerror("Invalid Entry", "You can't go there. Try again")
                    else:
                        return place
            except ValueError:
                # print("Entry must be a number. Try again")
                messagebox.showerror("Invalid Entry", "Entry must be a number. Try again")

    def move1():
        choice = choice1()
        board[choice] = "X"

    def move2():
        choice = choice2()
        board[choice] = "Y"

    def check_board():
        count = 0

        for i in win_combinations:
            if board[i[0]] == board[i[1]] == board[i[2]] == "X":
                # print("Player 1 Wins!")
                messagebox.showinfo("End", "Player 1 Wins!")
                return True
            elif board[i[0]] == board[i[1]] == board[i[2]] == "Y":
                # print("Player 2 Wins!")
                messagebox.showinfo("End", "Player 2 Wins!")
                return True

        for i in board:
            if i in ["X", "Y"]:
                count += 1

        if count == 9:
            # print("The game ends level")
            messagebox.showwarning("End", "The game ends level")
            return True

    while not end:
        table()
        end = check_board()

        if end:
            break

        move1()
        table()
        end = check_board()

        if end:
            break

        move2()
        table()

    if input("Play again ? (y/n) : ").lower() == "y":
        main()


main()

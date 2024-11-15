from tkinter import *
from tkinter import messagebox

class TicTacToe:
    def _init_(self):
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(0, 0)

        self.player = 'X'
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.game_over = False

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = Button(self.root, height=4, width=8, font=("Helvetica", 20), command=lambda r=i, c=j: self.click(r, c))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.root.mainloop()

    def click(self, row, col):
        if not self.game_over and self.board[row][col] == 0:
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)

            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.player} wins!")
                self.game_over = True
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.game_over = True
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return True

        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True

if __name__ == "_main_":
    game = TicTacToe()
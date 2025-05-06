# Depth First Search Word Search Solver

import tkinter as tk
from tkinter import messagebox
import copy

# Word Serach Logic
def exist(board, word):
    indices = []

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '#' or board[r][c] != word[i]:
            return False

        temp, board[r][c] = board[r][c], '#'
        indices.append((r, c))

        if (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)):
            board[r][c] = temp
            return True

        board[r][c] = temp
        indices.pop()
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True, indices.copy()

    return False, []

def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            row = [char for char in line.strip() if char != ' ' and char != ',']
            if row:
                board.append(row)
    return board

# Simple GUI
class WordSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Search Solver")
        self.board = []
        self.labels = []

        # Frame for board grid
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=10)

        # Dropdown to select board size
        self.size_var = tk.StringVar()
        self.size_var.set("Select Board Size")
        self.size_menu = tk.OptionMenu(self.root, self.size_var, "small", "medium", "large", command=self.load_predefined_board)
        self.size_menu.pack(pady=5)

        # Entry for word input
        self.entry = tk.Entry(self.root, font=('Arial', 14))
        self.entry.pack(pady=5)

        # Button to search
        self.submit_btn = tk.Button(self.root, text="Search Word", command=self.search_word)
        self.submit_btn.pack(pady=5)

    def draw_board(self, path=None):
        path = set(path or [])
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.labels = []
        for i, row in enumerate(self.board):
            label_row = []
            for j, char in enumerate(row):
                color = "yellow" if (i, j) in path else "lightblue"
                lbl = tk.Label(self.board_frame, text=char, width=2, height=1,
                               font=('Arial', 16), bg=color, relief='solid', bd=1)
                lbl.grid(row=i, column=j, padx=1, pady=1)
                label_row.append(lbl)
            self.labels.append(label_row)

    def load_predefined_board(self, size):
        file_path = f"./boards/{size}_board.txt"
        try:
            self.board = read_board_from_file(file_path)
            self.original_board = copy.deepcopy(self.board)
            self.draw_board()
        except FileNotFoundError:
            messagebox.showerror("File Error", f"{file_path} not found.")

    def search_word(self):
        word = self.entry.get().upper()
        if not word:
            messagebox.showwarning("Input Error", "Please enter a word.")
            return
        self.board = copy.deepcopy(self.original_board)
        found, path = exist(self.board, word)
        if found:
            self.draw_board(path)
            messagebox.showinfo("Result", f"{word} is present in the board.")
        else:
            self.draw_board([])
            messagebox.showinfo("Result", f"{word} is not present in the board.")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = WordSearchApp(root)
    root.mainloop()

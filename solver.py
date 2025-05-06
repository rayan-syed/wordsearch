import copy
from colorama import Fore, Style, init

# Word Search Solver with Depth First Search 

def exist(board, word) -> bool:
    indices = []
    def dfs(r, c, i):
        if len(word) == i:
            return True
        if r<0 or c<0 or r>=len(board) or c >= len(board[0]) or board[r][c] == '#' or word[i] != board[r][c]:
            return False
        
        board[r][c] = '#' # mark as visited
        indices.append((r,c))
        success = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
        if success: return True
        indices.pop()
        board[r][c] = word [i] # restore character

    # dfs from all starting nodes
    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r,c,0): return True, indices
    return False, indices

def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            row = [char for char in line.strip() if char != ' ' and char != ',']
            if row:
                board.append(row)
    return board

init(autoreset=True)
def print_board(board, ind=None):
    if ind: highlight_set = set(ind)  # for faster lookup
    else: highlight_set = set()
    for i, row in enumerate(board):
        row_str = ""
        for j, char in enumerate(row):
            if (i, j) in highlight_set:
                row_str += Fore.YELLOW + char + Style.RESET_ALL + " "
            else:
                row_str += Fore.CYAN + char + Style.RESET_ALL + " "
        print(row_str)


if __name__ == "__main__":
    board_type = input("What size board? (small/medium/large): ")
    valid_types = ['small','medium','large']

    while board_type not in valid_types:
        board_type = input("Please input a valid size: (small/medium/large): ")

    board = read_board_from_file(f"./boards/{board_type}_board.txt")
    print("\nCurrent board:")
    print_board(board)

    while(1):
        board_copy= copy.deepcopy(board)
        word = input("\nEnter a word to find: ").upper()
        if word=="EXIT()":
            break
        found, ind = exist(board, word)
        board = board_copy
        if found:
            print(f"{word} is present in the board:")
            print_board(board, ind)
        else:
            print(f"{word} is not present in the board.")


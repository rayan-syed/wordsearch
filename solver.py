import copy

# Word Search Solver with Depth First Search 

def exist(board, word) -> bool:
    def dfs(r, c, i):
        if len(word) == i:
            return True
        if r<0 or c<0 or r>=len(board) or c >= len(board[0]) or board[r][c] == '#' or word[i] != board[r][c]:
            return False
        
        board[r][c] = '#' # mark as visited
        success = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
        if success: return True
        board[r][c] = word [i] # restore character

    # dfs from all starting nodes
    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r,c,0): return True
    return False

def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip()) 
            row = [char for char in line.strip() if char != ' ' and char != ',']
            if row:
                board.append(row)
    return board

if __name__ == "__main__":
    board_type = input("What size board? (small/medium/large): ")
    valid_types = ['small','medium','large']

    while board_type not in valid_types:
        board_type = input("Please input a valid size: (small/medium/large): ")

    board = read_board_from_file(f"./boards/{board_type}_board.txt")

    while(1):
        board_copy= copy.deepcopy(board)
        word = input("\nEnter a word to find: ").upper()
        if word=="EXIT()":
            break
        if exist(board, word):
            print(f"{word} is present in the board.")
        else:
            print(f"{word} is not present in the board.")
        board = board_copy


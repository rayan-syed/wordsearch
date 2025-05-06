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

if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    for row in board:
        print(row)

    while(1):
        board_copy= copy.deepcopy(board)
        word = input("Enter a word to find: ").upper()
        if exist(board, word):
            print(f"{word} is present in the board.")
        else:
            print(f"{word} is not present in the board.")
        board = board_copy


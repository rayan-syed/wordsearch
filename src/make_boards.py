import random
from pathlib import Path

def embed_word(board, word, start_r, start_c, direction):
    dr, dc = direction
    for i, ch in enumerate(word):
        r, c = start_r + i * dr, start_c + i * dc
        board[r][c] = ch
    return board


def generate_scrambled_board(size, word_list):
    board = [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
              for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for word in word_list:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            direction = random.choice(directions)
            max_r = size - (len(word) if direction[0] else 1)
            max_c = size - (len(word) if direction[1] else 1)
            start_r = random.randint(0, max_r)
            start_c = random.randint(0, max_c)

            # Check if word can be placed
            fits = True
            for i, ch in enumerate(word):
                r, c = start_r + i * direction[0], start_c + i * direction[1]
                if board[r][c] != ch and board[r][c] in word:
                    fits = False
                    break
            if fits:
                embed_word(board, word, start_r, start_c, direction)
                placed = True
            attempts += 1
    return board


def save_board(filename, board):
    with open(filename, "w") as f:
        for row in board:
            f.write(" ".join(row) + "\n")


# Define word lists for each board size
small_words = ["CATS", "DOG", "BIRD", "FISH"]
medium_words = ["TRACERS", "SUNLIGHT", "WINDS", "MOUNTAIN",
                "FLOWERS", "BUTTERFLY", "ALLIGATOR", "ELEPHANT"]
large_words = ["APPLE", "TREES", "CHAMELEONS", "BLUEBERRIES", "STRAWBERRY", "DANDELIONS", "GRASSHOPPER",
               "LIGHTHOUSE", "CROCODILES", "CATERPILLAR", "HIPPOPOTAMUS", "UNICORNFISH", "HANNIBAL"]

# Generate and save boards
Path("boards").mkdir(parents=True, exist_ok=True)

boards = {
    "small_board.txt": generate_scrambled_board(6, small_words),
    "medium_board.txt": generate_scrambled_board(10, medium_words),
    "large_board.txt": generate_scrambled_board(14, large_words),
}

for name, board in boards.items():
    save_board(f"./{name}", board)

list(boards.keys())

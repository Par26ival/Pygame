import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the chessboard
board_size = 800
square_size = board_size // 8

# Define colors
LIGHT_COLOR = (240, 217, 181)
DARK_COLOR = (181, 136, 99)
HIGHLIGHT_COLOR = (102, 255, 102)
SELECTED_COLOR = (255, 255, 102)

# Set the window size and title
screen = pygame.display.set_mode((board_size, board_size))
pygame.display.set_caption("Chess Game")

# Load chess piece images and resize them
piece_images = {
    'wp': pygame.transform.scale(pygame.image.load('images/white_pawn.png'), (square_size, square_size)),
    'wr': pygame.transform.scale(pygame.image.load('images/white_rook.png'), (square_size, square_size)),
    'wn': pygame.transform.scale(pygame.image.load('images/white_knight.png'), (square_size, square_size)),
    'wb': pygame.transform.scale(pygame.image.load('images/white_bishop.png'), (square_size, square_size)),
    'wq': pygame.transform.scale(pygame.image.load('images/white_queen.png'), (square_size, square_size)),
    'wk': pygame.transform.scale(pygame.image.load('images/white_king.png'), (square_size, square_size)),
    'bp': pygame.transform.scale(pygame.image.load('images/black_pawn.png'), (square_size, square_size)),
    'br': pygame.transform.scale(pygame.image.load('images/black_rook.png'), (square_size, square_size)),
    'bn': pygame.transform.scale(pygame.image.load('images/black_knight.png'), (square_size, square_size)),
    'bb': pygame.transform.scale(pygame.image.load('images/black_bishop.png'), (square_size, square_size)),
    'bq': pygame.transform.scale(pygame.image.load('images/black_queen.png'), (square_size, square_size)),
    'bk': pygame.transform.scale(pygame.image.load('images/black_king.png'), (square_size, square_size))
}

# Initialize the chessboard
chessboard = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
]

# Initialize the selected piece
selected_piece = None
selected_piece_pos = None

# Helper function to draw the chessboard
def draw_chessboard():
    for row in range(8):
        for col in range(8):
            square_color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, square_color, (col * square_size, row * square_size, square_size, square_size))
            piece = chessboard[row][col]
            if piece:
                screen.blit(piece_images[piece], (col * square_size, row * square_size))

# Helper function to get the chessboard position from the mouse coordinates
def get_position_from_mouse(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col

# Helper function to check if a move is valid
def is_valid_move(start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = chessboard[start_row][start_col]

    # Check if the piece is moving within the bounds of the chessboard
    if not (0 <= end_row < 8 and 0 <= end_col < 8):
        return False

    # Check if the destination is occupied by a piece of the same color
    if chessboard[end_row][end_col] != '' and chessboard[end_row][end_col][0] == piece[0]:
        return False

    # Implement specific movement logic for each piece type
    if piece[1] == 'p':
        # Pawn movement logic
        if piece[0] == 'w':
            if start_row == 6 and start_col == end_col and start_row - end_row == 2 and chessboard[end_row + 1][end_col] == '':
                return True
            elif start_col == end_col and start_row - end_row == 1 and chessboard[end_row][end_col] == '':
                return True
            elif abs(start_col - end_col) == 1 and start_row - end_row == 1 and chessboard[end_row][end_col] != '':
                return True
        else:
            if start_row == 1 and start_col == end_col and end_row - start_row == 2 and chessboard[end_row - 1][end_col] == '':
                return True
            elif start_col == end_col and end_row - start_row == 1 and chessboard[end_row][end_col] == '':
                return True
            elif abs(start_col - end_col) == 1 and end_row - start_row == 1 and chessboard[end_row][end_col] != '':
                return True
    elif piece[1] == 'r':
        # Rook movement logic
        if start_row == end_row or start_col == end_col:
            if start_row == end_row:
                step = 1 if start_col < end_col else -1
                for col in range(start_col + step, end_col, step):
                    if chessboard[start_row][col] != '':
                        return False
            else:
                step = 1 if start_row < end_row else -1
                for row in range(start_row + step, end_row, step):
                    if chessboard[row][start_col] != '':
                        return False
            return True
    elif piece[1] == 'n':
        # Knight movement logic
        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1:
            return True
        elif abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2:
            return True
    elif piece[1] == 'b':
        # Bishop movement logic
        if abs(start_row - end_row) == abs(start_col - end_col):
            step_row = 1 if start_row < end_row else -1
            step_col = 1 if start_col < end_col else -1
            row, col = start_row + step_row, start_col + step_col
            while row != end_row and col != end_col:
                if chessboard[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return True
    elif piece[1] == 'q':
        # Queen movement logic
        if start_row == end_row or start_col == end_col:
            if start_row == end_row:
                step = 1 if start_col < end_col else -1
                for col in range(start_col + step, end_col, step):
                    if chessboard[start_row][col] != '':
                        return False
            else:
                step = 1 if start_row < end_row else -1
                for row in range(start_row + step, end_row, step):
                    if chessboard[row][start_col] != '':
                        return False
            return True
        elif abs(start_row - end_row) == abs(start_col - end_col):
            step_row = 1 if start_row < end_row else -1
            step_col = 1 if start_col < end_col else -1
            row, col = start_row + step_row, start_col + step_col
            while row != end_row and col != end_col:
                if chessboard[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return True
    elif piece[1] == 'k':
        # King movement logic
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not selected_piece:
                # Select a piece
                row, col = get_position_from_mouse(pygame.mouse.get_pos())
                piece = chessboard[row][col]
                if piece:
                    selected_piece = piece
                    selected_piece_pos = (row, col)
            else:
                # Move the selected piece
                row, col = get_position_from_mouse(pygame.mouse.get_pos())
                if is_valid_move(selected_piece_pos, (row, col)):
                    chessboard[selected_piece_pos[0]][selected_piece_pos[1]] = ''
                    chessboard[row][col] = selected_piece
                selected_piece = None
                selected_piece_pos = None

    screen.fill((255, 255, 255))
    draw_chessboard()

    if selected_piece_pos:
        pygame.draw.rect(screen, SELECTED_COLOR, (selected_piece_pos[1] * square_size, selected_piece_pos[0] * square_size, square_size, square_size))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
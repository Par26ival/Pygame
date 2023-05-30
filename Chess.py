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


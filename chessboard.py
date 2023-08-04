import pygame

# Constants for the chessboard and cell size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BOARD_SIZE = 8
CELL_SIZE = SCREEN_WIDTH // BOARD_SIZE

QUEEN_IMAGE = pygame.image.load("img/chess_com_black_queen.png")
CHESSBOARD_IMAGE = pygame.image.load("img/chess_com_green_board.png")


class Queen(pygame.sprite.Sprite):
    def __init__(self, image, row, col):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.update_position()
        self.attacked_squares = self.get_attacked_squares_by_queen(row, col)

    def update_position(self):
        self.rect.x = self.col * CELL_SIZE
        self.rect.y = self.row * CELL_SIZE

    @staticmethod
    def is_valid_position(row, col):
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

    def get_attacked_squares_by_queen(self, row, col):
        attacked_squares = set()

        attacked_squares.add((row, col))

        # Horizontal and Vertical
        for i in range(BOARD_SIZE):
            if i != col:
                attacked_squares.add((row, i))
            if i != row:
                attacked_squares.add((i, col))

        # Diagonal
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = row + dr, col + dc
            while self.is_valid_position(r, c):
                attacked_squares.add((r, c))
                r += dr
                c += dc

        return attacked_squares


class ChessboardSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = CHESSBOARD_IMAGE
        self.rect = self.image.get_rect()


class Chessboard:
    def __init__(self):
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.sprites = pygame.sprite.Group()
        self.chessboard_sprite: pygame.sprite.Sprite = ChessboardSprite()
        self.sprites.add(self.chessboard_sprite)
        self.attacked_squares_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    def get_queen_at(self, row, col):
        return self.board[row][col]

    def place_queen(self, row, col):
        if self.board[row][col] is None:
            piece = Queen(QUEEN_IMAGE, row, col)
            self.board[row][col] = piece
            self.sprites.add(piece)

    def remove_queen(self, row, col):
        piece = self.board[row][col]
        if piece is not None:
            self.board[row][col] = None
            self.sprites.remove(piece)
            if hasattr(piece, "attacked_squares"):
                self.attacked_squares_overlay.fill((0, 0, 0, 0))  # Clear attacked squares overlay
                for r, c in piece.attacked_squares:
                    if (r, c) != (piece.row, piece.col):
                        pygame.draw.rect(self.attacked_squares_overlay, (255, 0, 0, 100),
                                         (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def draw(self, screen):
        self.sprites.draw(screen)

        # Clear the attacked_squares_overlay
        self.attacked_squares_overlay.fill((0, 0, 0, 0))

        for piece in self.sprites:
            if isinstance(piece, Queen):
                if hasattr(piece, "attacked_squares"):
                    for r, c in piece.attacked_squares:
                        if (r, c) != (piece.row, piece.col):
                            pygame.draw.rect(self.attacked_squares_overlay, (255, 0, 0, 100),
                                         (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        else:
                            pygame.draw.rect(self.attacked_squares_overlay, (0, 0, 0, 0),
                                             (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(self.attacked_squares_overlay, (0, 0))


class ChessboardBacktracking:
    def __init__(self):
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.sprites = pygame.sprite.Group()
        self.chessboard_sprite: pygame.sprite.Sprite = ChessboardSprite()
        self.sprites.add(self.chessboard_sprite)
        self.attacked_squares_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    def get_queen_at(self, row, col):
        return self.board[row][col]

    def place_queen(self, row, col):
        if self.board[row][col] is None:
            piece = Queen(QUEEN_IMAGE, row, col)
            self.board[row][col] = piece
            self.sprites.add(piece)

    def remove_queen(self, row, col):
        piece = self.board[row][col]
        if piece is not None:
            self.board[row][col] = None
            self.sprites.remove(piece)
            if hasattr(piece, "attacked_squares"):
                self.attacked_squares_overlay.fill((0, 0, 0, 0))  # Clear attacked squares overlay
                for r, c in piece.attacked_squares:
                    if (r, c) != (piece.row, piece.col):
                        pygame.draw.rect(self.attacked_squares_overlay, (255, 0, 0, 100),
                                         (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def draw(self, screen):
        self.sprites.draw(screen)

        # Clear the attacked_squares_overlay
        self.attacked_squares_overlay.fill((0, 0, 0, 0))

        for piece in self.sprites:
            if isinstance(piece, Queen):
                if hasattr(piece, "attacked_squares"):
                    for r, c in piece.attacked_squares:
                        if (r, c) != (piece.row, piece.col):
                            pygame.draw.rect(self.attacked_squares_overlay, (255, 0, 0, 100),
                                         (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        else:
                            pygame.draw.rect(self.attacked_squares_overlay, (0, 0, 0, 0),
                                             (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(self.attacked_squares_overlay, (0, 0))
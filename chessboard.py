import pygame

# Constants for the chessboard and cell size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BOARD_SIZE = 8
CELL_SIZE = SCREEN_WIDTH // BOARD_SIZE

QUEEN_IMAGE = pygame.image.load("img/chess_com_black_queen.png")
CHESSBOARD_IMAGE = pygame.image.load("img/chess_com_green_board.png")


class Queen(pygame.sprite.Sprite):
    """Class representing a queen on the chessboard.

    Attributes:
        image (pygame.Surface): The image representing the queen.
        row (int): The row coordinate of the queen on the chessboard.
        col (int): The column coordinate of the queen on the chessboard.
        rect (pygame.Rect): The bounding rectangle of the queen image.
        attacked_squares (set): A set of (row, col) coordinates representing the squares attacked by the queen.

    Methods:
        update_position: Updates the queen's position on the chessboard.
        is_valid_position(row, col): Checks if a given row and column coordinates are valid on the chessboard.
        get_attacked_squares_by_queen(row, col): Calculates the set of attacked squares by the queen at given coordinates.
    """
    def __init__(self, image, row, col):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.update_position()
        self.attacked_squares = self.get_attacked_squares_by_queen(row, col)

    def update_position(self):
        """Updates the queen's position on the chessboard based on row and column coordinates."""
        self.rect.x = self.col * CELL_SIZE
        self.rect.y = self.row * CELL_SIZE

    @staticmethod
    def is_valid_position(row, col):
        """Checks if a given row and column coordinates are valid on the chessboard.

        Returns:
            bool: True if the coordinates are within the chessboard boundaries, False otherwise.
        """
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

    def get_attacked_squares_by_queen(self, row, col):
        """Calculates the set of attacked squares by the queen at given coordinates.

        Parameters:
            row (int): The row coordinate of the queen.
            col (int): The column coordinate of the queen.

        Returns:
            set: A set of (row, col) coordinates representing the squares attacked by the queen.
        """
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
    """Class representing the chessboard image on the screen.

    Attributes:
        image (pygame.Surface): The image representing the chessboard.
        rect (pygame.Rect): The bounding rectangle of the chessboard image.
    """
    def __init__(self):
        super().__init__()
        self.image = CHESSBOARD_IMAGE
        self.rect = self.image.get_rect()


class Chessboard:
    """Class representing the chessboard and its state.

    Attributes:
        board (List[List[Queen or None]]): A 2D list representing the chessboard and the queens placed on it.
        sprites (pygame.sprite.Group): A group containing all the sprites on the chessboard.
        chessboard_sprite (pygame.sprite.Sprite): The sprite representing the chessboard image.
        attacked_squares_overlay (pygame.Surface): A transparent surface used to draw attacked squares for visualization.

    Methods:
        get_queen_at(row, col): Get the queen at a given row and column coordinates.
        is_queen_at(row, col): Check if there is a queen at a given row and column coordinates.
        place_queen(row, col): Place a queen at a given row and column coordinates on the chessboard.
        remove_queen(row, col): Remove a queen from a given row and column coordinates on the chessboard.
        draw(screen): Draw the chessboard and its state on the screen.
    """
    def __init__(self):
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.sprites = pygame.sprite.Group()
        self.chessboard_sprite: pygame.sprite.Sprite = ChessboardSprite()
        self.sprites.add(self.chessboard_sprite)
        self.attacked_squares_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    def get_queen_at(self, row: int, col: int):
        """Get the queen at a given row and column coordinates.

        Parameters:
            row (int): The row coordinate.
            col (int): The column coordinate.

        Returns:
            Queen or None: The Queen object if a queen is present, None otherwise.
        """
        return self.board[row][col]

    def is_queen_at(self, row: int, col: int):
        """Check if there is a queen at a given row and column coordinates.

        Parameters:
            row (int): The row coordinate.
            col (int): The column coordinate.

        Returns:
            bool: True if there is a queen, False otherwise.
        """
        return isinstance(self.board[row][col], Queen)

    def place_queen(self, row: int, col: int):
        """Place a queen at a given row and column coordinates on the chessboard.

        Parameters:
            row (int): The row coordinate.
            col (int): The column coordinate.
        """
        if self.board[row][col] is None:
            piece = Queen(QUEEN_IMAGE, row, col)
            self.board[row][col] = piece
            self.sprites.add(piece)

    def remove_queen(self, row: int, col: int):
        """Remove a queen from a given row and column coordinates on the chessboard.

        Parameters:
            row (int): The row coordinate.
            col (int): The column coordinate.
        """
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

    def draw(self, screen: pygame.Surface):
        """Draw the chessboard and its state on the screen.

        Parameters:
            screen (pygame.Surface): The screen surface to draw on.
        """
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

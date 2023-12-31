import pygame
from chessboard import Chessboard

# Constants for the chessboard and cell size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BOARD_SIZE = 8
CELL_SIZE = SCREEN_WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)


def draw_chessboard(screen: pygame.Surface, chessboard: Chessboard):
    """
    Draws the chessboard on the screen.

    Args:
        screen (pygame.Surface): The pygame surface to draw the chessboard on.
        chessboard (Chessboard): The instance of the Chessboard class representing the current chessboard state.
    """
    screen.fill(WHITE)
    chessboard.draw(screen)
    pygame.display.flip()
    pygame.time.delay(60)


def solve_n_queens(screen: pygame.Surface, clock: pygame.time.Clock,  chessboard: Chessboard, col: int):
    """
    Solves the N-Queens problem recursively and visually displays the process on the screen.

    Args:
        screen (pygame.Surface): The pygame surface to visualize the chessboard.
        clock (pygame.time.Clock): The pygame clock to control the frame rate.
        chessboard (Chessboard): The instance of the Chessboard class representing the current chessboard state.
        col (int): The current column being processed for placing a queen.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col == BOARD_SIZE:
        draw_chessboard(screen, chessboard)
        return True
    for i in range(BOARD_SIZE):
        if is_safe(chessboard, i, col):
            chessboard.place_queen(i, col)
            draw_chessboard(screen, chessboard)

            if solve_n_queens(screen, clock, chessboard, col + 1):
                return True
            chessboard.remove_queen(i, col)
            draw_chessboard(screen, chessboard)
    return False


def is_safe(chessboard: Chessboard, row: int, col: int):
    """
    Checks if it is safe to place a queen at a specific cell on the chessboard.

    Args:
        chessboard (Chessboard): The instance of the Chessboard class representing the current chessboard state.
        row (int): The row index of the cell to be checked.
        col (int): The column index of the cell to be checked.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    for x in range(col):
        if chessboard.is_queen_at(row, x):
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard.is_queen_at(x, y):
            return False
    for x, y in zip(range(row, BOARD_SIZE, 1), range(col, -1, -1)):
        if chessboard.is_queen_at(x, y) == 1:
            return False
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("8-Queens Problem")
    clock = pygame.time.Clock()
    chessboard = Chessboard()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                clicked_cell = (mouse_pos[1] // CELL_SIZE, mouse_pos[0] // CELL_SIZE)

                existing_piece = chessboard.get_queen_at(*clicked_cell)

                if existing_piece is None:
                    chessboard.place_queen(*clicked_cell)
                else:
                    chessboard.remove_queen(*clicked_cell)

        draw_chessboard(screen, chessboard)
        pygame.time.delay(4000)

        solve_n_queens(screen, clock, chessboard, 0)

        pygame.time.delay(5000)
        pygame.quit()


if __name__ == "__main__":
    main()

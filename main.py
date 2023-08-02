import pygame
from chessboard import Chessboard

# Constants for the chessboard and cell size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BOARD_SIZE = 8
CELL_SIZE = SCREEN_WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)


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

        screen.fill(WHITE)
        chessboard.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

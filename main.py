import pygame

from data.classes.Board import Board 
from data.classes.bots.bot import Bot

# Configuration
AUTO_PLAY = False  # Set to True for automatic bot moves, False for manual stepping

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(
    "Chess - " + ("Auto Mode" if AUTO_PLAY else "Manual Mode (Press SPACE for moves)")
)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])


def draw(display):
    display.fill("white")
    board.draw(display)
    # Draw turn indicator only in manual mode
    if not AUTO_PLAY:
        font = pygame.font.Font(None, 36)
        if board.turn == "black":
            text = font.render("Bot's turn (Black) - Press SPACE", True, (0, 0, 0))
        else:
            text = font.render("Bot's turn (White) - Press SPACE", True, (0, 0, 0))
        display.blit(text, (10, WINDOW_SIZE[1] - 40))
    pygame.display.update()


def make_bot_move():
    if board.turn == "black":
        m = bot1.move("black", board)
        board.handle_move(m[0], m[1])
    else:
        m = bot2.move("white", board)
        board.handle_move(m[0], m[1])


if __name__ == "__main__":
    running = True
    # bot1 = RandomBot()
    # bot2 = RandomBot()
    bot1 = Bot()
    bot2 = Bot()
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse is clicked
                if event.button == 1:
                    board.handle_click(mx, my)
                    print(board.last_captured)
            elif event.type == pygame.KEYDOWN and not AUTO_PLAY:
                if event.key == pygame.K_SPACE:
                    # Make bot move when space is pressed (only in manual mode)
                    make_bot_move()

        # In auto play mode, make bot moves automatically
        if AUTO_PLAY:
            make_bot_move()

        if board.is_in_checkmate("black"):  # If black is in checkmate
            print("White wins!")
            running = False
        elif board.is_in_checkmate("white"):  # If white is in checkmate
            print("Black wins!")
            running = False
        elif board.is_in_draw():
            print("Draw!")
            running = False

        # Draw the board
        draw(screen)

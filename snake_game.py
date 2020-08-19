import pygame
import sys
from Snake import Snake
from Player import Player
from Food import Food


def run_game():
    play_again = True

    while play_again:
        screen = pygame.display.set_mode((1200, 1200))
        snake_color = (255, 255, 255)
        snake = Snake(300, 300, 30, 30)
        player = Player()
        food = Food(snake)
        game_won = False
        running = True
        snakes_added = 0

        while running:

            snake.direction = player.get_direction()

            screen.fill((0, 0, 0))

            snake.draw_snake(screen, snake_color)

            food.draw_food(screen, (0, 255, 0))

            if snakes_added > 0:
                snakes_added -= 1
                snake.add_snake()

            snake.move_snake()

            snake.update_square_directions()

            if food.is_eaten():
                snakes_added += 4
                player.score += 4
                if player.score >= 1600:
                    game_won = True

            if snake.is_out_of_bounds() or snake.is_collision() or game_won:
                running = False

            pygame.display.flip()

            pygame.time.delay(50)

        is_enter = False
        while not is_enter:
            if not game_won:
                pygame.font.init()
                font = pygame.font.SysFont('notosans', 100)
                text = font.render("Game Over", False, (255, 0, 0))
                screen.blit(text, (350, 400))

            else:
                pygame.font.init()
                font = pygame.font.SysFont('notosans', 100)
                text = font.render("You Won!!", False, (255, 255, 0))
                screen.blit(text, (350, 400))

            font2 = pygame.font.SysFont('notosans', 30)
            text2 = font2.render("Press ENTER to play again or press ESC to quit", False, (255, 100, 0))
            screen.blit(text2, (310, 550))
            text3 = font2.render("Your Score: {}".format(player.score), False, (0, 200, 100))
            screen.blit(text3, (530, 650))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_enter = True

                    if event.key == pygame.K_ESCAPE:
                        sys.exit()


if __name__ == '__main__':
    run_game()
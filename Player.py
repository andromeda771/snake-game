import pygame
import sys


class Player:
    directions = {pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right', pygame.K_DOWN: 'down', pygame.K_UP: 'up', None: None}

    def __init__(self):
        self.current_direction = None
        self.score = 1

    def get_direction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in Player.directions:
                    self.current_direction = event.key
                    return Player.directions[self.current_direction]

        return Player.directions[self.current_direction]

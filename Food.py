import pygame
import random


class Food:
    def __init__(self, snake):
        self.no_food = True
        self.snake_list = snake.snake_list
        self.food = pygame.Rect(0, 0, 30, 30)

    def create_food(self):
        self.no_food = False
        self.food.x, self.food.y = Food.generate_random_coords(self)

    def draw_food(self, surface, color):
        if self.no_food:
            Food.create_food(self)
        pygame.draw.rect(surface, color, self.food)

    def generate_random_coords(self):
        square_available = False
        random_x = random.randrange(0, 1170, 30)
        random_y = random.randrange(0, 1170, 30)

        while not square_available:
            for square in self.snake_list:
                if random_x == square.x and random_y == square.y:
                    random_x = random.randrange(0, 1170, 30)
                    random_y = random.randrange(0, 1170, 30)
                    break

                if self.snake_list.index(square) == len(self.snake_list) - 1:
                    square_available = True

        return random_x, random_y

    def is_eaten(self):
        x, y = self.snake_list[0].x, self.snake_list[0].y
        if self.food.x == x and self.food.y == y:
            self.no_food = True
            return True

import pygame


class Snake:
    def __init__(self, x, y, width, height, direction=None):
        self.direction = direction
        self.current_direction = None
        self.snake_list = [pygame.Rect(x, y, width, height)]
        self.square_directions = [self.current_direction]

    def move_snake(self):
        original_x = self.snake_list[0].x
        original_y = self.snake_list[0].y

        if self.direction == 'right' and Snake.can_move(self, 'right'):
            self.current_direction = self.direction
            self.square_directions[0] = self.current_direction

        elif self.direction == 'left' and Snake.can_move(self, 'left'):
            self.current_direction = self.direction
            self.square_directions[0] = self.current_direction

        elif self.direction == 'up' and Snake.can_move(self, 'up'):
            self.current_direction = self.direction
            self.square_directions[0] = self.current_direction

        elif self.direction == 'down' and Snake.can_move(self, 'down'):
            self.current_direction = self.direction
            self.square_directions[0] = self.current_direction

        if self.current_direction == 'right':
            self.snake_list[0].x += 30

        elif self.current_direction == 'left':
            self.snake_list[0].x -= 30

        elif self.current_direction == 'up':
            self.snake_list[0].y -= 30

        elif self.current_direction == 'down':
            self.snake_list[0].y += 30

        if len(self.snake_list) > 1:
            index = 1
            while index < len(self.snake_list):
                o_x = self.snake_list[index].x
                o_y = self.snake_list[index].y

                self.snake_list[index].x = original_x
                self.snake_list[index].y = original_y

                original_x = o_x
                original_y = o_y

                index += 1

    def draw_snake(self, surface, color):
        for square in self.snake_list:
            pygame.draw.rect(surface, color, square)

    def add_snake(self):
        last_square_x, last_square_y = self.snake_list[-1].x, self.snake_list[-1].y
        last_direction = self.square_directions[-1]

        if last_direction == 'right':
            self.snake_list.append(pygame.Rect(last_square_x - 30, last_square_y, 30, 30))

        elif last_direction == 'left':
            self.snake_list.append(pygame.Rect(last_square_x + 30, last_square_y, 30, 30))

        elif last_direction == 'down':
            self.snake_list.append(pygame.Rect(last_square_x, last_square_y - 30, 30, 30))

        elif last_direction == 'up':
            self.snake_list.append(pygame.Rect(last_square_x, last_square_y + 30, 30, 30))

        self.square_directions.append(last_direction)

    def can_move(self, direct):
        if len(self.snake_list) > 1:
            other_x, other_y = self.snake_list[1].x, self.snake_list[1].y

            if direct == 'right':
                if self.snake_list[0].x + 30 == other_x:
                    return False

            elif direct == 'left':
                if self.snake_list[0].x - 30 == other_x:
                    return False

            elif direct == 'down':
                if self.snake_list[0].y + 30 == other_y:
                    return False

            elif direct == 'up':
                if self.snake_list[0].y - 30 == other_y:
                    return False

        return True

    def is_out_of_bounds(self):
        current_x, current_y = self.snake_list[0].x, self.snake_list[0].y

        if self.current_direction == 'right':
            if current_x + 30 > 1200:
                return True

        elif self.current_direction == 'left':
            if current_x - 30 < -30:
                return True

        elif self.current_direction == 'down':
            if current_y + 30 > 1200:
                return True

        elif self.current_direction == 'up':
            if current_y - 30 < -30:
                return True

        return False

    def update_square_directions(self):
        if len(self.square_directions) > 1:
            self.square_directions.insert(0, self.current_direction)
            self.square_directions.pop()

    def is_collision(self):
        if self.snake_list[0].collidelist(self.snake_list[1:]) > 0:
            return True

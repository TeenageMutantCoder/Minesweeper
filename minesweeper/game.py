import pygame
import sys
import os
from random import choices


class Square():
    def __init__(self):
        self.is_clicked = False
        self.is_mine = False
        self.is_flagged = False
        self.num_of_nearby_mines = None


class Game():
    def __init__(self, width, height, grid_size=20, difficulty="normal"):
        pygame.init()
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.difficulty = difficulty
        self.game_font = pygame.font.SysFont("Arial", 48)
        self.game_over_font = pygame.font.SysFont("Arial", 72)
        self.window = pygame.display.set_mode((width, height))
        self.box_size = self.width // self.grid_size
        mine_icon_path = os.path.relpath(os.path.join("minesweeper", "assets", "mine.png"))
        flag_icon_path = os.path.relpath(os.path.join("minesweeper", "assets", "flag.png"))
        mine_icon = open(mine_icon_path, "rb")
        flag_icon = open(flag_icon_path, "rb")
        self.mine_icon = pygame.image.load(mine_icon, "mine.png").convert_alpha()
        self.flag_icon = pygame.image.load(flag_icon, "flag.png").convert_alpha()
        self.flag_icon = pygame.transform.scale(self.flag_icon, (self.box_size - 1, self.box_size - 1))
        self.mine_icon = pygame.transform.scale(self.mine_icon, (self.box_size - 1, self.box_size - 1))
        self.mine_count_to_number = {"1":(255, 0, 0),     # Red             Number of mines around a clicked square
                                     "2":(255, 51, 0),    # Orange          will be rendered as text in the colors
                                     "3":(255, 255, 0),   # Yellow          shown in this dictionary
                                     "4":(198, 255, 26),  # Yellow-Green
                                     "5":(0, 255, 0),     # Green
                                     "6":(0, 204, 102),   # Green-Cyan
                                     "7":(0, 255, 204),   # Cyan
                                     "8":(0, 153, 255)}   # Cyan-Blue
        self.game_over = False
        self.game_over_message = ""
        self.game_over_color = (0, 0, 0)
        pygame.display.set_caption("Minesweeper")
        self.start_game()
        self.update()

    def start_game(self):
        # Create grid of size given by variable 'self.grid_size'
        self.grid = [[Square() for count_x in range(self.grid_size)] for count_y in range(self.grid_size)]

        if self.difficulty == "easy":
            num_of_mines = 10
        elif self.difficulty == "normal":
            num_of_mines = 40
        else:
            num_of_mines = 99

        # Set specified number of random squares as mines
        one_dimensional_grid = [square for row in self.grid for square in row]
        for square in choices(one_dimensional_grid, k=num_of_mines):
            square.is_mine = True

    def find_grid_position(self, pos_x, pos_y):
        '''Converts mouse click position to grid array index. Returns tuple with indices.'''
        for count_x in range(self.grid_size):
            if (count_x * self.box_size) < pos_x < ((count_x + 1) * self.box_size):
                column = count_x
                break
        for count_y in range(self.grid_size):
            if (count_y * self.box_size) < pos_y < ((count_y + 1) * self.box_size):
                row = count_y
                break
        try:
            return row, column
        except UnboundLocalError:
            return

    def on_click(self, event):
        try:
            row, column = self.find_grid_position(event.pos[0], event.pos[1])
            square = self.grid[row][column]
            if event.button == 1:  # Left mouse click
                if not square.is_clicked and not square.is_flagged:
                    square.is_clicked = True
                    if square.is_mine:
                        self.game_over = True
                        self.game_over_message = "You Lost!"
                        self.game_over_color = (255, 0, 0)
                
            else:  # Right mouse click
                if not square.is_clicked:
                    square.is_flagged = not square.is_flagged
        except TypeError:  # If player clicks on a line, do nothing
            return

    def check_nearby_squares(self, row, column):
        '''Checks whether the squares around the given square location are mines, returns that number'''
        self.grid[row][column].num_of_nearby_mines = 0

        def check_upper_left(self, row, column):
            if self.grid[row - 1][column - 1].is_mine:  # Check upper left
                self.grid[row][column].num_of_nearby_mines += 1

        def check_up(self, row, column):
            if self.grid[row - 1][column].is_mine:  # Check up
                self.grid[row][column].num_of_nearby_mines += 1
        
        def check_upper_right(self, row, column):
            if self.grid[row - 1][column + 1].is_mine:  # Check upper right
                self.grid[row][column].num_of_nearby_mines += 1
        
        def check_left(self, row, column):
            if self.grid[row][column - 1].is_mine:  # Check left
                self.grid[row][column].num_of_nearby_mines += 1
        
        def check_right(self, row, column):
            if self.grid[row][column + 1].is_mine:  # Check right
                self.grid[row][column].num_of_nearby_mines += 1
        
        def check_lower_left(self, row, column):
            if self.grid[row + 1][column - 1].is_mine: # Check lower left
                self.grid[row][column].num_of_nearby_mines += 1
        
        def check_down(self, row, column):
            if self.grid[row + 1][column].is_mine:  # Check down
                self.grid[row][column].num_of_nearby_mines += 1
        
        def check_lower_right(self, row, column):
            if self.grid[row + 1][column + 1].is_mine:  # Check lower right
                self.grid[row][column].num_of_nearby_mines += 1
        
        if row == 0 and column == 0:  # Upper left corner grid square
            check_right(self, row, column)
            check_down(self, row, column)
            check_lower_right(self, row, column)
            return
        elif row == 0 and column == self.grid_size - 1:  # Upper right corner grid square
            check_left(self, row, column)
            check_lower_left(self, row, column)
            check_down(self, row, column)
            return
        elif row == self.grid_size - 1 and column == 0:  # Lower left corner grid square
            check_up(self, row, column)
            check_upper_right(self, row, column)
            check_right(self, row, column)
            return
        elif row == self.grid_size - 1 and column == self.grid_size - 1:  # Lower right corner grid square
            check_upper_left(self, row, column)
            check_up(self, row, column)
            check_left(self, row, column)
            return
        elif row == 0:  # Top side
            check_left(self, row, column)
            check_right(self, row, column)
            check_lower_left(self, row, column)
            check_down(self, row, column)
            check_lower_right(self, row, column)
            return
        elif row == self.grid_size - 1:  # Bottom side
            check_upper_left(self, row, column)
            check_up(self, row, column)
            check_upper_right(self, row, column)
            check_left(self, row, column)
            check_right(self, row, column)
            return
        elif column == 0:  # Left side
            check_up(self, row, column)
            check_upper_right(self, row, column)
            check_right(self, row, column)
            check_down(self, row, column)
            check_lower_right(self, row, column)
            return
        elif column == self.grid_size - 1: # Right side
            check_upper_left(self, row, column)
            check_up(self, row, column)
            check_left(self, row, column)
            check_lower_left(self, row, column)
            check_down(self, row, column)
            return
        else:
            check_upper_left(self, row, column)
            check_up(self, row, column)
            check_upper_right(self, row, column)
            check_left(self, row, column)
            check_right(self, row, column)
            check_lower_left(self, row, column)
            check_down(self, row, column)
            check_lower_right(self, row, column)
            return

    def draw_grid(self, row, column):
        rect = pygame.Rect((row * self.box_size, column * self.box_size), (self.box_size, self.box_size))
        pygame.draw.rect(self.window, (0, 0, 0), rect, 1)

    def select_nearby_squares(self, row, column):
        if row == 0 and column == 0:  # Upper left corner grid square
            self.grid[row][column + 1].is_clicked = True      # Select right
            self.grid[row + 1][column].is_clicked = True      # Select down
            self.grid[row + 1][column + 1].is_clicked = True  # Select lower right
            return
        elif row == 0 and column == self.grid_size - 1:  # Upper right corner grid square
            self.grid[row][column - 1].is_clicked = True      # Select left
            self.grid[row + 1][column - 1].is_clicked = True  # Select lower left
            self.grid[row + 1][column].is_clicked = True      # Select down
            return
        elif row == self.grid_size - 1 and column == 0:  # Lower left corner grid square
            self.grid[row - 1][column].is_clicked = True      # Select up
            self.grid[row - 1][column + 1].is_clicked = True  # Select upper right
            self.grid[row][column + 1].is_clicked = True      # Select right
            return
        elif row == self.grid_size - 1 and column == self.grid_size - 1:  # Lower right corner grid square
            self.grid[row - 1][column - 1].is_clicked = True  # Select upper left
            self.grid[row - 1][column].is_clicked = True      # Select up
            self.grid[row][column - 1].is_clicked = True      # Select left
            return
        elif row == 0:  # Top side
            self.grid[row][column - 1].is_clicked = True      # Select left
            self.grid[row][column + 1].is_clicked = True      # Select right
            self.grid[row + 1][column - 1].is_clicked = True  # Select lower left
            self.grid[row + 1][column].is_clicked = True      # Select down
            self.grid[row + 1][column + 1].is_clicked = True  # Select lower right
            return
        elif row == self.grid_size - 1:  # Bottom side
            self.grid[row - 1][column - 1].is_clicked = True  # Select upper left
            self.grid[row - 1][column].is_clicked = True      # Select up
            self.grid[row - 1][column + 1].is_clicked = True  # Select upper right
            self.grid[row][column - 1].is_clicked = True      # Select left
            self.grid[row][column + 1].is_clicked = True      # Select right
            return
        elif column == 0:  # Left side
            self.grid[row - 1][column].is_clicked = True      # Select up
            self.grid[row - 1][column + 1].is_clicked = True  # Select upper right
            self.grid[row][column + 1].is_clicked = True      # Select right
            self.grid[row + 1][column].is_clicked = True      # Select down
            self.grid[row + 1][column + 1].is_clicked = True  # Select lower right
            return
        elif column == self.grid_size - 1: # Right side
            self.grid[row - 1][column - 1].is_clicked = True  # Select upper left
            self.grid[row - 1][column].is_clicked = True      # Select up
            self.grid[row][column - 1].is_clicked = True      # Select left
            self.grid[row + 1][column - 1].is_clicked = True  # Select lower left
            self.grid[row + 1][column].is_clicked = True      # Select down
            return
        else:
            self.grid[row - 1][column - 1].is_clicked = True  # Select upper left
            self.grid[row - 1][column].is_clicked = True      # Select up
            self.grid[row - 1][column + 1].is_clicked = True  # Select upper right
            self.grid[row][column - 1].is_clicked = True      # Select left
            self.grid[row][column + 1].is_clicked = True      # Select right
            self.grid[row + 1][column - 1].is_clicked = True  # Select lower left
            self.grid[row + 1][column].is_clicked = True      # Select down
            self.grid[row + 1][column + 1].is_clicked = True  # Select lower right
            return

    def show_num_of_nearby_mines(self, row, column):
        square = self.grid[row][column]
        nearby_mine_count_text = self.game_font.render(str(square.num_of_nearby_mines), True, 
                                                  self.mine_count_to_number[str(square.num_of_nearby_mines)])
        rect = nearby_mine_count_text.get_rect()
        rect.center = (column * self.box_size + self.box_size // 2, row * self.box_size + self.box_size // 2)
        self.window.blit(nearby_mine_count_text, rect)

    def show_clicked(self, row, column):
        square = self.grid[row][column]
        rect = pygame.Rect((column * self.box_size, row * self.box_size), (self.box_size - 1, self.box_size - 1))
        pygame.draw.rect(self.window, (200, 200, 200), rect)
        if square.num_of_nearby_mines is None:
            self.check_nearby_squares(row, column)
        elif square.num_of_nearby_mines == 0:  # If there are no nearby mines, select nearby squares
            self.select_nearby_squares(row, column)
        elif square.num_of_nearby_mines > 0:
            self.show_num_of_nearby_mines(row, column)

    def show_flagged(self, row, column):
        rect = pygame.Rect((column * self.box_size, row * self.box_size), (self.box_size - 1, self.box_size - 1))
        # pygame.draw.rect(self.window, (71, 255, 0), rect)
        self.window.blit(self.flag_icon, rect)
            

    def show_mines(self):
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                if self.grid[row][column].is_mine:
                    rect = pygame.Rect((column * self.box_size, row * self.box_size), (self.box_size - 1, self.box_size- 1))
                    pygame.draw.rect(self.window, (135, 0, 0), rect)
                    self.window.blit(self.mine_icon, rect)

    def check_for_win(self):
        for row in self.grid:
            for column in row:
                if not column.is_clicked and not column.is_mine:  # If the only squares not clicked are mines, player wins
                    return
        self.game_over = True
        self.game_over_message = "You Won!"
        self.game_over_color = (0, 255, 0)  # Green message text

    def update(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over:
                        self.on_click(event)
                    else:
                        self.game_over = False
                        self.start_game()
                    
            if not self.game_over:
                self.window.fill((255, 255, 255))
                for row in range(self.grid_size):
                    for column in range(self.grid_size):
                        square = self.grid[row][column]
                        if square.is_clicked:
                            self.show_clicked(row, column)
                        elif square.is_flagged:
                            self.show_flagged(row, column)
                        self.draw_grid(row, column)
                self.check_for_win()
            else:
                self.show_mines()
                game_over_message = self.game_over_font.render(self.game_over_message, True, self.game_over_color)
                rect = game_over_message.get_rect()
                rect.center = (self.width//2, self.height//2)
                self.window.blit(game_over_message, rect)
            pygame.display.flip()


if __name__ == "__main__":
    Game(700, 700, grid_size=10, difficulty="easy")
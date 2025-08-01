import time
import random
from colorama import init, Back, Style

init()

WIDTH, HEIGHT = 80, 20
COLORS = [Back.BLACK, Back.RED, Back.GREEN, Back.BLUE]
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left

class Ant:
    def __init__(self, x, y, direction=0, symbol='@'):
        self.x = x
        self.y = y
        self.direction = direction
        self.symbol = symbol

    def move(self, grid):
        state = grid[self.y][self.x]
        self.direction = (self.direction + 1) % 4 if state % 2 == 0 else (self.direction - 1) % 4
        grid[self.y][self.x] = (state + 1) % len(COLORS)

        dx, dy = DIRECTIONS[self.direction]
        self.x = (self.x + dx) % WIDTH
        self.y = (self.y + dy) % HEIGHT

def print_grid(grid, ants):
    display = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            display[y][x] = COLORS[grid[y][x]] + ' ' + Style.RESET_ALL

    for ant in ants:
        display[ant.y][ant.x] = COLORS[grid[ant.y][ant.x]] + ant.symbol + Style.RESET_ALL

    print('\n'.join(''.join(row) for row in display))

def main():
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    ants = [Ant(random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)) for _ in range(3)]

    try:
        while True:
            print_grid(grid, ants)
            for ant in ants:
                ant.move(grid)
            time.sleep(0.1)
            print("\033[H", end="")  # Move cursor to top (minimal flicker)
    except KeyboardInterrupt:
        print("\nSimulation ended.")

if __name__ == "__main__":
    main()

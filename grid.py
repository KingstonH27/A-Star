import pygame

CELL_SIZE = 40

screen = None
gridData = []
colors = []


def init(new_screen, width, height):
    global screen, gridData, colors

    screen = new_screen

    gridData = [
        [0 for _ in range(width)]
        for _ in range(height)
    ]

    colors = [
        [None for _ in range(width)]
        for _ in range(height)
    ]


def color_tile(row, col, color):
    colors[row][col] = color


def click(pos):
    x, y = pos

    col = x // CELL_SIZE
    row = y // CELL_SIZE

    if 0 <= row < len(gridData) and 0 <= col < len(gridData[row]):
        gridData[row][col] = 1 - gridData[row][col]


def draw():
    for row in range(len(gridData)):
        for col in range(len(gridData[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Use custom color if one exists
            if colors[row][col] is not None:
                color = colors[row][col]
            elif gridData[row][col] == 1:
                color = (255, 255, 255)
            else:
                color = (50, 50, 50)

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                (100, 100, 100),
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )
import pygame

CELL_SIZE = 40

screen = None
gridData = []
colors = []
texts = []


def init(new_screen, width, height):
    global screen, gridData, colors, texts

    screen = new_screen

    gridData = [
        [0 for _ in range(width)]
        for _ in range(height)
    ]

    colors = [
        [None for _ in range(width)]
        for _ in range(height)
    ]

    texts = [
        ["" for _ in range(width)]
        for _ in range(height)
    ]


def color_tile(node, color):
    colors[node.y][node.x] = color


def text_tile(node, text):
    texts[node.y][node.x] = text


def click(pos):
    x, y = pos

    col = x // CELL_SIZE
    row = y // CELL_SIZE

    if 0 <= row < len(gridData) and 0 <= col < len(gridData[row]):
        gridData[row][col] = 1 - gridData[row][col]

def set(node, value):
    gridData[node.y][node.x] = int(value)

def check(node):
    return gridData[node.y][node.x]

def drawPaths(p):
    global paths
    paths.append(p)


paths = []

def draw():
    global paths
    font = pygame.font.Font(None, 24)


    for row in range(len(gridData)):
        for col in range(len(gridData[row])):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            val = gridData[row][col]

            if colors[row][col] is not None:
                color = colors[row][col]

            elif val == 1:
                color = (255, 255, 255)

            #Color assignments
            # val 2 = explored
            elif val == 2:
                color = (255,165,0)

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

            # Draw text in the center of the tile
            if texts[row][col] != "":
                text_surface = font.render(
                    str(texts[row][col]),
                    True,
                    (0, 0, 0)
                )

                text_rect = text_surface.get_rect(
                    center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2)
                )

                screen.blit(text_surface, text_rect)
    for path in paths:
        n1 = path.n1
        n2 = path.n2
        pygame.draw.line(screen, (255, 0, 0), ((n1.x+0.5) * CELL_SIZE, (n1.y+0.5) * CELL_SIZE), ((n2.x+0.5) * CELL_SIZE, (n2.y+0.5) * CELL_SIZE), 5)


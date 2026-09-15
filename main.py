#Chatgpt was used for the pygame elements

import pygame
import grid
import pathFinding

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid.init(screen, 20, 15)

running = True
drag_value = None

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Start drag
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            col = x // grid.CELL_SIZE
            row = y // grid.CELL_SIZE

            if 0 <= row < len(grid.gridData) and 0 <= col < len(grid.gridData[row]):
                # Remember the state of the initially clicked tile
                drag_value = 1 if grid.gridData[row][col] == 0 else 0

        # End drag
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drag_value = None

    # Paint while dragging
    if drag_value is not None and pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        col = x // grid.CELL_SIZE
        row = y // grid.CELL_SIZE

        if 0 <= row < len(grid.gridData) and 0 <= col < len(grid.gridData[row]):
            grid.gridData[row][col] = drag_value

    screen.fill((30, 30, 30))

    pathFinding.run()

    grid.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
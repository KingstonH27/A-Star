# Chatgpt was used for the pygame elements
https://chatgpt.com/share/6aa97ead-7fac-83ea-906d-ab4d3b7776a7
https://chatgpt.com/share/6aa97e1c-8750-83e9-9709-bec38bda0d31

import pygame
import grid
import pathFinding

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid.init(screen, 20, 15)
pathFinding.init()

running = True
drag_value = None
started = False

# Button
button = pygame.Rect(650, 50, 100, 50)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Start / Stop button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button.collidepoint(event.pos):
                started = not started
                continue

        # Start drag
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            col = x // grid.CELL_SIZE
            row = y // grid.CELL_SIZE

            if 0 <= row < len(grid.gridData) and 0 <= col < len(grid.gridData[row]):
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

    # Only run pathfinding when started
    if started:
        pathFinding.run()

    grid.draw()

    # Draw button
    pygame.draw.rect(screen, (100, 100, 100), button)

    font = pygame.font.Font(None, 28)
    text = "Stop" if started else "Start"
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
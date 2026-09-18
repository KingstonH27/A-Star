# Chatgpt was used for the pygame elements

import pygame
import grid
import pathFinding
import controls
import os
import sys

pygame.init()

width = controls.width
height = controls.height

# Grid size + UI panel
PANEL_WIDTH = 200
WIDTH = width * grid.CELL_SIZE + PANEL_WIDTH
HEIGHT = height * grid.CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid.init(screen, width, height)
pathFinding.init(width, height)

drag_value = None
heuristic = "Manhattan"

# Buttons
button = pygame.Rect(width * grid.CELL_SIZE + 40, 50, 120, 50)
step_button = pygame.Rect(width * grid.CELL_SIZE + 40, 120, 120, 50)
heuristic_button = pygame.Rect(width * grid.CELL_SIZE + 40, 190, 120, 50)
showPaths_button = pygame.Rect(width * grid.CELL_SIZE + 40, 260, 120, 50)
restart_button = pygame.Rect(width * grid.CELL_SIZE + 40, 330, 120, 50)

font = pygame.font.Font(None, 28)
big_font = pygame.font.Font(None, 36)

while controls.running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            controls.running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # Start / Stop
            if button.collidepoint(event.pos):
                controls.started = not controls.started
                continue

            # Step
            if step_button.collidepoint(event.pos):
                controls.started = True
                pathFinding.run()
                controls.started = False
                controls.step += 1
                continue

            # Heuristic
            if heuristic_button.collidepoint(event.pos):
                heuristic = "Euclidean" if heuristic == "Manhattan" else "Manhattan"
                pathFinding.heuristic = heuristic
                continue

            # Show all paths
            if showPaths_button.collidepoint(event.pos):
                controls.showAllPaths = not controls.showAllPaths
                continue

            # Restart
            if restart_button.collidepoint(event.pos):
                pygame.quit()
                os.execl(sys.executable, sys.executable, *sys.argv)

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

    # Run continuously
    if controls.started:
        pathFinding.run()
        controls.step += 1

    # Background
    screen.fill((30, 30, 30))

    # Grid
    grid.draw()

    # Panel
    panel_x = width * grid.CELL_SIZE
    pygame.draw.rect(screen, (45, 45, 45), (panel_x, 0, PANEL_WIDTH, HEIGHT))

    # Title
    title = big_font.render("Pathfinding", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(panel_x + PANEL_WIDTH // 2, 20)))

    # Step counter
    step_text = font.render(f"Step: {controls.step}", True, (255, 255, 255))
    screen.blit(step_text, step_text.get_rect(center=(panel_x + 100, 440)))

    # Path length
    pathLengthText = font.render(
        f"Path Length: {controls.pathLength}",
        True,
        (255, 255, 255)
    )
    screen.blit(
        pathLengthText,
        pathLengthText.get_rect(center=(panel_x + 100, 540))
    )

    # No path
    pathNotFoundText = font.render(
        f"No Path: {controls.pathNotFound}",
        True,
        (255, 255, 255)
    )
    screen.blit(
        pathNotFoundText,
        pathNotFoundText.get_rect(center=(panel_x + 100, 480))
    )

    # Buttons
    pygame.draw.rect(screen, (80, 80, 80), button, border_radius=8)
    pygame.draw.rect(screen, (80, 80, 80), step_button, border_radius=8)
    pygame.draw.rect(screen, (80, 80, 80), heuristic_button, border_radius=8)
    pygame.draw.rect(screen, (80, 80, 80), showPaths_button, border_radius=8)
    pygame.draw.rect(screen, (80, 80, 80), restart_button, border_radius=8)

    # Start / Stop
    text = "Stop" if controls.started else "Start"
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, text_surface.get_rect(center=button.center))

    # Step
    text_surface = font.render("Step", True, (255, 255, 255))
    screen.blit(text_surface, text_surface.get_rect(center=step_button.center))

    # Heuristic
    text_surface = font.render(heuristic, True, (255, 255, 255))
    screen.blit(
        text_surface,
        text_surface.get_rect(center=heuristic_button.center)
    )

    # Show all paths
    text = "Paths: ON" if controls.showAllPaths else "Paths: OFF"
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(
        text_surface,
        text_surface.get_rect(center=showPaths_button.center)
    )

    # Restart
    text_surface = font.render("Restart", True, (255, 255, 255))
    screen.blit(
        text_surface,
        text_surface.get_rect(center=restart_button.center)
    )

    pygame.display.flip()
    clock.tick(400)

pygame.quit()
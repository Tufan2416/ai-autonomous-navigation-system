# simulation.py — Pygame simulation window and rendering

import pygame
import sys
import os
import time
from config import *

def draw_grid(screen, grid, path, visited, agent_pos, start, goal):
    """Render all grid elements to the screen."""
    rows, cols = grid.shape

    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pos = (r, c)

            if grid[r][c] == 1:
                color = BLACK           # obstacle
            elif pos == start:
                color = GREEN           # start
            elif pos == goal:
                color = RED             # goal
            elif pos == agent_pos:
                color = YELLOW          # agent
            elif pos in path:
                color = BLUE            # planned path
            elif pos in visited:
                color = CYAN            # explored cells
            else:
                color = WHITE           # free cell

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)  # grid lines

def run_simulation(grid, path, visited, agent, start, goal, save_screenshot=True):
    """Main simulation loop."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("AI Autonomous Navigation System")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 14)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    screenshot_count = 0
    start_time = time.time()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen, grid, set(path) if path else set(),
                  visited, agent.position, start, goal)

        # HUD — stats overlay
        elapsed = round(time.time() - start_time, 1)
        status = "GOAL REACHED!" if agent.is_done() else "Navigating..."
        info = f"Steps: {agent.steps_taken}  |  Time: {elapsed}s  |  {status}"
        label = font.render(info, True, (0, 0, 0))
        screen.blit(label, (5, 5))

        pygame.display.flip()

        # Move agent
        if not agent.is_done():
            agent.move()
        else:
            # Save final screenshot
            if save_screenshot:
                path_img = os.path.join(OUTPUT_DIR,
                    f"final_run_{screenshot_count}.png")
                pygame.image.save(screen, path_img)
                print(f"Screenshot saved: {path_img}")
                screenshot_count += 1
            pygame.time.wait(2000)
            running = False

        clock.tick(FPS)

    pygame.quit()
    return agent.steps_taken, time.time() - start_time
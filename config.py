# config.py — Central configuration for the simulation

# Grid settings
GRID_ROWS = 20
GRID_COLS = 20
CELL_SIZE = 35  # pixels per cell

# Window size
WINDOW_WIDTH = GRID_COLS * CELL_SIZE
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE

# Colors (RGB)
WHITE  = (255, 255, 255)   # free cell
BLACK  = (20,  20,  20)    # obstacle
GRAY   = (180, 180, 180)   # grid lines
BLUE   = (30,  144, 255)   # path
GREEN  = (50,  205, 50)    # start
RED    = (220, 20,  60)    # goal
YELLOW = (255, 215, 0)     # agent
CYAN   = (0,   255, 255)   # visited cells

# Simulation settings
FPS = 10               # frames per second (agent speed)
OBSTACLE_DENSITY = 0.25  # 25% of cells are obstacles

# Output
OUTPUT_DIR = "outputs/screenshots"
RESULTS_FILE = "outputs/results.txt"
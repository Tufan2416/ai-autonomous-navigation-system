# main.py — Entry point for the AI Autonomous Navigation System

from config import GRID_ROWS, GRID_COLS, OBSTACLE_DENSITY
from src.grid   import create_grid, place_start_goal
from src.astar  import astar
from src.agent  import Agent
from src.simulation import run_simulation
from src.utils  import save_results, save_path_csv

def main():
    print("=" * 50)
    print("  AI-Based Autonomous Navigation System")
    print("=" * 50)

    # Step 1: Create the environment grid
    print("\n[1] Creating grid environment...")
    grid = create_grid(GRID_ROWS, GRID_COLS, OBSTACLE_DENSITY)
    start, goal = place_start_goal(grid, GRID_ROWS, GRID_COLS)
    print(f"    Grid: {GRID_ROWS}x{GRID_COLS} | Start: {start} | Goal: {goal}")

    # Step 2: Run A* path planning
    print("\n[2] Running A* path planning...")
    path, visited = astar(grid, start, goal, GRID_ROWS, GRID_COLS)

    if path is None:
        print("    ERROR: No path found! Try reducing obstacle density.")
        return
    print(f"    Path found! Length: {len(path)} steps")
    print(f"    Cells explored: {len(visited)}")

    # Step 3: Create agent
    agent = Agent(start)
    agent.set_path(path)

    # Step 4: Run simulation
    print("\n[3] Launching Pygame simulation...")
    steps, elapsed = run_simulation(grid, path, visited, agent, start, goal)

    # Step 5: Save outputs
    print("\n[4] Saving results...")
    save_results(steps, elapsed, len(path), GRID_ROWS)
    save_path_csv(path)

    print("\n✅ Navigation complete!")
    print(f"   Total steps: {steps}")
    print(f"   Time taken:  {round(elapsed, 2)} seconds")

if __name__ == "__main__":
    main()
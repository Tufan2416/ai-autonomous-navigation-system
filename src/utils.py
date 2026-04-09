# utils.py — Logging and helper functions

import os
import csv
from config import RESULTS_FILE

def save_results(steps, elapsed, path_length, grid_size):
    """Save run statistics to a text file."""
    os.makedirs("outputs", exist_ok=True)
    with open(RESULTS_FILE, "a") as f:
        f.write(f"Grid: {grid_size}x{grid_size} | "
                f"Path Length: {path_length} | "
                f"Steps: {steps} | "
                f"Time: {round(elapsed,2)}s\n")
    print(f"Results saved to {RESULTS_FILE}")

def save_path_csv(path):
    """Save waypoints to CSV."""
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/path_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["step", "row", "col"])
        for i, (r, c) in enumerate(path):
            writer.writerow([i, r, c])
    print("Path log saved to outputs/path_log.csv")
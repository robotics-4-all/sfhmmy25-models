#!/usr/bin/env python3
"""
Script to extract comment lines (starting with //) from all .goal files 
in the current directory and subdirectories.
"""

import os
import glob
from pathlib import Path
import re
from goal_dsl.language import build_model


def find_goal_files_glob():
    """Find all .goal files using glob pattern matching."""
    print("=== Using glob.glob() ===")
    goal_files = glob.glob("**/*.goal", recursive=True)

    if not goal_files:
        print("No .goal files found.")
        return []

    print(f"Found {len(goal_files)} .goal file(s):")
    for file_path in sorted(goal_files):
        print(f"  - {file_path}")

    return goal_files


def find_goal_files_pathlib():
    """Find all .goal files using pathlib."""
    print("\n=== Using pathlib ===")
    current_dir = Path(".")
    goal_files = list(current_dir.rglob("*.goal"))
    
    if not goal_files:
        print("No .goal files found.")
        return []
    
    print(f"Found {len(goal_files)} .goal file(s):")
    for file_path in sorted(goal_files):
        print(f"  - {file_path}")
    
    return goal_files


def find_goal_files_os_walk():
    """Find all .goal files using os.walk()."""
    print("\n=== Using os.walk() ===")
    goal_files = []
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".goal"):
                file_path = os.path.join(root, file)
                goal_files.append(file_path)
    
    if not goal_files:
        print("No .goal files found.")
        return []
    
    print(f"Found {len(goal_files)} .goal file(s):")
    for file_path in sorted(goal_files):
        print(f"  - {file_path}")
    
    return goal_files


def process_goal_file(file_path):
    """Process a single .goal file (placeholder for your logic)."""
    model = build_model(file_path)
    entities = model.entities
    goals = model.goals

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            comment_lines = []
            for line_num, line in enumerate(lines):
                stripped_line = line.strip()
                if stripped_line.startswith("//"):
                    comment_lines.append(f"Line {line_num + 1}: {stripped_line}")

            print(f"\nProcessing: {file_path}")

            # Exclude comment lines from size and line count
            non_comment_lines = [line for line in lines if not line.strip().startswith("//")]
            non_comment_content = "".join(non_comment_lines)

            print(f"Size: {len(non_comment_content)} characters")
            print(f"Lines: {len(non_comment_lines)}")
            print(f"Comment lines: {len(comment_lines)}")
            print(f"Model size: E={len(entities)}, G={len(goals)}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    """Main function to demonstrate different approaches."""
    print(f"Current directory: {os.getcwd()}")
    print("Searching for .goal files...\n")
    
    # Method 1: Using glob
    goal_files_glob = find_goal_files_glob()
    
    # Method 2: Using pathlib (recommended)
    goal_files_pathlib = find_goal_files_pathlib()
    
    # Method 3: Using os.walk
    goal_files_os_walk = find_goal_files_os_walk()
    
    # Process files if any were found
    if goal_files_pathlib:
        print("\n" + "="*50)
        print("PROCESSING FILES")
        print("="*50)
        
        for goal_file in sorted(goal_files_pathlib):
            process_goal_file(goal_file)


if __name__ == "__main__":
    main()

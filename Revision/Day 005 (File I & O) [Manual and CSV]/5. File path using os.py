"""
File Path Problem

When using open("students.txt", "w"), Python creates the file in the
"current working directory" — the folder where the script is executed from.

If I run this script from the parent folder (e.g., Python-Starter),
the file gets created there, not inside the script's own folder.

This causes confusion because the file appears "outside" where I expect it.

To fix this, we use the 'os' module to build the file path dynamically
so the file always appears in the same folder as this script,
regardless of where the script is run from.
"""

import os
# Provides functions for interacting with the file system

script_dir = os.path.dirname(__file__)
# __file__ = full path to this script (e.g., .../Day 005/file.py)
# os.path.dirname() extracts just the folder path, removing the script name

file_path = os.path.join(script_dir, "students.txt")
# os.path.join() combines folder and filename into one valid path
# This guarantees the file is created inside script_dir

with open(file_path, "w") as file:
    file.write("Alice, 85\n")
    file.write("Bob, 92\n")
    file.write("Charlie, 78\n")

with open(file_path, "r") as file:
    text = file.read()
    print(text)
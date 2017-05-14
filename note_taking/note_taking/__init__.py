"""
Add the current location to Python's search path in order to
load modules from this directory.
"""
import sys
import os
# Get the absolute path to this file.
current_path = os.path.dirname(os.path.abspath(__file__))
# Append the current_path to the sys.path to enable module imports
# from current_path.
sys.path.append(current_path)
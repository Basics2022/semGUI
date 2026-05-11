"""
New main file, after re-arranging files into a ./src folder
"""

import sys
import os

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

from main import start_everything

if __name__ == "__main__":
    # Just import old main.py file, so that it runs
    start_everything()


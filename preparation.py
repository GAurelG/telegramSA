#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup

current_path = Path(__file__).parent
file_path = (current_path / "./Data/messages2.html").resolve()

with open(file_path) as fp:
    soup = BeautifulSoup(fp)



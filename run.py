import os
import sys
import runpy
import pygame as pg
import pygame.freetype as pgft
import json
from time import sleep
import random
import copy


exe_dir = os.path.dirname(sys.executable)

if exe_dir not in sys.path:
    sys.path.insert(0, exe_dir)

runpy.run_path(os.path.join(exe_dir, "main.py"))
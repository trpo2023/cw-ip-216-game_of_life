import pygame
import sys
from random import randint
from copy import deepcopy

FPS = 12
tile = 10
resolution = width, height = 1280, 720
w, h = width // tile, height // tile
pygame.init()
import pygame
import sys
from random import randint
from copy import deepcopy

FPS = 12
tile = 10
resolution = width, height = 1280, 720
w, h = width // tile, height // tile
pygame.init()

window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
pygame.display.set_caption("Игра 'Жизнь'")

font_main = pygame.font.SysFont('centurygothic', 100)
font_rg = pygame.font.SysFont('centurygothic', 40)
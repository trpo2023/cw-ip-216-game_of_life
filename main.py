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

running = True
while running:
    window.fill(pygame.Color('black'))
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if cf[y][x]:
                pygame.draw.rect(window, pygame.Color(color), (x * tile + 2, y * tile + 2, tile - 2, tile - 2))
            nf[y][x] = cell_status(cf, x, y)
    cf = deepcopy(nf)
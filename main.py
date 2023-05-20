import pygame
import sys
from cs_func import cell_status
from dl_func import draw_label
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

def game_scene(cf, nf, color):
    running = True
    while running:
        window.fill(pygame.Color('black'))
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                if cf[y][x]:
                    pygame.draw.rect(window, pygame.Color(color), (x * tile + 2, y * tile + 2, tile - 2, tile - 2))
                nf[y][x] = cell_status(cf, x, y)
        cf = deepcopy(nf)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pygame.display.flip()
        clock.tick(FPS)
    return running

def main_menu():
    c1 = randint(30, 44)
    c2 = randint(14, 24)
    nf = [[0 for i in range(w)] for j in range(h)]
    cf = [[randint(0, 1) for i in range(w)] for j in range(h)]
    cf1 = [[1 if not i % c1 else 0 for i in range(w)] for j in range(h)]
    cf2 = [[1 if not (i * (j*4)) % c2 else 0 for i in range(w)] for j in range(h)]
    while True:
        window.fill(pygame.Color('black'))
        draw_label("Игра 'Жизнь'", font_main, pygame.Color('white'), window, 330, 170)
        draw_label('Random', font_rg, pygame.Color('orange'), window, 190, 430)
        draw_label('Game', font_rg, pygame.Color('orange'), window, 205, 480)

        draw_label('Waves', font_rg, pygame.Color('skyblue'), window, 560, 465)

        draw_label('Football', font_rg, pygame.Color('green'), window, 890, 430)
        draw_label('Yard', font_rg, pygame.Color('green'), window, 920, 480)

        button_rg = pygame.draw.rect(window, pygame.Color('gray'), (150, 370, 250, 250), 10, 15)
        button_p1 = pygame.draw.rect(window, pygame.Color('gray'), (500, 370, 250, 250), 10, 15)
        button_p2 = pygame.draw.rect(window, pygame.Color('gray'), (850, 370, 250, 250), 10, 15)

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and button_rg.collidepoint((mx, my)):
                if event.button == 1:
                    game_scene(cf, nf, 'orange')
            if event.type == pygame.MOUSEBUTTONDOWN and button_p1.collidepoint((mx, my)):
                if event.button == 1:
                    game_scene(cf1, nf, 'skyblue')
            if event.type == pygame.MOUSEBUTTONDOWN and button_p2.collidepoint((mx, my)):
                if event.button == 1:
                    game_scene(cf2, nf, 'green')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)
    return type(cf)

if __name__ == '__main__':
    main_menu()

import pygame
import sys


def draw_base():
    screen.blit(base, (base_x_pos, 650))
    screen.blit(base, (base_x_pos + 432, 650))


pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (432, 768))

base = pygame.image.load('assets/base.png').convert()
base = pygame.transform.scale2x(base)
base_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # background_image
    screen.blit(bg_surface, (0, 0))

    # Moving Floor
    base_x_pos -= 1
    draw_base()
    if (base_x_pos <= -432):
        base_x_pos = 0

    pygame.display.update()
    clock.tick(120)

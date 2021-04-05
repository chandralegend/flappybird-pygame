import pygame
import sys
import random


def draw_base():
    screen.blit(base_surface, (base_x_pos, 450))
    screen.blit(base_surface, (base_x_pos + 288, 450))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(350, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(350, random_pipe_pos - 150))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    return pipes


def remove_pipes(pipes):
    for pipe in pipes:
        if pipe.centerx <= -300:
            pipes.remove(pipe)
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            # print("Collision with Pipe")
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        # print("Collision on Ground or Ceiling")
        return False

    return True


pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0
pipe_speed = 3
game_active = True

# Assets loading
bg_surface = pygame.image.load('assets/background-night.png').convert()

base_surface = pygame.image.load('assets/base.png').convert()
base_x_pos = 0

bird_surface = pygame.image.load('assets/redbird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center=(50, 256))

pipe_surface = pipe_surface = pygame.image.load('assets/pipe-red.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 800)
pipe_height = [200, 300, 400]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # background_image
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        pipe_list = remove_pipes(pipe_list)
        draw_pipes(pipe_list)

    # Moving Floor
    base_x_pos -= 1
    draw_base()
    if (base_x_pos <= -288):
        base_x_pos = 0

    pygame.display.update()
    clock.tick(120)

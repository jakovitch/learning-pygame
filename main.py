#!/usr/bin/python

import pygame
from sys import exit
import os

WIDTH, HEIGHT = 1000, 800
PLAYER_X, PLAYER_Y = WIDTH//2, HEIGHT//2
PLAYER_WIDTH = 36
PLAYER_HEIGHT = 36
PLAYER_SPEED = 4
FRICTION = 0.4
GRAVITY = 0.5
PLAYER_VEL_X = 5
PLAYER_VEL_Y = -10
FLOOR_Y = HEIGHT * 3/4
pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer 3rd attempt")

clock = pygame.time.Clock()
player_image = pygame.image.load(os.path.join("images", "geometrydash.png"))

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = "right"
        self.jumping = False

player = Player()

def move():
    if player.direction == "left" and player.velocity_x < 0:
        player.velocity_x += FRICTION

    if player.direction == "right" and player.velocity_x > 0:
        player.velocity_x -= FRICTION
    
    else:
        player.velocity_x = 0

    player.x += player.velocity_x
    if player.x < 0:
        player.x = 0
    elif player.x + player.width > WIDTH:
        player.x = WIDTH - player.width

    player.velocity_y += GRAVITY
    player.y += player.velocity_y

    if player.y + player.height > FLOOR_Y:
        player.y = FLOOR_Y - player.height 
        player.jumping = False

def draw():
    scr.fill((84, 153, 222))
    scr.blit(player.image, (player.x, player.y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping:
        player.velocity_y = PLAYER_VEL_Y
        player.jumping = True
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.velocity_x = -PLAYER_VEL_X
        player.direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.velocity_x = PLAYER_VEL_X
        player.direction = "right"
    
    move()
    draw()
    pygame.display.update()
    clock.tick(60)


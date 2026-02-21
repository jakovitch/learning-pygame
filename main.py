#!/usr/bin/python

import pygame
from sys import exit
import os

WIDTH, HEIGHT = 1000, 800
PLAYER_X, PLAYER_Y = WIDTH//2, HEIGHT//2
PLAYER_WIDTH = 36
PLAYER_HEIGHT = 36
pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer 3rd attempt")

clock = pygame.time.Clock()
player_image = pygame.image.load(os.path.join("images", "geometrydash.png"))

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

player = Player()

def draw():
    scr.fill((84, 153, 222))
    scr.blit(player.image, (player.x, player.y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5
    
    draw()
    pygame.display.update()
    clock.tick(60)

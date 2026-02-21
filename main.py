#!/usr/bin/python

import pygame
from sys import exit
WIDTH, HEIGHT = 1000, 800
pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer 3rd attempt")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
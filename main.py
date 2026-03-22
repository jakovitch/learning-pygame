#!/usr/bin/python

import pygame
from sys import exit
import os
TILE_SIZE = 40
WIDTH, HEIGHT = 640, 640
PLAYER_X, PLAYER_Y = WIDTH//2, HEIGHT//2
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40
PLAYER_SPEED = 5
PLAYER_JUMP_WIDTH, PLAYER_JUMP_HEIGHT = 40, 40
ENEMY_WIDTH, ENEMY_HEIGHT = 40, 40
PLAYER_VEL_X = 5
PLAYER_VEL_Y = -10
GRAVITY = 0.4
FRICTION = 0.4
pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer 3rd attempt")
clock = pygame.time.Clock()


player_image_right = pygame.image.load(os.path.join("images", "geometry_dash.png"))
player_image_right = pygame.transform.scale(player_image_right, (PLAYER_WIDTH, PLAYER_HEIGHT))
pygame_tile = pygame.image.load(os.path.join("images", "geometry_dash.png"))
pygame_tile = pygame.transform.scale(pygame_tile, (TILE_SIZE, TILE_SIZE))
enemy_image_left = pygame.image.load(os.path.join("images", "geometry_dash.png"))
enemy_image_left = pygame.transform.scale(pygame_tile, (ENEMY_WIDTH, ENEMY_HEIGHT))

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right
        self.velocity_y = 0
        self.velocity_x = 0
        self.direction = "right"
        self.jumping = False

    def update_image(self):
        if self.direction == "right":
            self.image = player_image_right
        elif self.direction == "left":
            self.image = player_image_right

class Tile(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, TILE_SIZE, TILE_SIZE)
        self.image = image


def create_map():
    for i in range(4):
        tile = Tile((player.x + i*TILE_SIZE), (player.y + TILE_SIZE*2), pygame_tile)
        tiles.append(tile)

    for i in range(16):
        tile = Tile(i*TILE_SIZE, player.y + TILE_SIZE * 5, pygame_tile)
        tiles.append(tile)
        
    for i in range(3):
        tile = Tile(TILE_SIZE * 3, (i+10) * TILE_SIZE, pygame_tile)
        tiles.append(tile)



def collide():
    for tile in tiles:
        if player.colliderect(tile):
            return tile
    return None

def collide_x():
    tile = collide()
    if tile is not None:
        if player.velocity_x < 0:
            player.x = tile.x + player.width
        elif player.velocity_x > 0:
            player.x = tile.x - player.width
        player.velocity_x = 0

def collide_y():
    tile = collide()
    if tile is not None:
        if player.velocity_y < 0:
            player.y = tile.y + tile.height
        elif player.velocity_y > 0:
            player.y = tile.y - tile.height
            player.jumping = False
        player.velocity_y = 0

def move():
    if player.direction == "left" and player.velocity_x < 0:
        player.velocity_x += FRICTION
    elif player.direction == "right" and player.velocity_x > 0:
        player.velocity_x -= FRICTION
    else:
        player.velocity_x = 0
    
    player.x += player.velocity_x
    collide_x()
    player.velocity_y += GRAVITY
    player.y += player.velocity_y
    collide_y()
    if player.x < 0:
        player.x = 0
    elif player.x + player.width >WIDTH:
        player.x = WIDTH - player.width

def draw():
    scr.fill((20, 18, 167))

    player.update_image()

    for tile in tiles:
        scr.blit(tile.image, tile)

    scr.blit(player.image, player)

player = Player()
tiles = []
create_map()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

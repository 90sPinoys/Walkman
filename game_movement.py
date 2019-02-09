#!/usr/bin/env python3

import pygame
import sys
import os
from woop import Woop

'''
Objects
'''
'''
Setup
'''
worldx = 960
worldy = 720

fps = 40        # frame rate
ani = 4        # animation cycles
clock = pygame.time.Clock()
pygame.init()
main = True

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)

world = pygame.display.set_mode([worldx,worldy])
player = Woop()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 100      # how fast to move
ani = 4
'''
Main loop
'''
while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.fill(BLACK)
#    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world) #refresh player position
    pygame.display.flip()
    clock.tick(fps)

#!/usr/bin/env python3
from cd import cd
import pygame
import sys
import os
import random
from woop import Woop

'''
Objects
'''
'''
Setup
'''
worldx = 768
worldy = 500

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("home.mp3")
pygame.mixer.music.play(-1,0.0)


fps = 40        # frame rate
clock = pygame.time.Clock()
main = True

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('Backgrounds', 'mp.png'))
backdropbox = world.get_rect()
random.seed()
cd_x = []
cd_y = []
for i in range(0, 29):
    cd_x.append(random.randint(0, 200))
    cd_y.append(random.randint(4, 200))

cd = cd()   # spawn player
cd.rect.x = cd_x[0]
cd.rect.y = cd_y[0]
cd_list = pygame.sprite.Group()
cd_list.add(cd)
player = Woop()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 6      # how fast to move



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
                player.control(0, -steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

#    world.fill(BLACK)
    world.blit(backdrop, (0,220))
    cd_list.draw(world)
    player.update()
    player_list.draw(world) #refresh player position
    pygame.display.flip()
    clock.tick(fps)

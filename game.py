import pygame
import sys
import os # new code below
from woop import Woop


'''
Setup
'''
# put run-once code here
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()
world    = pygame.display.set_mode([worldx,worldy])
player = Woop()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
main = True
# backdrop = pygame.image.load(os.path.join('images','stage.png').convert())
# backdropbox = world.get_rect()


'''
Main Loop
'''
while main == True:
    world.fill(BLUE)
    player_list.draw(screen) # draw player
    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

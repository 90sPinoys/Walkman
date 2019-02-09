import pygame
import sys
import os # new code below

class Woop(pygame.sprite.Sprite):
    '''
    Spawn woop
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,2):
            img = pygame.image.load(os.path.join('Sprites','woop_walk' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey((60, 255, 0)) # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

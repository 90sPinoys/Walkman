import pygame
import sys
import os # new code below

class cd(pygame.sprite.Sprite):
    '''
    Spawn a cd
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('Sprites','cd.png')).convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey((60, 255, 0)) # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()

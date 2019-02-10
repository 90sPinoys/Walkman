import pygame
import sys
import os # new code below
from collision import Collision

class Woop(pygame.sprite.Sprite):
    '''
    Spawn woop
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.hitBox = Collision(0, 300, 175, 200)
        self.images = []
        self.leftDirection = False
        for i in range(0,8):
            img = pygame.image.load(os.path.join('Sprites','woop' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey((60, 255, 0)) # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
            

    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''
        if ( not self.hitBox.checkIntersect( self.rect.x + self.movex, self.rect.y + self.movey)):
            self.rect.x = self.rect.x + self.movex
            self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            if self.rect.x < 0:
                self.rect.x = self.rect.x - self.movex
            self.frame += 1
            self.image = self.images[(self.frame % 2) + 2]
            self.leftDirection = True            

        # moving right
        if self.movex > 0:
            if self.rect.x >= 725:
                self.rect.x = self.rect.x - self.movex
            self.frame += 1
            self.image = self.images[(self.frame % 2)]
            self.leftDirection = False

       # moving up
        if self.movey < 0:
            self.frame += 1
            if self.rect.y < 0:
                self.rect.y = self.rect.y - self.movey

            # moving up/left
            if self.leftDirection == True:
                self.image = self.images[(self.frame % 2) + 4]

            # moving up/right
            if self.leftDirection == False:
                self.image = self.images[(self.frame % 2) + 6]

        # moving down
        if self.movey > 0:
            self.frame += 1
            if self.rect.y > 348:
                self.rect.y = self.rect.y - self.movey

            # moving up/left
            if self.leftDirection == True:
                self.image = self.images[(self.frame % 2) + 4]

            # moving up/right
            if self.leftDirection == False:
                self.image = self.images[(self.frame % 2) + 6]             
                
    

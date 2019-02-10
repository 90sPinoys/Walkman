import pygame
import sys
import os # new code below
from collision import Collision

class Woop(pygame.sprite.Sprite):
    '''
    Spawn woop, and other stuff
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.isJumping = False
        self.jump = 0
        self.gravity = 3
        self.airtime = 10000
        self.hitBox = Collision(0, 500, 325, 400)
        self.hitBox2 = Collision(438, 720, 327, 400)
        self.images = []
        self.leftDirection = False
        for i in range(0,8):
            img = pygame.image.load(os.path.join('Sprites','woop' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey((60, 255, 0)) # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
            

    def jump():
        self.jump = -40

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

        
        if (not 
            (self.hitBox.checkIntersect(self.rect.x + self.movex, self.rect.y + self.movey) 
            or self.hitBox2.checkIntersect(self.rect.x + self.movex, self.rect.y + self.movey )
            )):
                 #self.rect.x = self.rect.x + self.movex
            # self.rect.y = self.rect.y + self.movey
            self.airtime -= 1
            print(str(self.rect.x) + " , " + str(self.rect.y))
            if(self.airtime > 0 or (self.gravity - self.movey > 0)):
                self.rect.y = self.rect.y + self.movey + self.jump + self.gravity
            if(self.jump < 0):
                self.jump += 1

        if(self.hitBox.checkIntersect(self.rect.x + self.movex, self.rect.y + self.movey)):
            self.airtime = 100
        self.rect.x = self.rect.x + self.movex


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
            self.airtime -= 1
            if self.airtime > 0:
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
        # if self.movey > 0:
        #     self.frame += 1
        #     if self.rect.y > 500:
        #         self.rect.y = self.rect.y - self.movey

        #     # moving up/left
        #     if self.leftDirection == True:
        #         self.image = self.images[(self.frame % 2) + 4]

        #     # moving up/right
        #     if self.leftDirection == False:
        #         self.image = self.images[(self.frame % 2) + 6]             
                
    

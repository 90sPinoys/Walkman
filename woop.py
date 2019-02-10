import pygame
import sys
import os # new code below


class Woop(pygame.sprite.Sprite):
    '''
    Spawn woop
    '''

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.isJumping = False
        self.jump = 0
        self.gravity = 3
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

    def jump():
        self.jump = -40

##    def midAir(self):
##        if self.gravity > 0:
##            return True
##        else:
##            return False
    

    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.movex

        if(self.rect.y > 250):
            self.gravity = 0 #check for collision
        else:
            self.gravity = 3
            
        self.rect.y = self.rect.y + self.movey + self.jump + self.gravity

        if(self.jump < 0):
            self.jump += 1

        # moving left
        if self.movex < 0:
            self.frame += 1
            self.image = self.images[(self.frame % 2) + 2]
            self.leftDirection = True            

        # moving right
        if self.movex > 0:
            self.frame += 1
            self.image = self.images[(self.frame % 2)]
            self.leftDirection = False

       # moving up
        if self.movey < 0:
            self.frame += 1

            # moving up/left
            if self.leftDirection == True:
                self.image = self.images[(self.frame % 2) + 4]

            # moving up/right
            if self.image == False:
                self.image = self.images[(self.frame % 2) + 6]
        

             
                
    

import pygame
import sys
import os

class Collision(pygame.sprite.Sprite):

    def __init__(self, x1 ,x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def checkIntersect(self, x, y):
        return (x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2)

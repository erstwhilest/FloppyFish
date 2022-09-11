import pygame, math
from pygame.locals import *

image_up = pygame.image.load("fish up.png")
image_down = pygame.image.load("fish down.png")
cooked_fish = pygame.image.load("cooked fish.png")

SPEEDUP = 6

class Player:
    def __init__(self):
        self.location = (0,0)
        self.velx = 0
        self.vely = 0
        self.accely = .1
        self.dead = False
        self.rect = pygame.Rect(self.location[0], self.location[1], 140, 92)

    def render(self, surface):
        if self.vely < 5:
            self.vely += self.accely
        self.location = (self.location[0]+self.velx,self.location[1]+self.vely)
        if self.dead:
            image = cooked_fish
        else:
            if self.vely <= 0:
                image = image_up
            else:
                image = image_down
        surface.blit(pygame.transform.scale(image, (148, 92)), self.location)

    def collision(self, objects):
        global SPEEDUP
        bottom = self.rect.height + self.location[1]
        left = self.location[0]
        right = self.location[0] + self.rect.width
        for object in objects:
            touch_bottom = bottom > object.rect.y
            touch_left = left < (object.rect.x + object.rect.width)
            touch_right = right > object.rect.x
            if touch_bottom and touch_left and touch_right:
                if object.name == "grill":
                    self.vely = 0
                    self.velx = 0
                    self.accely = 0
                    self.dead = True
                elif object.name == "floor":
                    self.vely = -7
                elif object.name == "beach":
                    self.location = (0, 0)
                    SPEEDUP += 2

class Obstacle:
    def __init__(self, x, y, w, h, name):
        self.rect = pygame.Rect(x, y, w, h)
        self.name = name
        self.velx = 6

    def render(self, surface, image):
        surface.blit(image, (self.rect.x, self.rect.y))
        
    def animate(self, surface, image1, image2, time):
        if (time//1)%2 == 1:
            surface.blit(image1, (self.rect.x, self.rect.y))
        else:
            surface.blit(image2, (self.rect.x, self.rect.y))
            
    def move(self):
        if self.rect.x < 0:
            self.velx = SPEEDUP
        if self.rect.x + self.rect.width > 1520:
            self.velx = -SPEEDUP
        self.rect.x += self.velx
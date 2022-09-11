import pygame
from pygame.locals import *
from player import *

pygame.init()
screen = pygame.display.set_mode((1920, 720))
pygame.display.set_caption("Floppy Fish")
clock = pygame.time.Clock()

fish = Player()
floor = Obstacle(0, 600, 1920, 10, "floor")
grill = Obstacle(700, 500, 100, 100, "grill")
beach = Obstacle(1520, 590, 400, 10, "beach")
grill_image = pygame.image.load("grill.png")

grill_image = pygame.transform.scale(grill_image, (100, 100)).convert_alpha()
objects = [floor, grill, beach]
you_died = pygame.image.load("cooked.png").convert_alpha()
background = Obstacle(0, 0, 1920, 720, "bg")
b1 = pygame.image.load("beach1.png").convert()
b2 = pygame.image.load("beach2.png").convert()

heldL = False
heldR = False
time = -1000

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            heldR = True
        else:
            heldR = False
        if keys[pygame.K_LEFT]:
            heldL = True
        else:
            heldL = False
    if fish.dead == False:
        if heldL:
            fish.velx = -3
        elif heldR:
            fish.velx = 3
        else:
            fish.velx = 0
            
    background.animate(screen, b1, b2, time)

    fish.render(screen)

    grill.move()
    grill.render(screen, grill_image)

    fish.collision(objects)
    if fish.dead:
        screen.blit(you_died, (0, 0))

    pygame.display.update()
    clock.tick(60)
    time += 1/(clock.get_fps()+.01)

import pygame
import sys
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Drawing')
FPS = 60
fpsClock = pygame.time.Clock()

red = (255, 0, 0)
white = (255, 255, 255)

screen.fill(white)
rect = pygame.draw.rect(screen, red, (200, 150, 100, 50))

autox = 10
autoy = 10
direction = 'left'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
import pygame, sys,os
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((550, 400))
pygame.display.set_caption('Jas Fasola')
moja_grafika = pygame.image.load('jas.png')
screen = pygame.display.get_surface()
screen.fill((255, 255, 255))
screen.blit(moja_grafika, (50,50))
pygame.display.flip()

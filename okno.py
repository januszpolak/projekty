import pygame, sys
from pygame import *
pygame.init()

pygame.display.set_mode((800,600))
pygame.display.set_caption('Pierwsze okno')
image = pygame.image.load('jas.png')
pygame.display.flip()

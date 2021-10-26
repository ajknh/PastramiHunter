## main py game file
import pygame
import random

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pastrami Hunter')
exitgame = False

while not exitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
    pygame.display.update()
pygame.quit()
quit()

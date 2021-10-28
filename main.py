## main py game file
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pastrami Hunter')
exitgame = False

while not exitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
    gameDisplay.fill(BLACK)
    pygame.display.flip()
pygame.quit()
quit()

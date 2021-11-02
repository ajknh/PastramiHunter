## main py game file
import pygame
import random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PASCOLOR = (199, 121, 121)

# add font
gameFont = pygame.font.Font('PressStart2P.ttf', 25)

gameDisplay = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Pastrami Hunter')

exitgame = False

while not exitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
            
    # --- Game logic should go here

    # --- Screen-clearing code goes here
    
    gameDisplay.fill(BLACK)
    # add lines on outside
    pygame.draw.line(gameDisplay, WHITE, [100, 100], [1100, 100], 5)
    pygame.draw.line(gameDisplay, WHITE, [100, 550], [1100, 550], 5)
    pygame.draw.line(gameDisplay, WHITE, [102, 100], [102, 550], 5)
    pygame.draw.line(gameDisplay, WHITE, [1098, 552], [1098, 102], 5)

    # add text to screen
    titletxt = gameFont.render("Pastrami Hunter", True, PASCOLOR)
    gameDisplay.blit(titletxt, (400, 40))
        
    pygame.display.flip()
pygame.quit()
quit()


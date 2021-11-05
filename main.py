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
    pygame.draw.line(gameDisplay, WHITE, [1098, 100], [1098, 550], 5)
    # add inside box
    pygame.draw.rect(gameDisplay, WHITE, (525, 250, 150, 150), 5)

    # Add images
    rantaOpen = pygame.image.load('ranta_open.png')
    rantaClosed = pygame.image.load('ranta_closed.png')
    # resize ranta
    rantaOpen = pygame.transform.scale(rantaOpen, (63.5, 87))
    rantaClosed = pygame.transform.scale(rantaClosed, (63.5, 87))

    def loadImages(rx, ry):
        while True:
            gameDisplay.blit(rantaOpen, (rx,ry))
            time.sleep(1)
            gameDisplay.blit(rantaClosed, (rx,ry))
    loadImages()

    
    # add text to screen
    titletxt = gameFont.render("Pastrami Hunter", True, PASCOLOR)
    gameDisplay.blit(titletxt, (400, 40))
        
    pygame.display.flip()
pygame.quit()
quit()


## main py game file
import pygame
import random
import time
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PASCOLOR = (199, 121, 121)

# add font
gameFont = pygame.font.Font('PressStart2P.ttf', 25)

screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption('Pastrami Hunter')

exitgame = False

# pastrami image is main player for now, we will change later
meatImg = pygame.image.load('pastrami.png')
meatImg = pygame.transform.scale(meatImg, (140, 90))
meatX = 110
meatY = 110

# Add images
rantaOpen = pygame.image.load('ranta_open.png')
rantaClosed = pygame.image.load('ranta_closed.png')
# resize ranta
rantaOpen = pygame.transform.scale(rantaOpen, (64, 87))
rantaClosed = pygame.transform.scale(rantaClosed, (64, 87))

def loadImages(rx, ry):
    screen.blit(meatImg, (meatX, meatY))
    #while True:
        #screen.blit(rantaOpen, (rx,ry))
        #time.sleep(1)
        #screen.blit(rantaClosed, (rx,ry))
        
while not exitgame:
    pkeys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = True
        # if player presses key 
        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                #meatX -= 10
                #screen.blit(meatImg, (meatX, meatY))
            #elif event.key == pygame.K_UP or event.key == pygame.K_w:
                #meatY -= 10
                #screen.blit(meatImg, (meatX, meatY))
            #elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #meatY += 10
                #screen.blit(meatImg, (meatX, meatY))
            #elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                #meatX += 10
                #screen.blit(meatImg, (meatX, meatY))
        # above causes buggy movement when first pressing a key to hold
        # also pretty redundant
    # if player holds down key
    pkeys = pygame.key.get_pressed()
    if pkeys[pygame.K_LEFT] or pkeys[pygame.K_a]:
        meatX -= 1
        screen.blit(meatImg, (meatX, meatY))
        time.sleep(0.02)
    elif pkeys[pygame.K_UP] or pkeys[pygame.K_w]:
        meatY -= 1
        screen.blit(meatImg, (meatX, meatY))
        time.sleep(0.02)
    elif pkeys[pygame.K_DOWN] or pkeys[pygame.K_s]:
        meatY += 1
        screen.blit(meatImg, (meatX, meatY))
        time.sleep(0.02)
    elif pkeys[pygame.K_RIGHT] or pkeys[pygame.K_d]:
        meatX += 1
        screen.blit(meatImg, (meatX, meatY))
        time.sleep(0.02)
            
    # --- Game logic should go here

    # --- Screen-clearing code goes here
    
    screen.fill(BLACK)

    # add start screen
    # add lines on outside
    pygame.draw.line(screen, WHITE, [100, 100], [1100, 100], 5)
    pygame.draw.line(screen, WHITE, [100, 550], [1100, 550], 5)
    pygame.draw.line(screen, WHITE, [102, 100], [102, 550], 5)
    pygame.draw.line(screen, WHITE, [1098, 552], [1098, 102], 5)
    # add inside box
    pygame.draw.rect(screen, WHITE, (525, 250, 150, 150), 5)
    
    loadImages(565, 280)
    # add text to screen
    titletxt = gameFont.render("Pastrami Hunter", True, PASCOLOR)
    screen.blit(titletxt, (400, 40))
        
    pygame.display.flip()
pygame.quit()
quit()

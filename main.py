## main py game file
impot pygame
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
playerImgX = 180
playerImgY = 225
playerImg = pygame.image.load('Cyan.png')
playerImg = pygame.transform.scale(playerImg, (playerImgX, playerImgY))
playerX = 110
playerY = 110

# Add images
rantaOpen = pygame.image.load('ranta_open.png')
rantaClosed = pygame.image.load('ranta_closed.png')
# resize ranta
rantaOpen = pygame.transform.scale(rantaOpen, (64, 87))
rantaClosed = pygame.transform.scale(rantaClosed, (64, 87))

def loadImages(rx, ry):
    screen.blit(playerImg, (playerX, playerY))
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
    speed = 0.2
    if pkeys[pygame.K_LEFT] or pkeys[pygame.K_a]:
        playerX -= speed
        if touching_wall():
            playerX = 100
        screen.blit(playerImg, (playerX, playerY))
        time.sleep(0.0)
    if pkeys[pygame.K_UP] or pkeys[pygame.K_w]:
        playerY -= speed
        if touching_wall():
            playerY = 100
        screen.blit(playerImg, (playerX, playerY))
        time.sleep(0.0)
    if pkeys[pygame.K_DOWN] or pkeys[pygame.K_s]:
        playerY += speed
        if touching_wall():
            playerY = 550 - playerImgY
        screen.blit(playerImg, (playerX, playerY))
        time.sleep(0.0)
    if pkeys[pygame.K_RIGHT] or pkeys[pygame.K_d]:
        playerX += speed
        if touching_wall():
            playerX = 1100 - playerImgX
        screen.blit(playerImg, (playerX, playerY))
        time.sleep(0.00)
    
    # --- Game logic should go here
    def touching_wall():
        if playerX < 100:
            return True
        elif playerY < 100:
            return True
        elif playerY + playerImgY > 550:
            return True
        elif playerX + playerImgX > 1100:
            return True
        # numbers are wall coordinates, playerImg variables for potentially
        # varying player image sizes in the future
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

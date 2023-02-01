#Import pygame library
import pygame

#Import Paddle & Ball Class
from BlockBreaker_paddle import Paddle
from BlockBreaker_ball import Ball
from BlockBreaker_block import Block

#Initialize pygame 
pygame.init()
 
#Define the colours used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 175, 175)
DARKPINK = (155, 102, 178)
MAGENTA = (255, 51, 153)
PURPLE = (204, 153 ,255)
DARKPURPLE = (178, 102, 255)
 
#Opens new window
size = (850, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("-Block Breaker-")

#Define starting score and lives
score = 0
lives = 3
 
#Create paddle
paddle = Paddle(DARKPURPLE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560
 
#Create ball
ball = Ball(PURPLE,10,10)
ball.rect.x = 345
ball.rect.y = 190

#Create blocks 
all_blocks = pygame.sprite.Group()

#Sprites List
all_sprites_list = pygame.sprite.Group()

#Creates 7 blocks in a row with 3 different rows
for i in range(7):
    block = Block(MAGENTA, 80, 30)
    block.rect.x = 60 + i * 100
    block.rect.y = 60
    all_sprites_list.add(block)
    all_blocks.add(block)
for i in range(7):
    block = Block(DARKPINK, 80, 30)
    block.rect.x = 60 + i * 100
    block.rect.y = 100
    all_sprites_list.add(block)
    all_blocks.add(block)
for i in range(7):
    block = Block(PINK, 80, 30)
    block.rect.x = 60 + i * 100
    block.rect.y = 140
    all_sprites_list.add(block)
    all_blocks.add(block)
 

#Add paddle and ball to sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
 
#Loop runs until player exits
keepPlaying = True
 
#Clock times updates on screen
clock = pygame.time.Clock()
 
#Main
while keepPlaying:

    #Main event loop
    for event in pygame.event.get():

	#Game quits if clicked closed
        if event.type == pygame.QUIT: 
              keepPlaying = False
 
    #Keys to move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
    all_sprites_list.update()
 
    #Check if the ball hits a wall
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 5 seconds
            font = pygame.font.SysFont('Comic Sans MS', 75)
            text = font.render("GAME OVER :(", 1, BLACK)
            screen.blit(text, (150,250))
            pygame.display.flip()
            pygame.time.wait(5000)
 
            #Exits game
            keepPlaying = False
 
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
 
    #Ball bounces off paddle 
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
 
    #Ball hits block
    block_collision = pygame.sprite.spritecollide(ball,all_blocks,False)
    for block in block_collision:
      ball.bounce()
      score += 1
      block.kill()
      if len(all_blocks) == 0:
           #Display Game Complete Message for 5 seconds
            font = pygame.font.SysFont('Comic Sans MS', 75)
            text = font.render("GAME COMPLETE! :D", 1, YELLOW)
            screen.blit(text, (150,250))
            pygame.display.flip()
            pygame.time.wait(5000)
 
            #Exits game
            keepPlaying = False
 
    #Makes background white
    screen.fill(WHITE)
 
    #Displays score and number of lives
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render("Score: " + str(score), 1, BLACK)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, BLACK)
    screen.blit(text, (650,10))
    all_sprites_list.draw(screen)
    pygame.display.flip()
 
    #60 frames per second
    clock.tick(60)
 
#End of loop. Quits game
pygame.quit()

#Imports and initializes pygame library
import pygame
pygame.init()

#Open a new window
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption('Pong')

#Define colours used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTPINK = (255, 153, 255)
PINK = (255, 175, 175)
BLUE = (0, 0, 255)
LIGHTBLUE = (102, 178, 255)

#Creates player 1’s paddle
class Paddle1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 75])
		self.image.fill(LIGHTPINK)
		self.rect = self.image.get_rect()
		self.points = 0

#Creates player 2’s paddle
class Paddle2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 75])
		self.image.fill(LIGHTBLUE)
		self.rect = self.image.get_rect()
		self.points = 0

#Creates bal
class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.speed = 15
		self.dx = 1
		self.dy = 1

#Places player 1’s paddle on screen
paddle1 = Paddle1()
paddle1.rect.x = 25
paddle1.rect.y = 225

#Places player 2’s paddle on screen
paddle2 = Paddle2()
paddle2.rect.x = 715
paddle2.rect.y = 225

#Speed of both paddles
paddle_speed = 15
pong = Ball()
pong.rect.x = 375
pong.rect.y = 250
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)

#Updates screen
def redraw():

	#Black screen
	screen.fill(BLACK)

#Title
	font = pygame.font.Font(None, 45)
	text = font.render('PONG', False, WHITE)
	textRect = text.get_rect()
	textRect.center = (750 // 2, 25)
	screen.blit(text, textRect)

#Player 1’s score
	p1_score = font.render(str(paddle1.points), False, PINK)
	p1Rect = p1_score.get_rect()
	p1Rect.center = (50, 50)
	screen.blit(p1_score, p1Rect)
	#Player 2’s score
	p2_score = font.render(str(paddle2.points), False, BLUE)
	p2Rect = p2_score.get_rect()
	p2Rect.center = (700, 50)
	screen.blit(p2_score, p2Rect)

	#Updates game
	all_sprites.draw(screen)

	#Displays updates
	pygame.display.update()

#Loop runs until player exits
KeepPlaying = True

#Main
while KeepPlaying:
	pygame.time.delay(80)

	#Exits Game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			KeepPlaying = False

	#Paddle controls
	key = pygame.key.get_pressed()

	#Player 1’s paddle
	if key[pygame.K_a]:
		paddle1.rect.y += -paddle_speed
	if key[pygame.K_z]:
		paddle1.rect.y += paddle_speed

	#Player 2’s paddle
	if key[pygame.K_UP]:
		paddle2.rect.y += -paddle_speed
	if key[pygame.K_DOWN]:
		paddle2.rect.y += paddle_speed

	#Moves ball
	pong.rect.x += pong.speed * pong.dx
	pong.rect.y += pong.speed * pong.dy

	#Making ball bounce off paddle and wall
	if pong.rect.y > 490:
		pong.dy = -1
	if pong.rect.y < 1:
		pong.dy = 1
	if pong.rect.x > 740:
		pong.rect.x, pong.rect.y = 375, 250
		pong.dx = -1
		paddle1.points += 1
	if pong.rect.x < 1:
		pong.rect.x, pong.rect.y = 375, 250
		pong.dx = 1
		paddle2.points += 1
	if paddle1.rect.colliderect(pong.rect):
		pong.dx = 1
	if paddle2.rect.colliderect(pong.rect):
		pong.dx = -1
	redraw()

pygame.quit()

#Imports pygame library
import pygame

#Define colour
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		#calls parent class
		super().__init__()
 
		#Create paddles
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
 
		#Draw paddle
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		self.rect = self.image.get_rect()
 
 	#Define how paddles move
	def moveLeft(self, pixels):
		self.rect.x -= pixels
		#Check if paddle is on screen
		if self.rect.x < 0:
    			self.rect.x = 0
 
	def moveRight(self, pixels):
		self.rect.x += pixels
		#Check if paddle is on screen
		if self.rect.x > 700:
			self.rect.x = 700

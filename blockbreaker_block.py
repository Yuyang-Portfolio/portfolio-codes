#Import pygame library
import pygame

#Define colour
BLACK = (0,0,0)
 
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        #Calls parent class
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        #Draw block
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

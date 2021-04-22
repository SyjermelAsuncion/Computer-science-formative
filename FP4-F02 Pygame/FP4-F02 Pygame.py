#----------------------------------------------------
#Syjer Asuncion
#Simple basic structure of game
#----------------------------------------------------

import pygame
from pygame.locals import *

WIDTH = 1000
LENGTH = 500

class Player_one:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load('block.png') #the image of the person
    
        self.block_x = 100
        self.block_y = 100

    def move_left(self): #move to the left
        self.block_x -= 10
        self.draw()

    def move_right(self): #move to the right
        self.block_x += 10
        self.draw()

    def move_up(self):  #move to the up
        self.block_y -= 10
        self.draw()

    def move_down(self):  #move to the down
        self.block_y += 10
        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5)) # background color 
        self.parent_screen.blit(pygame.transform.scale(self.block, (100, 100)), (self.block_x, self.block_y)) #to resize the image of the block
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, LENGTH))
        self.Player_one = Player_one(self.surface)
        self.Player_one.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.Player_one.move_left()

                    if event.key == K_RIGHT:
                        self.Player_one.move_right()

                    if event.key == K_UP:
                        self.Player_one.move_up()

                    if event.key == K_DOWN:
                        self.Player_one.move_down()

                elif event.type == QUIT:
                    running = False

if __name__ == '__main__':
    game = Game()
    game.run()


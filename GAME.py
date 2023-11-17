## SNAKE GAME YIPPEEE

# THIS BIT OPENS THE WINDOW FOR THE GAME TO BEGIN

import pygame
import time
import random
pygame.init()
 

# displays the window for the game
dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('*ੈ✩‧₊˚ sncak game *ੈ✩‧₊˚')

 
snake_block = 10
font = pygame.font.Font('Retro Gaming.ttf', 32)
clock = pygame.time.Clock()
snake_speed=30
 
def message(msg,color):
    mesg = font.render(msg,"#F2D492", color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

while not game_over:
    while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", "#F29559")
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    if x1 == dis_width or x1 == 0 or y1 == dis_height or y1 == 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill('#F1E3D3')
    pygame.draw.rect(dis,"#d88c9a", [x1, y1, 10, 10])
    pygame.display.update()
    
    clock.tick(30)
text = font.render('GAME OVER', True, )

pygame.quit()
quit()
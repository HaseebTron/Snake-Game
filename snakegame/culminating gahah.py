# Filename: culminating_SnakeV2.py
# Author: Abdul Haseeb, Shaharyar
# Date Created: October 23, 2018
# Description:

'''Key

lead_x=headX
lead_y=headY
blockSize=squareSize
Message_to_screen=textScreen
screen_text=displayText
snakelist=snake_list
snakeHead = snake_mouth
AppleThickness=apple_thickness
direction = angle
head=front
game_intro=game_start
Intro = start'''



#----1)Import and start pygame---------------------------------------
import pygame,sys
from pygame.locals import* 
import random

pygame.init()       # initialize the pygame engine
#----2)#Definitions: Constants and Variables-------------------------
#Constants: BLACK, BLUE, GREEN, RED, WHITE
WHITE = (255, 255, 255) # is used to get color white.
BLACK = (0,0,0) # is used to get color black.
RED = (255, 0, 0) # is used to get color red.
GREEN = (0, 255, 0) # is used to get color green.
BROWN = (238,118,33)

display_width = 800 # controls size of screen.
display_height = 800 # controls size of screen.
vineWidth = 50 # controls the sixe of the vine.
squareSize = 50 # controls size of snake.
apple_thickness = 50 # controls thickness of apple.

clock = pygame.time.Clock()
FPS = 10 # controls the speed of the snake.
angle = "right" # is the side of the snake when it starts.

#images
img_snake = pygame.image.load('snakehead.png') # loads an image of the snake head.
apple_img = pygame.image.load('apple.png') # loads image of an apple.
game_menu = pygame.image.load('game_menu.jpg') # loads the game starting menu image.
game_over = pygame.image.load('gameover.png') # loads image of game over screen. 
grass_img = pygame.image.load("grass.jpg") # loads image of grass.

#sounds
crunch = pygame.mixer.Sound("applebite2 (3).wav") # loads sound of apple being bitten.
over = pygame.mixer.Sound("Retro-game-over-sound-effect.wav") # loads game over sound.
game = pygame.mixer.Sound("Hypnotic-Puzzle3.wav") # loads starting screen and pause screen sound.

#fonts and size
small_font = pygame.font.SysFont("comicsansms", 17) 
average_font = pygame.font.SysFont("comicsansms", 25)
medium_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 80)

#text
text_a = large_font.render("Snake V2", True, GREEN)
text_b = small_font.render("-The objective of this game is to eat the apples.", True, BLACK)
text_c = small_font.render("-If you run into yourself or the vines, you die.", True, BLACK)
text_d = small_font.render("-When you eat apples you get longer", True, BLACK)
text_e = small_font.render("-Press C to play, Q to quit and P to pause.", True, BLACK)
text_f = large_font.render("Paused", True, GREEN)                                 
text_g = medium_font.render("Press C to continue or Q to quit.", True, BLACK)
text_i = average_font.render("Rules:",True, BLACK)
text_k= small_font.render("-Press p to pause the game.",True, BLACK)
text_l= average_font.render("Press Enter to start",True, BLACK)
'''text_b = average_font.render("-The Objective of this game \n is to eat the apples \n -If you run into yourself \n or the vines, you die\n -When you eat apples you \n get longer \n -Press C to play, Q to quit \n and P to pause", True, BLACK)'''

# ----- 3) Pygame commands ----------------------------------------------
# 3a) Setup pygame & screen commands
pygame.display.set_caption("Snake V2") # sets the caption of screen to Snake V2.
screen = pygame.display.set_mode(grass_img.get_size()) #use image's size to determine the window size

#---------------------------starting screen-------------------------------
def pause():        #defining pause screen
    
    paused = True
    game.play()
    
   
    
    while paused:
        # displays screen until user closes it.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            #if c is pressed then the pause screen is exited from and the game continues   
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_c:
                    paused = False
                
                #if q is pressed the game is exited     
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                                      
        screen.fill(WHITE)                  #turns the screen white
        screen.blit(text_f, (290, 0))       #displays text to temporary buffer screen
        screen.blit(text_g, (30, 100))       #displays text to temporary buffer screen
        pygame.display.flip()
        clock.tick(5) 
                    
                
#defines the score
def score(score):       
    text = average_font.render("Score: "+str(score), True, RED)
    screen.blit(text, [0,0])

#defines start menu
def game_start():
    
    keepGoing = True
    start = True
    game.play()     #plays the game sound 
    
    while start:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                start = False
                pygame.quit()
                quit()
            elif ev.type == KEYDOWN:                   
               if (ev.key == K_RETURN):
                   start = False

        #displays text to temporary buffer screen
        screen.blit(game_menu, (0,0))       #displays the game start menu image to temporary buffer screen
        screen.blit(text_a, (0, -20))
        screen.blit(text_b, (265, 310))
        screen.blit(text_c, (265, 340))
        screen.blit(text_d, (265, 370))
        screen.blit(text_k, (265, 400)) 
        screen.blit(text_i, (265, 270))
        screen.blit(text_l, (265, 430))    
        pygame.display.flip()

#defines the snake direction and location
def snake(squareSize, snake_list ):
    if angle == "right":
        front = pygame.transform.rotate(img_snake, 270) # this moves the snake right.
    if angle == "left":
        front = pygame.transform.rotate(img_snake, 90) # this moves the snake left.       
    if angle == "up":
        front = img_snake # this moves the snake  up.         
    if angle == "down":
        front = pygame.transform.rotate(img_snake, 180) # this moves the snakew down.               
        
    screen.blit(front, (snake_list[-1][0], snake_list[-1][1]))      #displays the head of snake to temporary buffer screen
    for XnY in snake_list[:-1]:
        pygame.draw.rect(screen, BLACK, [XnY[0],XnY[1],squareSize,squareSize])
        
#defines text, its colour and its size
def text_objects(text, color, size):
    if size == "small":        
        textSurface = small_font.render(text, True, color)
    elif size == "medium":        
        textSurface = medium_font.render(text, True, color)        
    elif size == "large":        
        textSurface = large_font.render(text, True, color)
        
    return textSurface, textSurface.get_rect()
    
'''def textToScreen(msg, color, yDisplace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    #displayText = my_font.render(msg, True, BLACK)
    #screen.blit(displayText, [display_width/3, display_height/3])
    textRect.center = (display_width/2), (display_height/2)+yDisplace
    screen.blit(textSurf, textRect)'''

#defines the game loop
def gameLoop ():
    global angle
    
    
    angle = "right"
    keepGoing = True
    gameOver = False
    
    #starts the snake head in the middle of the screen
    headX = display_width/2  
    headY = display_height/2
    
    headX_change = 50 
    headY_change = 0
    
    snake_list = [] # adds to the list of snake size.
    snake_size = 1 # starts the snake at 1 block.
    
    rand_apple_x = (round(random.randint(vineWidth,display_width-vineWidth-apple_thickness)/50.0))*50.0     #randomly generates the x coordinate of the apple on a grid of 50
    rand_apple_y = (round(random.randint(vineWidth,display_height-vineWidth-apple_thickness)/50.0))*50.0        #randomly generates the y coordinate of the apple on a grid of 50
    
    while keepGoing:
        
        while gameOver == True:     #game over screen
            screen.blit(game_over, (0,0))       #displays game over image to temporary buffer screen
            screen.blit(text_g, (25, 450))      #displays text to temporary buffer screen
            score(snake_size-1)
            pygame.display.flip()
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keepGoing = False       #exits the the keepGoing loop
                    gameOver = False        #exits the game over loop
                    
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_q:
                        keepGoing = False       #exits the the keepGoing loop
                        gameOver = False        #exits the game over loop
                    elif ev.key == pygame.K_c:
                        gameLoop()              #starts the gameLoop meaning the game           

        for ev in pygame.event.get():          
            if ev.type == QUIT:
                keepGoing = False
            if ev.type == pygame.KEYDOWN:
                #if the left key is pressed the snake faces the left direction and moves in that direction
                if ev.key == pygame.K_LEFT:
                    angle = "left"
                    headX_change = -squareSize
                    headY_change = 0
                #if the right key is pressed the snake faces the left direction and moves in that direction
                elif ev.key == pygame.K_RIGHT:
                    angle = "right"
                    headX_change = squareSize
                    headY_change = 0 
                #if the up key is pressed the snake faces the left direction and moves in that direction
                elif ev.key == pygame.K_UP:
                    angle = "up"
                    headY_change = -squareSize
                    headX_change = 0 
                #if the down key is pressed the snake faces the left direction and moves in that direction
                elif ev.key == pygame.K_DOWN:
                    angle = "down"
                    headY_change = squareSize
                    headX_change = 0
                #displays the pause screen if p is pressed
                elif ev.key == pygame.K_p:
                    pause()
                    
            game.stop()     #stops the game sound       
        
        if headX >= 750 or headX < 50 or headY >= 750 or headY < 50: # if snake hits the sides game over.
            gameOver = True
            over.play()
            
        
        
        headX += headX_change # when the head changes position on x axis.
        headY += headY_change # when the head changes position on y axis.
        screen.blit(grass_img, (0,0))       #displays the grass image to temporary buffer screen
        
        #pygame.draw.rect(screen, RED, [rand_apple_x,rand_apple_y,apple_thickness,apple_thickness])
 
        screen.blit(apple_img, (rand_apple_x,rand_apple_y))     #displays the apple image to temporary buffer screen
 
        snake_mouth = []
        snake_mouth.append(headX) # adds to the snake head.
        snake_mouth.append(headY) # adds to the snake head.
        snake_list.append(snake_mouth)
        
        if len(snake_list) > snake_size: # it deletes the tail of the snake every time the snake moves.
            del snake_list[0]
            
        for eachSegment in snake_list[: -1]: # if the snake hits itself gameover.
            if eachSegment == snake_mouth:
                gameOver = True
                over.play()
        
        
        
        snake(squareSize, snake_list)
        
        score(snake_size-1) # starts the score at 0.
            
        pygame.display.flip()
        
        if headX >= rand_apple_x and headX < rand_apple_x + apple_thickness: # this is used for when the snake hits the apple it eats it.
            if headY >= rand_apple_y and headY < rand_apple_y + apple_thickness: 
                rand_apple_x = (round(random.randint(vineWidth,display_width-vineWidth-apple_thickness)/50.0))*50.0
                rand_apple_y = (round(random.randint(vineWidth,display_height-vineWidth-apple_thickness)/50.0))*50.0
                snake_size += 1 # adds to the snakes size.
                crunch.play()
        
        '''if headX > rand_apple_x and headX < rand_apple_x + apple_thickness or headX + squareSize > rand_apple_x and headX +squareSize < rand_apple_x + apple_thickness:# deals with the collison on the x axis of the grid.
            if headY > rand_apple_y and headY < rand_apple_y + apple_thickness:# deals with the collison on the y axis of the grid.
                rand_apple_x = (round(random.randint(vineWidth,display_width-vineWidth-apple_thickness)/50.0))*50.0
                rand_apple_y = (round(random.randint(vineWidth,display_height-vineWidth-apple_thickness)/50.0))*50.0
                snake_size += 1                
                
                
            elif headY + squareSize > rand_apple_y and headY + squareSize < rand_apple_y + apple_thickness:# deals with the collison on the y axis of the grid.
                rand_apple_x = (round(random.randint(vineWidth,display_width-vineWidth-apple_thickness)/50.0))*50.0
                rand_apple_y = (round(random.randint(vineWidth,display_height-vineWidth-apple_thickness)/50.0))*50.0
                snake_size += 1'''                
                
            
        clock.tick(FPS)
    
    # close the window  
    pygame.quit()
    quit()

game_start()
game.stop()
gameLoop()  


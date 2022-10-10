"""ARKAPRATIM GHOSH
TECHNO MAIN SALTLAKE
CSE 10 OCTOBER 2021"""

import pygame
import random
import os
pygame.mixer.init()


pygame.init()

#colours
white=(255,255,255)
ranco=(233,190,190)
red =(255,0,0)
green=(0,255,0)
black=(0,0,0)
sh=600
sw=900
window=pygame.display.set_mode((sw,sh))#screen
#bgimg=pygame.image.load("download.jfif")
#bgimg=pygame.transform.scale(bgimg,(sw,sh)).convert_alpha()
pygame.display.set_caption("snakes")#caption
pygame.display.update()
clock=pygame.time.Clock()#game time
font=pygame.font.SysFont(None,55)
def screensc(text,color,x,y):
    sctext=font.render(text,True,color)
    window.blit(sctext,[x,y])
def plotsnk(window,color,snkl,snake_size):
    for x,y in snkl:
        pygame.draw.rect(window,black,[x,y,snake_size,snake_size])

def welcome():
    exitgame=False
    while not exitgame:
        window.fill(ranco)
        screensc("WELCOME TO SNAKE GAME",black,50,200)
        screensc("Press Enter to Play",red,50,300)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exitgame=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:

                    gameloop()
        pygame.display.update()
        clock.tick(10)
def gameloop():
    exitgame = False
    gameover = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    velocity_x = 0
    velocity_y = 0
    fruit_x = random.randint(20, sw / 2)
    fruit_y = random.randint(20, sh / 2)
    score = 0
    init_velocity = 5
    fps = 10
    snkl = []
    snk_length = 1
    if (not os .path.exists("highscore.txt")):
        with open("highscore.txt","w")as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        his = f.read()
    while not exitgame:#game loop
        if gameover:
            with open("highscore.txt", "w") as f:
                his = f.write(str(score))
            window.fill(white)

            screensc("GAME OVER, PRESS ENTER TO CONTINUE",red,50,200)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
                        gameloop()
        else:

            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key==pygame.K_q:
                        score+=10

            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-fruit_x)<6 and abs(snake_y-fruit_x)<6:
                score+=10
                print("score: ",score)
                screensc("Score: "+str(score),red,5,5)
                fruit_x = random.randint(20,sw/2)
                fruit_y = random.randint(20,sh/2)
                snk_length+=5
                if score>int(his):
                    his=score
            window.fill(green)#window colour
            #window.blit(bgimg,(0,0))
            screensc("SCORE: " + str(score)+" high score: "+str(his), red, 5, 5)
            pygame.draw.rect(window, red, [fruit_x, fruit_y, snake_size, snake_size])#fruit
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snkl.append(head)

            if len(snkl)>snk_length:

                del snkl[0]
            if head in snkl[:-1]:
                gameover=True
            if snake_x<0 or snake_x>sw or snake_y<0 or snake_y>sh:
                gameover=True
                print("Game Over")
            #pygame.draw.rect(window,white,[snake_x,snake_y,snake_size,snake_size])#snake
            plotsnk(window,white,snkl,snake_size)
        pygame.display.update()#updating screen
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
gameloop()
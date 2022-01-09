import pygame
import time
import random
import sys
pygame.init()

#to set resolution
width=600
height=600
screen = pygame.display.set_mode((width, height))

black=(0,0,0)
red =(255,0,0)
green=(0,255,0)
silver=(150,150,150)
random_color=(120,60,190)

#  front bvackground image
background_image = pygame.image.load("tic tac.jpg")
start_image = pygame.image.load("stat.jpg")
start_pos = (380, 550)
Start_Point = (382, 480, 550, 595)
image_pos = (0, 0)


gameDisplay=pygame.display.set_mode((width,height))

#to set title
pygame.display.set_caption("Tic Tac Toe")
#
clock=pygame.time.Clock()

tictacimage=pygame.image.load("tictactoe.png")


def image(Background_image, image_pos):
    screen.blit(Background_image, (image_pos[0], image_pos[1]))

def main():
    def text_objects(text,font):
        textSurface=font.render(text,True,silver)
        return textSurface,textSurface.get_rect()

    def text_objects_final(text,font):
        textSurface=font.render(text,True,random_color)
        return textSurface,textSurface.get_rect()

    def background_image():
        gameDisplay.blit(tictacimage,(0,0))

    def message_display(text,x,y):
        largeText=pygame.font.Font('freesansbold.ttf',120)
        TextSurf,TextRect=text_objects(text,largeText)
        TextRect.center=(x,y)
        gameDisplay.blit(TextSurf,TextRect)

    def show(text,*place):
        x,y=place
        message_display(text,x,y)

    ximage=pygame.image.load("tictactoe.png")
    def background_image1(x,y):
        gameDisplay.blit(ximage,(x,y))

    def msg(text):
        largeText=pygame.font.Font('freesansbold.ttf',75)
        TextSurf,TextRect=text_objects_final(text,largeText)
        TextRect.center=(300,300)
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        time.sleep(3)


    #setting resolution for all nine blocks to place text as centered
    resolution=[(100,100),(300,100),(500,100),(100,307),(300,307),(500,307),(100,510),(300,510),(500,510)]

    #initially setting the positions to -100 to look board as empty
    coordinate=[(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100)]
    

    #initially all the X or O are empty in the block
    t=[" "," "," "," "," "," "," "," "," "]

    board=[0,1,2,3,4,5,6,7,8]
    def check(char):
        if checkforwin(char,0,1,2):
            return True
        if checkforwin(char,1,4,7):
            return True
        if checkforwin(char,2,5,8):
            return True
        if checkforwin(char,6,7,8):
            return True
        if checkforwin(char,3,4,5):
            return True
        if checkforwin(char,2,4,6):
            return True
        if checkforwin(char,0,3,6):
            return True
        if checkforwin(char,0,4,8):
            return True

    def checkforwin(char,spot1,spot2,spot3):
        if board[spot1]==char and board[spot2]==char and board[spot3]==char:
            return True

    def draw():
        flag=True
        for i in range(0,9):
            if board[i]!='O' and board[i]!='X':
                flag=False
        return flag

    # tic tac toe AI using minimax algorithm
    def minimax(char):
        if char=='X':
            if check('X'):
                return 1
        else:
            if check('O'):
                return 1
        move=-1
        score=-2
        for i in range(0,9):
            if board[i]!='O' and board[i]!='X':
                board[i]=char
                if char=='X':
                    thisscore=-minimax('O')
                else:
                    thisscore=-minimax('X')
                if thisscore>score:
                    score=thisscore
                    move=i
                board[i]=i
        if move==-1:
            return 0
        return score

    #function to decide computer move which calls minimax to decide the move
    def computer_turn():
        move=-1
        score=-2
        for i in range(0,9):
            if board[i]!='O' and board[i]!='X':
                board[i]='O'
                tempscore=-minimax('X')
                board[i]=i
                if tempscore > score:
                    score=tempscore
                    move=i
        return move

    def new(l):
        if board[l]!='X' and board[l]!='O':
            board[l]='X'
            t[l]="X"
            coordinate[l]=resolution[l]          #go for user's move and check for win and draw situations
            if check('X'):
                m,n=coordinate[l]
                show('X',m,n)
                msg("You win!!")
                quit()
            if draw():
                m,n=coordinate[l]
                show('X',m,n)
                msg("It is a Draw!!")
                quit()
            opponent=computer_turn()
            board[opponent]='O'
            t[opponent]='O'
            coordinate[opponent]=resolution[opponent]
            if check('O'):
                m,n=coordinate[opponent]
                a,b=coordinate[l]
                show('X',a,b)
                show('O',m,n)
                msg("Computer Wins!")
                quit()


    #game loop
    game=True
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:          #to get cursor position on pressing of mousing
                x,y=event.pos
                if x>=0 and x<=180 and y>=0 and y<=180:      #deciding the block position on the basis of curson's position on clicking
                    new(0)
                
                elif x>=225 and x<=376 and y>=0 and y<=180:
                    new(1)

                elif x>=415 and x<=600 and y>=0 and y<=180:
                    new(2)

                elif x>=0 and x<=180 and y>=231 and y<=370:
                    new(3)

                elif x>=226 and x<=376 and y>=231 and y<=370:
                    new(4)
                
                elif x>=415 and x<=600 and y>=231 and y<=370:
                    new(5)

                elif x>=0 and x<=180 and y>=420 and y<=600:
                    new(6)

                elif x>=225 and x<=376 and y>=420 and y<=600:
                    new(7)

                elif x>=415 and x<=600 and y>=420 and y<=600:
                    new(8)

        pygame.display.update()
        gameDisplay.fill(black)
        background_image()

        x,y=coordinate[0]
        show(t[0],x,y)                      #calling all the show function for each block continusly in the loop 

        x,y=coordinate[1]
        show(t[1],x,y)

        x,y=coordinate[2]
        show(t[2],x,y)

        x,y=coordinate[3]
        show(t[3],x,y)
        
        x,y=coordinate[4]
        show(t[4],x,y)

        x,y=coordinate[5]
        show(t[5],x,y)

        x,y=coordinate[6]
        show(t[6],x,y)
        
        x,y=coordinate[7]
        show(t[7],x,y)


        x,y=coordinate[8]
        show(t[8],x,y)
        pygame.display.update()

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and Start_Point[0] <= pygame.mouse.get_pos()[0] <= Start_Point[1] and Start_Point[2] <= pygame.mouse.get_pos()[1] <= Start_Point[3]:
            main()
        clock.tick(3000000)
        
    image(background_image, image_pos)
    image(start_image, start_pos)
    # x, y = pygame.mouse.get_pos()
    # print(x , y)
    pygame.display.update()



pygame.quit()
quit()



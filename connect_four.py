import numpy as np
import pygame
import sys
import math

size_form = 100
ROW_NUM = 6
COLUMN_NUM = 7
blue = (0, 0, 255)
black = (0, 0, 0)
RADIUS = int(size_form/2 - 3)
yellow = (255, 255, 0)
pink = (200, 0, 200)

def Create_board():
    board = np.zeros([ROW_NUM,COLUMN_NUM])
    return board
board = Create_board()
print(board)



def drop_piece(board , col , row , piece):
    board[col][row] = piece



def Is_empty_place(board, col):
    return board [ROW_NUM-1][col] == 0



def next_row(board, col):
    for r in range(ROW_NUM):
        if board[r][col] == 0:
            return r


def flip_print_board(board):
    print(np.flip(board,0))

def winnin_steps(board,piece):
    #check all horizontal location for win
    for c in range (COLUMN_NUM-3):
        for r in range (ROW_NUM):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # check all vertical location for win
    for c in range (COLUMN_NUM):
        for r in range (ROW_NUM-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # check right solpe
    for c in range (COLUMN_NUM-2):
        for r in range (ROW_NUM-2):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #check left sople
    for c in range (COLUMN_NUM-3):
        for r in range ( ROW_NUM):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range (COLUMN_NUM):
        for r in range (ROW_NUM):
            pygame.draw.rect(screen, blue, (c*size_form, r*size_form+size_form, size_form,size_form))
            pygame.draw.circle(screen, black, (int(c * size_form + size_form / 2), int(r * size_form + size_form + size_form / 2)), RADIUS)

    for c in range(COLUMN_NUM):
        for r in range(ROW_NUM):
            if board[r][c] ==1:
                pygame.draw.circle(screen, pink, (int(c * size_form + size_form / 2),height- int(r * size_form + size_form / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(c * size_form + size_form / 2),height- int(r * size_form + size_form / 2)), RADIUS)
    pygame.display.update()

board = Create_board()
flip_print_board(board)
turn = 0
game_over = False

#initialize all imported pygame functions
pygame.init()

size_form =100

width = COLUMN_NUM * size_form
height = (ROW_NUM+1) * size_form

size = (width , height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("none",75)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            #to show O in the black rect
            pygame.draw.rect(screen,black,(0, 0, width, size_form))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, pink, (posx, int(size_form / 2)),RADIUS)
            else:
                pygame.draw.circle(screen, yellow, (posx, int(size_form / 2)),RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,black,(0, 0, width, size_form))

            # Ask Player 1
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/size_form))
                if Is_empty_place(board, col):
                    row = next_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winnin_steps(board, 1):
                        label = myfont.render("Player 1 Win",1,pink)
                        screen.blit(label,(40,30))
                        game_over = True
                        
            # Ask player 2

            else:
                posx = event.pos[0]
                col = int(math.floor(posx / size_form))
                if Is_empty_place(board, col):
                    row = next_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winnin_steps(board, 2):
                        label = myfont.render("Player 2 Win",2,yellow)
                        screen.blit(label,(40,30))
                        game_over=True
            flip_print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2

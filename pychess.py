#!/usr/bin/python3
import pygame, sys, os
from socket import *

from board import Board

pygame.init()
(scr_w,scr_h) = (600,600)
screen = pygame.display.set_mode((scr_w,scr_h))
g_b = Board(scr_w, scr_h) # game board obj
gamestate = 'start' 

change = True # used to detect change to board so it can be updated

selc1 = None
selc2 = None


# draws start screen and all relative assets
def draw_start_screen(str_tbox):
  #rect = pygame.draw.rect(screen, (255,255,255), ((scr_w/2) - 50, (scr_h/2) - 15, 100, 30))
  #tbox = Text_box(scr_w/2, scr_h/2, 100, 30)
  #str_tbox.draw(screen)
  pass

def text_obj(text, font):
  textSurface = font.render(text, True, (0,0,0))
  return textSurface, textSurface.get_rect()

def message_display(text, rect):
  font = pygame.font.SysFont("Times New Roman", 20)
  TextSurf, TextRect = text_obj(text, font)
  TextRect.center = (rect.center)
  screen.blit(TextSurf, TextRect)

# draws the board and all relative assets
def draw_board():
  global change
  light_c = (254,206,158)
  dark_c = (208,140,71)
  xpos = 0 # x pos of tile or piece 
  ypos = 0 # y pos of tile or piece
  odd = True
  # tile variables
  tile_c = (255,255,255) # color of tile
  tile_w = int(scr_w/8) # tile width
  tile_h = int(scr_h/8) # tile height

  if change:
    for pos in range(1, 65):
      # uses bool odd to change color of tiles in board
      if odd:
        tile_c = dark_c
        odd = not odd
      else:
        tile_c = light_c
        odd = not odd
      
      # draws tile
      pygame.draw.rect(screen, tile_c, (int(xpos), int(ypos), tile_w, tile_h), 0)
      
      # draws pieces if any on tile
      piece = g_b.get_tile(pos-1).piece
      if piece != None:
        screen.blit(piece.image, (xpos, ypos))
            
      # sets xpos and ypos to achieve checkered board affect
      xpos += scr_w/8
      if (pos)%8 == 0:
        ypos += scr_h/8
        xpos = 0
        odd = not odd # offsets the way tile color alternates 
    
    change = False

# draws the gameover screen
def draw_gameover():
  pass

def main():
  str_tbox = Text_box(scr_w//2 - 50, scr_h//2 - 30, 100, 30)

  while True:
    ''' Event Handling '''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit() 
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          pygame.quit()
          quit()
        elif event.key == pygame.K_s:
          if gamestate == 'start':
            gamestate = 'running'
        elif event.key == pygame.K_r:
          if gamestate == 'running':
            g_b.reset()
            change = True
      elif event.type == pygame.MOUSEBUTTONUP:
        mxpos, mypos = pygame.mouse.get_pos() 
        # handles move input from player while in running state
        if gamestate == 'start':
          selc1, selc2 = None, None
          #str_tbox.checkclick(self, [mxpos, mypos])
        elif gamestate == 'running':
          x = int(mxpos/((scr_w/8)))
          y = int(mypos/((scr_h/8)))
          i = x + 8*y # index of tile in board ranging from 0 to 63
          piece = g_b.board[i].piece
          if selc1 != None and selc2 == None and i != selc1:
            selc2 = i
          if selc1 == None and piece != None:
            selc1 = i
          if selc1 != None and selc2 != None and selc1 != selc2:
            g_b.move(selc1, selc2)
            change = True
            selc1, selc2 = None, None
        elif gamestate == 'gameover':
          pass

    ''' Draw Screen '''
    if gamestate == 'start':
      draw_start_screen()
    elif gamestate == 'running':
      draw_board()
    elif gamestate == 'gameover':
      draw_gameover()
    
    pygame.display.flip()

if __name__ == '__main__':
  main()


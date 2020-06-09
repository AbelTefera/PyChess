#!/usr/bin/python3
import pygame,sys, os

from board import Board
from piece import Piece

pygame.init()
(scr_w,scr_h) = (600,600)
screen = pygame.display.set_mode((scr_w,scr_h))
g_b = Board(scr_w, scr_h) # game board obj

change = True # used to detect change to board so it can be updated

selc1 = None
selc2 = None

while True:
  ##### event handling #####
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit() 
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        pygame.quit()
        quit()
    elif event.type == pygame.MOUSEBUTTONUP:
      mxpos, mypos = pygame.mouse.get_pos() 
      x = int(mxpos/((scr_w/8)))
      y = int(mypos/((scr_h/8)))
      i = x + 8*y
      piece = g_b.board[i].piece
      if selc1 != None and selc2 == None and i != selc1:
        selc2 = i
      if selc1 == None and piece != None:
        selc1 = i
      if selc1 != None and selc2 != None and selc1 != selc2:
        g_b.move(selc1, selc2)
        change = True
        selc1, selc2 = None, None

        
  ##### draws board and pieces #####
  light_c = (254,206,158)
  dark_c = (208,140,71)
  xpos = 0 # x pos of tile or piece 
  ypos = 0 # y pos of tile or piece
  odd = True 
  if change:
    for pos in range(1, 65):
      # uses bool odd to change color of tiles in board
      if odd:
        tile_c = dark_c
        odd = not odd
      else:
        tile_c = light_c
        odd = not odd
      
      pygame.draw.rect(screen, tile_c, (int(xpos), int(ypos), int(scr_w/8), int(scr_h/8)), 0)
      
      # draws pieces if any on tile
      piece = g_b.board[pos-1].piece
      if piece != None:
        #import pdb; pdb.set_trace()
        screen.blit(piece.image, (xpos, ypos))
            
      # sets xpos and ypos to achieve checkered board affect
      xpos += scr_w/8
      if (pos)%8 == 0:
        ypos += scr_h/8
        xpos = 0
        odd = not odd
  change = False
 
  pygame.display.flip()


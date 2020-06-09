#!/usr/bin/python3
import pygame,sys, os
from socket import *

from board import Board
from piece import Piece

pygame.init()
(scr_w,scr_h) = (600,600)
screen = pygame.display.set_mode((scr_w,scr_h))
g_b = Board(scr_w, scr_h) # game board obj

# setup node for udp
serverName = '192.168.0.23'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

change = True # used to detect change to board so it can be updated
curr_player = 'W'
gamestate = 'start screen'
player2 = None

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
      if event.key == pygame.K_s:
        if gamestate == 'start screen':
          gamestate = 'running'
    elif event.type == pygame.MOUSEBUTTONUP:
      mxpos, mypos = pygame.mouse.get_pos() 
      if gamestate == 'running':
        x = int(mxpos/((scr_w/8)))
        y = int(mypos/((scr_h/8)))
        i = x + 8*y
        piece = g_b.board[i].piece
        if selc1 != None and selc2 == None and i != selc1:
          selc2 = i
        if selc1 == None and piece != None:
          selc1 = i
        if selc1 != None and selc2 != None and selc1 != selc2:
          if g_b.move(selc1, selc2, curr_player):
            if curr_player == 'W':
              curr_player = 'B'
            elif curr_player == 'B':
              curr_player = 'W'
          change = True
          selc1, selc2 = None, None

  ##### draws board and pieces #####
  if gamestate == 'start screen':
    gamestate = input('choose multi or single')
  elif gamestate == 'single':
    gamestate = 'running'
  elif gamestate == 'multi':
    player2 = input('enter ip address of player2')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    player2_state, serverAddress = clientSocket.recvfrom(2048)
    print(player2_state)
    gamestate = 'running'
  elif gamestate == 'running':
    # playing multiplayer if player2 not None

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


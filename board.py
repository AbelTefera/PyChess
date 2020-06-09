from tile import Tile
from pawn import Pawn
from king import King
from rook import Rook
from queen import Queen
from bishop import Bishop
from knight import Knight

class Board:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.board = self.new_b()
    self.curr_player = 'W'

  
  def new_b(self):
    new_b = []
    xpos = 0
    ypos = 0
    for i in range(64):
      # white
      if i == 0 or i == 7:
        new_b.append(Tile(xpos, ypos, Rook('W')))
      elif i == 1 or i == 6:
        new_b.append(Tile(xpos, ypos, Knight('W')))
      elif i == 2 or i == 5:
        new_b.append(Tile(xpos, ypos, Bishop('W')))
      elif i == 3:
        new_b.append(Tile(xpos, ypos, Queen('W')))
      elif i == 4:
        new_b.append(Tile(xpos, ypos, King('W')))
      elif i >= 8 and i <= 15:
        new_b.append(Tile(xpos, ypos, Pawn('W')))
      # black
      elif i == 56 or i == 63:
        new_b.append(Tile(xpos, ypos, Rook('B')))
      elif i == 57 or i == 62:
        new_b.append(Tile(xpos, ypos, Knight('B')))
      elif i == 58 or i == 61:
        new_b.append(Tile(xpos, ypos, Bishop('B')))
      elif i == 59:
        new_b.append(Tile(xpos, ypos, Queen('B')))
      elif i == 60:
        new_b.append(Tile(xpos, ypos, King('B')))
      elif i >= 48 and i <= 55:
        new_b.append(Tile(xpos, ypos, Pawn('B')))
      # empty
      else:
        new_b.append(Tile(xpos, ypos))

      # sets xpos and ypos
      xpos+=self.w/8
      if (i+1)%8 == 0:
        xpos = 0
        ypos += self.h/8
    return new_b
  

  # returns tile with piece if mouse clicked on it
  def collide(self, pos):
    coll = None
    if self.board[pos].piece != None:    
      coll = self.board[pos]
    return coll  
  
 
  # returns true for successful move and false otherwise
  def move(self, from_pos, dest_pos, curr_player):
    move_valid = self.is_move_valid(from_pos, dest_pos, curr_player)
    if move_valid:
      tile_from = self.collide(from_pos)
      piece = tile_from.piece
      tile_dest.piece = piece 
      tile_from.piece = None
      return True

    return False

  def get_tile(self, pos):
    return self.board[pos]

  # returns true for valid moves and false otherwise
  def is_move_valid(self, from_pos, dest_pos, curr_player):
    tile_from = self.collide(from_pos)
    tile_dest = self.get_tile(dest_pos)
    piece = tile_from.piece
    dest_piece = None
    if tile_dest.piece != None:
      dest_piece = tile_dest.piece
    valid = True
    if piece == None:
      valid = False
    elif from_pos == dest_pos:
      valid = False
    elif not piece.is_move_legal(from_pos+1, dest_pos+1):
      valid = False
    elif curr_player != piece.color:
      valid = False
    elif dest_piece != None and curr_player == dest_piece.color:
      valid = False
    
    if not valid:
      print(f'move from {from_pos+1} > {dest_pos+1} is not valid')

    return valid



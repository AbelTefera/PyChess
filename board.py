from pawn import Pawn
from king import King
from rook import Rook
from queen import Queen
from bishop import Bishop
from knight import Knight

class Board:
  def __init__(self, w, h):
    self.board = self.init_board() # list containing all tiles in board
    self.curr_player = 'W' # current player could White('W') or Black('B')
 
 
  # pos should be in range of 0 to 63
  def get_tile(self, pos):
    return self.board[pos]

  
  def switch_curr_player(self):
    if self.curr_player == 'W':
      self.curr_player = 'B'
    elif self.curr_player == 'B':
      self.curr_player = 'W'

  
  # resets board and current player
  def reset(self):
    self.board = self.init_board()
    self.curr_player = 'W'
    
    
  # returns true for successful move and false otherwise
  def move(self, from_pos, dest_pos):
    move_valid = self.is_move_valid(from_pos, dest_pos)
    if move_valid:
      # moves piece form tile_from to tile_dest
      tile_from = self.get_tile(from_pos)
      tile_dest = self.get_tile(dest_pos)
      piece = tile_from.piece
      tile_dest.piece = piece 
      tile_from.piece = None

      self.switch_curr_player()
      return True

    return False
 

  # returns true for valid moves and false otherwise
  # from_pos and dest_pos must in range 0 to 63
  def is_move_valid(self, from_pos, dest_pos):
    tile_from = self.get_tile(from_pos)
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
    elif self.curr_player != piece.color:
      valid = False
    elif dest_piece != None and self.curr_player == dest_piece.color:
      valid = False
    
    if not valid:
      print(f'move from {from_pos+1} > {dest_pos+1} is not valid')
    return valid

  
  def init_board(self):
    new_b = []
    for i in range(64):
      # white
      if i == 0 or i == 7:
        new_b.append(Tile(Rook('W')))
      elif i == 1 or i == 6:
        new_b.append(Tile(Knight('W')))
      elif i == 2 or i == 5:
        new_b.append(Tile(Bishop('W')))
      elif i == 3:
        new_b.append(Tile(Queen('W')))
      elif i == 4:
        new_b.append(Tile(King('W')))
      elif i >= 8 and i <= 15:
        new_b.append(Tile(Pawn('W')))
      # black
      elif i == 56 or i == 63:
        new_b.append(Tile(Rook('B')))
      elif i == 57 or i == 62:
        new_b.append(Tile(Knight('B')))
      elif i == 58 or i == 61:
        new_b.append(Tile(Bishop('B')))
      elif i == 59:
        new_b.append(Tile(Queen('B')))
      elif i == 60:
        new_b.append(Tile(King('B')))
      elif i >= 48 and i <= 55:
        new_b.append(Tile(Pawn('B')))
      # empty
      else:
        new_b.append(Tile())

    return new_b 


class Tile:
  def __init__(self, piece=None):
    self.piece = piece

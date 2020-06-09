from piece import Piece
from moves import *

class Rook(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img()

  def get_img(self):
    return super().get_img('R')

  def is_move_legal(self, from_pos, dest_move):
    return hor_or_vert(from_pos, dest_move)

from piece import Piece
from moves import *

class Bishop(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img()

  def get_img(self):
    return super().get_img('B')

  def is_move_legal(self, from_pos, dest_pos):
    return move_is_diagonal(from_pos, dest_pos)

from piece import Piece
from moves import *

class Queen(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img()

  def get_img(self):
    return super().get_img('Q')

  def is_move_legal(self, from_pos, dest_pos):
    valid = False
    if hor_or_vert(from_pos, dest_pos):
      valid = True
    elif move_is_diagonal(from_pos, dest_pos):
      valid = True

    return valid

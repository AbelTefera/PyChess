from piece import Piece

class Pawn(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img() 

  def get_img(self):
    return super().get_img('P')
  
  def is_move_legal(self, from_pos, dest_pos):
    if self.color == 'W':
      return dest_pos-from_pos == 8
    elif self.color == 'B':
      return dest_pos-from_pos == -8

from piece import Piece

class Knight(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img()

  def get_img(self):
    return super().get_img('N')

  def is_move_legal(self, from_pos, dest_pos):
    valid = False
    if abs(from_pos-dest_pos) == 10:
      valid = True
    elif abs(from_pos-dest_pos) == 6:
      valid = True
    elif abs(from_pos-dest_pos) == 17:
      valid = True
    elif abs(from_pos-dest_pos) == 15:
      valid = True
      
    return valid

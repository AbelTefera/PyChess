from piece import Piece

class King(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img()

  def get_img(self):
    return super().get_img('K')  

  def is_move_legal(self, from_pos, dest_pos):
    valid = False
    if abs(from_pos-dest_pos) == 8:
      valid = True
    elif abs(from_pos-dest_pos) == 1:
      valid = True
    elif abs(from_pos-dest_pos) == 7:
      valid = True
    elif abs(from_pos-dest_pos) == 9:
      valid = True

    return valid

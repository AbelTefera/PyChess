from piece import Piece

class Bishop(Piece):
  def __init__(self, color):
    super().__init__(color)
    self.image = self.get_img()

  def get_img(self):
    return super().get_img('B')

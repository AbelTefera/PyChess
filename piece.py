import pygame, os

class Piece:
  def __init__(self, color):
    self.color = color

  def get_img(self, p_name): 
    img = pygame.image.load(os.path.join(f'{self.color}_{p_name}.png'))
    return img


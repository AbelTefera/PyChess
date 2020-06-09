# list of functions that return a bool

def move_is_diagonal(from_pos, to_pos):
  if abs(to_pos-from_pos)%9 == 0:
    return True
  elif abs(to_pos-from_pos)%7 == 0:
    return True
  else:
    return False

def in_same_row(from_pos, to_pos):
 if from_pos <= 8 and to_pos <= 8:
  return True
 elif from_pos <= 16 and from_pos > 8:
  return to_pos <= 16 and to_pos > 8
 elif from_pos <= 24 and from_pos > 16:
  return to_pos <= 24 and to_pos > 16
 elif from_pos <= 32 and from_pos > 24:
  return to_pos <= 32 and to_pos > 24
 elif from_pos <= 40 and from_pos > 32:
  return to_pos <= 40 and to_pos > 32
 elif from_pos <= 48 and from_pos > 40:
  return to_pos <= 48 and to_pos > 40
 elif from_pos <= 56 and from_pos > 48:
  return to_pos <= 56 and to_pos > 48
 elif from_pos <= 64 and from_pos > 56:
  return to_pos <= 64 and to_pos > 56
 else: 
  return False

def hor_or_vert(from_pos, to_pos):
  # up or down move
  if abs(to_pos-from_pos)%8 == 0:
    return True
  elif in_same_row(from_pos, to_pos):
    return True
  else:
    return False



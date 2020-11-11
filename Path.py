import random


class ObjPath():
  def __init__(self):
     self.points = {}
     self.index = 0
     self.start_point_x = 0
     self.start_point_y = 0

  def get_point(self, current_pos_x, current_pos_y, speed):
    speed = abs(speed)

    goto_point_x = self.points['x'][self.index]
    goto_point_y = self.points['y'][self.index]
    go_up = False
    go_down = False
    go_left = False
    go_right = False
    finish_x = False
    finish_y = False

    go_right = goto_point_x >= current_pos_x
    go_left = goto_point_x <= current_pos_x
    go_down = goto_point_y >= current_pos_y
    go_up = goto_point_y <= current_pos_y

    if go_right:
        point_x = current_pos_x + speed
        if point_x >= goto_point_x:
          point_x = goto_point_x
          finish_x = True

    if go_left:
        point_x = current_pos_x - speed
        if point_x <= goto_point_x:
          point_x = goto_point_x
          finish_x = True

    if go_down:
        point_y = current_pos_y + speed
        if point_y >= goto_point_y:
          point_y = goto_point_y
          finish_y = True

    if go_up:
        point_y = current_pos_y - speed
        if point_y <= goto_point_y:
          point_y = goto_point_y
          finish_y = True

    if finish_x and finish_y:
        self.index += 1

    return (point_x, point_y)

class EnemyPath1(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 1
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [442, 654, 442, 231, 442, 654, 442, 231, 442, 654, 442, 231, 442, 654, 442, 231, 442, 654, 442, 231, 232],
                    "y": [185, 375, 563, 372, 185, 375, 563, 372, 185, 375, 563, 372, 185, 375, 563, 372, 185, 375, 563, 372, 4000]}


class EnemyPath2(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 1
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [10, 700, 700, 10, 10, 700, 442, 231, 442, 654, 442, 231, 442, 654, 442, 231, 442, 654, 442, 231, 232],
                    "y": [30, 30, 500, 500, 30, 30, 563, 372, 185, 375, 563, 372, 185, 375, 563, 372, 185, 375, 563, 372, 4000]}


class EnemyPath3(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 10
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [10, 800,  10, 50, 90, 150, 800, 10,  700, 60, 500, 850],
                    "y": [30, 800, 30, 70, 120, 300, 120, 800, 850, 10, 500, 1200]}

class EnemyPath4(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 880
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [880,  5, 700, 200, 10, 300, 333, 700],
                    "y": [10, 830, 500, 200, 10,  10, 150, 1200]}

class EnemyPath5(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 500
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [500,  5, 300,   6, 800, 700, 600, 500, 700, 600, 500, 450],
                    "y": [50, 830, 200, 800, 10,  500, 600, 500, 500, 600, 500, 1200]}

class EnemyPath6(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 100
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [100, 700, 600, 500, 10, 300, 800, 700],
                    "y": [10,  300, 500, 100, 10, 300, 150, 1200]}

class EnemyPath7(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 200
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [200,  5, 700, 200, 10, 300, 333, 700],
                    "y": [10, 830, 500, 200, 10,  10, 150, 1200]}

class EnemyPath8(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 500
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [500,  5, 400, 850, 500,   5, 700, 200,  10, 300, 333, 600, 700,  10, 300, 600],
                    "y": [10, 400, 500, 800, 100, 300, 100, 830, 500, 200,  10, 400,  10, 150, 150, 1200]}


class EnemyPath9(ObjPath):
  def __init__(self):
     super().__init__()
     self.start_point_x = 1
     self.start_point_y = random.randrange(-1100, -300)
     self.points = {"x": [1,  200, 700, 200, 10, 300, 333, 400, 850, 500, 700],
                    "y": [10, 830, 500, 200, 10,  10, 150, 100, 300, 100, 1200]}
def get_random_path(enemy_path):

    if enemy_path == 0:
        return EnemyPath1()
    elif enemy_path == 1:
        return EnemyPath2()
    elif enemy_path == 2:
        return EnemyPath3()
    elif enemy_path == 3:
        return EnemyPath4()
    elif enemy_path == 4:
        return EnemyPath5()
    elif enemy_path == 5:
        return EnemyPath6()
    elif enemy_path == 6:
        return EnemyPath7()
    elif enemy_path == 7:
        return EnemyPath8()
    elif enemy_path == 8:
        return EnemyPath9()
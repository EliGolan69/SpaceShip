from Images import *
from Const import *

class ExplosionAnimation():
  def __init__(self, engine_game, sound):
    self.engine_game, self.sound = engine_game, sound
    self.image_file_1 = "1.png"
    self.image_file_2 = "2.png"
    self.image_file_3 = "3.png"
    self.image_file_4 = "4.png"
    self.image_file_5 = "5.png"
    self.image_file_6 = "6.png"
    self.image_file_7 = "7.png"
    self.image_file_8 = "8.png"
    self.image_file_9 = "9.png"

    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_1)
    self.image_1 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_2)
    self.image_2 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_3)
    self.image_3 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_4)
    self.image_4 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_5)
    self.image_5 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_6)
    self.image_6 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_7)
    self.image_7 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_8)
    self.image_8 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_LASER_EXPLOSIONS, self.image_file_9)
    self.image_9 = image.LoadGameIamge()

    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]
    self.index = 0

  def StartAnimation(self, x, y, window):
    if self.index <= len(self.images ) -1:
      window.blit(self.images[self.index], (x, y))
      self.index += 1
      y += 2

class PlayerExplosionAnimation():
  def __init__(self, engine_game, sound):
    self.engine_game, self.sound = engine_game, sound
    self.image_file_1 = "1.png"
    self.image_file_2 = "2.png"
    self.image_file_3 = "3.png"
    self.image_file_4 = "4.png"
    self.image_file_5 = "5.png"
    self.image_file_6 = "6.png"
    self.image_file_7 = "7.png"
    self.image_file_8 = "8.png"
    self.image_file_9 = "9.png"

    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_1)
    self.image_1 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_2)
    self.image_2 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_3)
    self.image_3 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_4)
    self.image_4 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_5)
    self.image_5 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_6)
    self.image_6 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_7)
    self.image_7 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_8)
    self.image_8 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_BIG_EXPLOSIONS, self.image_file_9)
    self.image_9 = image.LoadGameIamge()

    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]
    self.index = 0

  def StartAnimation(self, x, y, window):
    if self.index <= len(self.images ) -1:
      window.blit(self.images[self.index], (x, y))
      self.index += 1
      y += 2

class RocketFlame():
  def __init__(self, engine_game):
    self.engine_game = engine_game
    self.image_file_1 = "1.png"
    self.image_file_2 = "2.png"
    self.image_file_3 = "3.png"
    self.image_file_4 = "4.png"
    self.image_file_5 = "5.png"
    self.image_file_6 = "6.png"
    self.image_file_7 = "7.png"
    self.image_file_8 = "8.png"
    self.image_file_9 = "9.png"

    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_1)
    self.image_1 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_2)
    self.image_2 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_3)
    self.image_3 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_4)
    self.image_4 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_5)
    self.image_5 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_6)
    self.image_6 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_FLAME, self.image_file_7)
    self.image_7 = image.LoadGameIamge()

    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7]
    self.index = 0

  def StartAnimation(self, x, y, window):
    if self.index <= len(self.images ) -1:
      window.blit(self.images[self.index], (x, y))
      self.index += 1
    else:
      self.index = 0

class RocketExplosionAnimation():
  def __init__(self, engine_game, sound):
    self.engine_game, self.sound = engine_game, sound
    self.image_file_1 = "1.png"
    self.image_file_2 = "2.png"
    self.image_file_3 = "3.png"
    self.image_file_4 = "4.png"
    self.image_file_5 = "5.png"
    self.image_file_6 = "6.png"
    self.image_file_7 = "7.png"
    self.image_file_8 = "8.png"
    self.image_file_9 = "9.png"

    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_1)
    self.image_1 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_2)
    self.image_2 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_3)
    self.image_3 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_4)
    self.image_4 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_5)
    self.image_5 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_6)
    self.image_6 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_7)
    self.image_7 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_8)
    self.image_8 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, IMAGE_FOLDER_ROCKET_EXPLOSIONS, self.image_file_9)
    self.image_9 = image.LoadGameIamge()
    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]
    self.index = 0

  def StartAnimation(self, x, y, window):
    if self.index == 0:
       self.sound.ExplosionsEffect()
       self.smooth_animation = 0

    if self.index <= len(self.images) -1:
      window.blit(self.images[self.index], (x-70, y-70))
      self.smooth_animation += 1
      if self.smooth_animation >= 4:
        self.index += 1
        smooth_animation = 0
      elif self.smooth_animation == 1:
        self.index += 1
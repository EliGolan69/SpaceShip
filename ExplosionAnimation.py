from Images import *
from Const import *

class Animation():
  def __init__(self, engine_game, sound, image_folder, image_off_x=0, image_off_y=0):
    self.engine_game, self.sound = engine_game, sound
    self.images = []
    self.index = 0
    self.animation_ended = False
    self.image_off_x, self.image_off_y = image_off_x, image_off_y
    image  = GameIamge(self.engine_game, image_folder, "1.png")
    self.image_1 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "2.png")
    self.image_2 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "3.png")
    self.image_3 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "4.png")
    self.image_4 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "5.png")
    self.image_5 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "6.png")
    self.image_6 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "7.png")
    self.image_7 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "8.png")
    self.image_8 = image.LoadGameIamge()
    image  = GameIamge(self.engine_game, image_folder, "9.png")
    self.image_9 = image.LoadGameIamge()

  def StartAnimation(self, x, y, window):
    if self.index <= len(self.images )-1:
      window.blit(self.images[self.index], (x + self.image_off_x, y + self.image_off_y))
      self.index += 1
      y += 2

  def AnimationEnded(self):
    return (self.index >= (len(self.images)))


class ExplosionAnimation(Animation):
  def __init__(self, engine_game, sound):
    super().__init__(engine_game, sound, IMAGE_FOLDER_LASER_EXPLOSIONS)
    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]


class PlayerExplosionAnimation(Animation):
  def __init__(self, engine_game, sound):
    super().__init__(engine_game, sound, IMAGE_FOLDER_BIG_EXPLOSIONS)
    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]


class RocketFlame(Animation):
  def __init__(self, engine_game, sound):
    super().__init__(engine_game, sound, IMAGE_FOLDER_ROCKET_FLAME)
    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7]

  def StartAnimation(self, x, y, window):
    if self.index <= len(self.images ) -1:
      window.blit(self.images[self.index], (x, y))
      self.index += 1
    else:
      self.index = 0



class RocketExplosionAnimation(Animation):
  def __init__(self, engine_game, sound):
    super().__init__(engine_game, sound, IMAGE_FOLDER_ROCKET_EXPLOSIONS)
    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]


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

  def AnimationEnded(self):
    return (self.index >= (len(self.images)-1))


class SmallExplosionAnimation(Animation):
  def __init__(self, engine_game, sound, image_off_x, image_off_y):
    super().__init__(engine_game, sound, IMAGE_FOLDER_SMALL_EXPLOSION, image_off_x, image_off_y)
    self.images = [self.image_1, self.image_2, self.image_3, self.image_4, self.image_5, self.image_6, self.image_7, self.image_8, self.image_9]

from Ships import Ship
from Weapons import Laser
from Const import ENEMY_SPEED


class Enemy(Ship):
  def __init__(self, x, y, enemy_game, ship_type, laser_type, enemy_sound, path_obj,health=100):
    super().__init__(x, y, enemy_game, ship_type, laser_type, enemy_sound,health)
    self.enemy_game = enemy_game
    self.speed = ENEMY_SPEED
    self.enemy_sound = enemy_sound
    self.path = path_obj
    self.animation_ended = False
    self.x = self.path.start_point_x
    self.y = self.path.start_point_y


  def can_destroy(self):
      return (self.animation_ended and self.exploded and not self.weapons)

  def move(self):
   # self.y += self.speed
   self.x, self.y = self.path.get_point(self.x, self.y, self.speed)

  def draw(self, window):
    if not self.exploded:
      window.blit(self.image, (self.x, self.y))
    else:
      self.explod_animation.StartAnimation(self.x, self.y, window)
      self.animation_ended = self.explod_animation.AnimationEnded()
    for weapon in self.weapons:
        weapon.draw(window)

  def shoot(self):
    if self.exploded:
      pass
    elif self.cool_down_counter == 0:
        if self.y >= 0:
          self.enemy_sound.LaserEnemyEffect()
        laser = Laser(self.x + int(self.imageWidth/2), self.y, self.enemy_game, self.weapon_type)
        self.weapons.append(laser)
        self.cool_down_counter = 1

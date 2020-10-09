from Ships import Ship
from Weapons import Laser
from Const import ENEMY_SPEED

class Enemy(Ship):
  def __init__(self, x, y, enemy_game, ship_type, laser_type, enemy_sound,health=100):
    super().__init__(x, y, enemy_game, ship_type, laser_type, enemy_sound,health)
    self.enemy_game = enemy_game
    self.speed = ENEMY_SPEED
    self.enemy_sound = enemy_sound

  def move(self):
    self.y += self.speed

  def draw(self, window):
    if not self.exploded:
      window.blit(self.image, (self.x, self.y))
    elif self.exploded:
      self.explod_animation.StartAnimation(self.x, self.y, window)

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

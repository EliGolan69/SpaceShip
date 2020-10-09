from Const import *
from Ships import *
from Weapons import *

class ExtraShip(Ship):
  def __init__(self, x, y, extra_ship_game, ship_type, weapon_type, extra_ship_sound,health=100):
    super().__init__(x, y, extra_ship_game, ship_type, weapon_type, extra_ship_sound,health)
    self.extra_ship_sound = extra_ship_sound
    self.extra_ship_game = extra_ship_game
    self.cool_down = EXTRA_SHIP_ROCKET_COOL_DOWN
    self.max_health = health
    self.extra_shot = 0
    self.speed = PLAYER_SPEED
    self.weapon_speed = 5
    self.numberOfRocket = 6

  def draw(self, window):
     if not self.exploded:
        window.blit(self.image, (self.x, self.y))
        for weapon in self.weapons:
            weapon.draw(window)

  def shoot(self):
     if self.cool_down_counter == 0:
       if self.numberOfRocket >= 0:
         weapon = Rocket(self.x + int(self.imageWidth/2), self.y, self.extra_ship_game, self.weapon_type)
         self.extra_ship_sound.RockketShipEffect()
         self.weapons.append(weapon)
         self.cool_down_counter = 1
         self.numberOfRocket -= 1

  def move_lasers(self, EnemyObjs):
    self.cooldown()
    for weapon in self.weapons:
      weapon.move(-self.weapon_speed)
      if weapon.off_screen(self.GetScreenSizeH()):
        self.weapons.remove(weapon)
      else:
        for obj in EnemyObjs:
          if weapon.collision(obj):
            obj.exploded = True
            if weapon in self.weapons:
              self.weapons.remove(weapon)
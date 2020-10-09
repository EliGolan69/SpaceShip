from Const import *
import os
from Images import GameIamge
from ExtraShips import *
from random import randrange
from random import random

class PowerUp():
  def __init__(self, x, y, power_up_game, power_up_type, power_up_sound):
    self.power_up_sound = power_up_sound
    self.x = x
    self.y = y
    self.power_up_game = power_up_game
    self.power_up_type = power_up_type
    self.PowerUp = PowerUpContainer(self.power_up_game, power_up_type)
    self.image = self.PowerUp.GetPowerUpImage()
    self.mask = self.PowerUp.GetWeaponMask()
    self.imageHeight = self.image.get_height()
    self.imageWidth = self.image.get_width()
    self.speed = POWER_UP_SPEED
    self.canDestroy = True
    self.screenWidth, self.screenHeight = self.power_up_game.display.get_surface().get_size()

  def collide(self, obj1, obj2):
      offset_x = obj2.x - obj1.x
      offset_y = obj2.y - obj1.y
      return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

  def Ability(self,obj):
    pass

  def get_width(self):
    return self.image.get_width()

  def get_height(self):
    return self.image.get_height()

  def draw(self, window):
    window.blit(self.image, (self.x, self.y))

  def move(self):
    self.y += self.speed

  def off_screen(self, height):
    return not (self.y <= height and self.y >= 0)

class PowerUpContainer():
    def __init__(self, game_power_up, power_up_type):
        self.power_up_type = power_up_type
        self.game_power_up = game_power_up
        if self.power_up_type == POWER_UP_HEALTH:
          self.HEALTH = GameIamge(self.game_power_up, IMAGE_FOLDER+ IMAGE_FOLDER_POWER_UP, FILE_NAME_POWER_UP_HEALTH)
        elif self.power_up_type == POWER_UP_ROCKETS:
          self.ROCKETS = GameIamge(self.game_power_up, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_POWER_UP_ROCKETS)
        elif self.power_up_type == POWER_UP_LIFE:
          self.LIFE = GameIamge(self.game_power_up, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_POWER_UP_LIFE)
        elif self.power_up_type == POWER_UP_ADD_SHOT:
          self.ADD_SHOT = GameIamge(self.game_power_up, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_POWER_UP_ADD_SHOT)
        elif self.power_up_type == POWER_UP_SHIELD:
          self.SHIELD = GameIamge(self.game_power_up, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_POWER_UP_SHIELD)
        elif self.power_up_type == POWER_UP_CLUSTER_BOMB:
          self.CLUSTER_BOMB = GameIamge(self.game_power_up, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_POWER_UP_CLUSTER_BOMB)

    def GetPowerUpImage(self):
        if self.power_up_type == POWER_UP_HEALTH:
          return self.HEALTH.LoadGameIamge()
        elif self.power_up_type == POWER_UP_ROCKETS:
          return self.ROCKETS.LoadGameIamge()
        elif self.power_up_type == POWER_UP_LIFE:
          return self.LIFE.LoadGameIamge()
        elif self.power_up_type == POWER_UP_ADD_SHOT:
          return self.ADD_SHOT.LoadGameIamge()
        elif self.power_up_type == POWER_UP_SHIELD:
          return self.SHIELD.LoadGameIamge()
        elif self.power_up_type == POWER_UP_CLUSTER_BOMB:
          return self.CLUSTER_BOMB.LoadGameIamge()

    def GetWeaponMask(self):
        if self.power_up_type == POWER_UP_HEALTH:
          return self.HEALTH.MaskFromSurface()
        elif self.power_up_type == POWER_UP_ROCKETS:
          return self.ROCKETS.MaskFromSurface()
        elif self.power_up_type == POWER_UP_LIFE:
          return self.LIFE.MaskFromSurface()
        elif self.power_up_type == POWER_UP_ADD_SHOT:
          return self.ADD_SHOT.MaskFromSurface()
        elif self.power_up_type == POWER_UP_SHIELD:
          return self.SHIELD.MaskFromSurface()
        elif self.power_up_type == POWER_UP_CLUSTER_BOMB:
          return self.CLUSTER_BOMB.MaskFromSurface()


class Health(PowerUp):
   def __init__(self,  x, y, power_up_game, sound, health=25):
     super().__init__( x, y, power_up_game, POWER_UP_HEALTH, sound)
     self.sound = sound
     self.name = POWER_UP_HEALTH
     self.health = health

   def Ability(self,obj):
     current_health = obj.health
     obj.health += self.health
     if obj.health > obj.max_health:
       obj.health = obj.max_health
     obj.Power_up_healed_value = obj.health - current_health
     if obj.Power_up_healed_value < 0:
       obj.Power_up_healed_value = 0
     if obj.Power_up_healed_value >0:
       obj.Power_up_healed = True


class FullLife(PowerUp):
  def __init__(self, x, y, power_up_game, sound):
    super().__init__(x, y, power_up_game, POWER_UP_LIFE, sound)
    self.sound = sound
    self.name = POWER_UP_LIFE

  def Ability(self, obj):
    health = obj.max_health
    current_health = obj.health
    obj.health += health
    if obj.health > obj.max_health:
      obj.health = obj.max_health
    obj.Power_up_healed_value = obj.health - current_health
    if obj.Power_up_healed_value < 0:
      obj.Power_up_healed_value = 0
    if obj.Power_up_healed_value > 0:
      obj.Power_up_healed = True

class Rockets(PowerUp):
  def __init__(self, x, y, power_up_game, windows, sound):
    super().__init__(x, y, power_up_game, POWER_UP_ROCKETS, sound)
    self.sound = sound
    self.name = POWER_UP_ROCKETS
    self.myShip = ExtraShip(x, y, power_up_game, EXTRA_SHIP, EXTRA_SHIP_ROCKET, sound, 500)
    self.canDestroy = False
    self.StartShipAttack = False
    self.ShipInProgress = False
    self.windows = windows

  def Ability(self, obj):
    self.StartShipAttack = True
    if self.ShipInProgress:
      self.myShip.shoot()
      self.myShip.draw(self.windows)
    elif self.StartShipAttack:
      self.StartShipAttack = False
      self.ShipInProgress = True
      self.x = -500
      self.y = -500
      self.myShip = ExtraShip(randrange(0, 100), self.screenHeight - 20, self.power_up_game, EXTRA_SHIP, EXTRA_SHIP_ROCKET, self.sound, 500)

  def DrawAbility(self, windows, EnemyObj):
    if self.ShipInProgress:
      self._move()
      self.myShip.shoot()
      self.myShip.move_lasers(EnemyObj)
      self.myShip.draw(windows)

  def _move(self):
    self.myShip.y -= self.speed
    self.myShip.x += self.speed

  def CanDestroyAbility(self):
    if self.ShipInProgress:
      return (self.myShip.x + self.myShip.get_width()) > self.screenWidth
    else:
      return False

class AddShot(PowerUp):
  def __init__(self, x, y, power_up_game, windows, sound):
    super().__init__(x, y, power_up_game, POWER_UP_ADD_SHOT, sound)
    self.sound = sound
    self.name = POWER_UP_ADD_SHOT
    self.windows = windows
    self.canDestroy = True

  def Ability(self, obj):
    obj.extra_left_shot += 1
    obj.extra_right_shot += 1
    obj.cool_down = SHIP_COOL_DOWN + 10


class Shield(PowerUp):
  def __init__(self, x, y, power_up_game, windows, sound):
    super().__init__(x, y, power_up_game, POWER_UP_SHIELD, sound)
    self.sound = sound
    self.name = POWER_UP_SHIELD
    self.windows = windows
    self.canDestroy = True

  def Ability(self, obj):
    obj.shield_on = True
    obj.shield_time_counter = SHIELD_TIME


class ClusterBombPowerUp(PowerUp):
  def __init__(self, x, y, power_up_game, windows, sound):
    super().__init__(x, y, power_up_game, POWER_UP_CLUSTER_BOMB, sound)
    self.sound = sound
    self.name = POWER_UP_CLUSTER_BOMB
    self.windows = windows
    self.canDestroy = True

  def Ability(self, obj):
    obj.cluster_bomb_on = True
    obj.shoot()
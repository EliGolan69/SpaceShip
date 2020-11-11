from Const import *
import random

class GameLevel():
  def __init__(self, level=1):
    self._level = level
    self._startLevel = False
    self._healthPowerUpTimer = 0
    self._rocketPowerUpTimer = 0
    self._LifePowerUpTimer = 0
    self._LaserLeftPowerUpTimer = 0
    self._LaserRightPowerUpTimer = 0
    self._ShieldPowerUpTimer = 0
    self._ClusterBombPowerUpTimer = 0
    self._showStartLevel = SHOW_START_LEVEL_INDEX # index on the Y
    self.waveLength = WAVE_LENGTH
    self.startOfGame = True
    self.heal_value_counter = 0

  def SetHealValueCounter(self, plus_value, only_set_value = False):
    if only_set_value:
      self.heal_value_counter = only_set_value
    else:
      self.heal_value_counter += plus_value

  def GetHealValueCounter(self):
    return self.heal_value_counter

  def GetStartOfGame(self):
    return self.startOfGame

  def SetStartOfGame(self, _bool):
    self.startOfGame = _bool


  def GetWaveLength(self):
    return self.waveLength

  def SetWaveLength(self, wave):
    self.waveLength += wave

  def GetShowStartLevel (self):
    return self._showStartLevel

  def SetShowStartLevel (self, number):
    self._showStartLevel -= number
    if self._showStartLevel <= 0:
      self._StartLevel = False

  def AddLevel(self, number):
    self._level += number

  def GetLevel(self):
    return self._level

  def SetStartLevel(self, start_level):
    self._startLevel = start_level
    self._showStartLevel = SHOW_START_LEVEL_INDEX

  def GetStartLevel(self):
    return self._startLevel

  def EnemyWeaponShot(self):
    weaponSpeed = ENEMY_WEAPON_SHOT
    if self._level > 1 and self._level <= 2:
      weaponSpeed -= 0
    elif self._level > 3 and self._level <= 4:
      weaponSpeed -= 10
    elif self._level > 4 and self._level <= 6:
      weaponSpeed -= 20
    elif self._level > 6 and self._level <= 8:
      weaponSpeed -= 22
    elif self._level > 8 and self._level <= 11:
      weaponSpeed -= 30
    elif self._level > 11 and self._level <= 13:
      weaponSpeed -= 50
    elif self._level > 13 and self._level <= 18:
      weaponSpeed -= 70
    else:
      weaponSpeed -= 150
    return random.randrange(0, weaponSpeed) == 1

  def ChangeCoolDown(self):
    if self._level > 1 and self._level <=2:
      return 1
    elif self._level > 3 and self._level <=4:
      return 0
    elif self._level > 4 and self._level <=7:
      return 0
    elif self._level > 8 and self._level <=10:
      return 1
    elif self._level > 10 and self._level <= 13:
      return 1
    elif self._level > 13 and self._level <=15:
      return 1
    else:
      return 0

  def HealthPowerUp(self):
    self._healthPowerUpTimer += 1

    powerUp = 0
    if self._level > 1 and self._level <=5:
      powerUp -= 0
    elif self._level > 5 and self._level <=8:
      powerUp -= 100
    elif self._level > 8 and self._level <=10:
      powerUp -= 150
    elif self._level > 10 and self._level <=13:
      powerUp -= 250
    elif self._level > 13 and self._level <=15:
      powerUp -= 300
    else:
      powerUp = 0

    if self._healthPowerUpTimer > (POWER_UP_HEALTH_CREATE - powerUp):
      self._healthPowerUpTimer = 0
      return True
    else:
      return False

  def RocketPowerUp(self):
    self._rocketPowerUpTimer += 1

    powerUp = 0
    if self._level > 1 and self._level <=5:
      powerUp -= 0
    elif self._level > 5 and self._level <=8:
      powerUp -= 120
    elif self._level > 8 and self._level <=10:
      powerUp -= 180
    elif self._level > 10 and self._level <=13:
      powerUp -= 250
    elif self._level > 13 and self._level <=15:
      powerUp -= 300
    else:
      powerUp = 0

    if self._rocketPowerUpTimer > (POWER_UP_ROCKET_CREATE - powerUp):
      self._rocketPowerUpTimer = 0
      return True
    else:
      return False

  def LifePowerUp(self):
    self._LifePowerUpTimer += 1

    powerUp = 0
    if self._level > 1 and self._level <=5:
      powerUp -= 0
    elif self._level > 5 and self._level <=8:
      powerUp -= 120
    elif self._level > 8 and self._level <=10:
      powerUp -= 180
    elif self._level > 10 and self._level <=13:
      powerUp -= 250
    elif self._level > 13 and self._level <=15:
      powerUp -= 300
    else:
      powerUp = 0

    if self._LifePowerUpTimer > (POWER_UP_LIFE_CREATE - powerUp):
      self._LifePowerUpTimer = 0
      return True
    else:
      return False


  def LaserLeftPowerUp(self):
    self._LaserLeftPowerUpTimer += 1

    powerUp = 0
    if self._level > 1 and self._level <=5:
      powerUp -= 0
    elif self._level > 5 and self._level <=8:
      powerUp -= 300
    elif self._level > 8 and self._level <=10:
      powerUp -= 600
    elif self._level > 10 and self._level <=13:
      powerUp -= 800
    elif self._level > 13 and self._level <=15:
      powerUp -= 1000
    else:
      powerUp = 0

    if self._LaserLeftPowerUpTimer > (POWER_UP_ADD_LASER_CREATE - powerUp):
      self._LaserLeftPowerUpTimer = 0
      return True
    else:
      return False


  def ShieldPowerUp(self):
    self._ShieldPowerUpTimer += 1

    powerUp = 0
    if self._level > 1 and self._level <=5:
      powerUp -= 0
    elif self._level > 5 and self._level <=8:
      powerUp -= 300
    elif self._level > 8 and self._level <=10:
      powerUp -= 600
    elif self._level > 10 and self._level <=13:
      powerUp -= 800
    elif self._level > 13 and self._level <=15:
      powerUp -= 1500
    else:
      powerUp = 0

    if self._ShieldPowerUpTimer > (POWER_UP_SHIELD_CREATE - powerUp):
      self._ShieldPowerUpTimer = 0
      return True
    else:
      return False

  def ShieldTime(self):
    powerUp = SHIELD_TIME
    if self._level > 1 and self._level <=5:
      powerUp -= 30
    elif self._level > 5 and self._level <=8:
      powerUp -= 25
    elif self._level > 8 and self._level <=10:
      powerUp -= 22
    elif self._level > 10 and self._level <=13:
      powerUp -= 17
    elif self._level > 13 and self._level <=15:
      powerUp -= 14
    else:
      powerUp = 10

    return powerUp


  def ClusterBombPowerUp(self):
    self._ClusterBombPowerUpTimer += 1

    powerUp = 0
    if self._level > 1 and self._level <=5:
      powerUp -= 0
    elif self._level > 5 and self._level <=8:
      powerUp -= 30
    elif self._level > 8 and self._level <=10:
      powerUp -= 50
    elif self._level > 10 and self._level <=13:
      powerUp -= 100
    elif self._level > 13 and self._level <=15:
      powerUp -= 130
    else:
      powerUp = -150

    if self._ClusterBombPowerUpTimer > (POWER_UP_CLUSTER_BOMB_CREATE - powerUp):
      self._ClusterBombPowerUpTimer = 0
      return True
    else:
      return False
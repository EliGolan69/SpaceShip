from Const import *
import os
import pygame
import random
import Ships
from Players import *
import Enemys
from PowerUp import Health, Rockets, FullLife, AddShot, Shield, ClusterBombPowerUp
from Images import GameIamge
from GameLevels import GameLevel
from Sound import Sound
from GUI import GUIObj
from ExplosionAnimation import *
import Path

class Game():
  def __init__(self, gameWidth = 0, gameHeight = 0):

    self.myGame = pygame
    self.gameSound = Sound(self.myGame, IMAGE_FOLDER + IMAGE_FOLDER_MUSIC, FILE_NAME_GAME_MUSIC)
    self.myGame .init()
    self.myGame.font.init()
    self.gameLevel = GameLevel()
    self.FPS = GAME_FPS
    self.lost = False
    self.mainFont = self.myGame.font.SysFont("comicsans", 50)
    self.lostFont = self.myGame.font.SysFont("comicsans", 60)
    self.shipFont = self.myGame.font.SysFont("comicsans", 25)
    self.shipHealedFont = self.myGame.font.SysFont("comicsans", 23)
    self.nextLevelFont = self.myGame.font.SysFont("comicsans", 120)
    self.enemies = []
    self.powerUps = []
    self.animation_objs = []
    self.player = Player(x = 300, y = 630, player_game = self.myGame, ship_type = PLAYER_SHIP, laser_type = PLAYER_LASER, player_sound = self.gameSound)
    self.playerSpeed = PLAYER_SPEED
    self.run = True
    self.gameWidth = gameWidth
    self.gameHeight = gameHeight
    self.myGame.display.set_caption("My Space Shooter")
    if gameWidth == 0:
      self.gameWidth, self.gameHeight = WIDTH, HEIGHT
    self.mainWindows = self.myGame.display.set_mode((self.gameWidth, self.gameHeight))
    self.gameGUI = GUIObj(self.myGame, self.mainWindows, self.gameSound)
    BackGroundImage = GameIamge(self.myGame, IMAGE_FOLDER, FILE_NAME_BACK_GROUND, self.gameWidth, self.gameHeight)
    self.bkImage = BackGroundImage.GetScaleIamge()


  def _collide(self, obj1, obj2):
    if obj1.exploded:
      return False
    else:
      offset_x = obj2.x - obj1.x
      offset_y = obj2.y - obj1.y
      if type(obj2) == Player:
        if obj2.shield_on:
          offset_x = obj2.x - 25 - obj1.x
          offset_y = obj2.y - 25 - obj1.y
          return obj1.mask.overlap(obj2.shield_animation.masks[obj2.shield_animation_index], (offset_x, offset_y)) != None
        else:
          return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
      return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

  def _redraw_window_with_extra_data(self):
    if self.gameLevel.GetStartLevel() and (self.gameLevel.GetShowStartLevel() > 0) and (self.gameLevel.GetLevel() > 0):
      labelNextLevel = self.nextLevelFont.render(f"New level {self.gameLevel.GetLevel()}", 1,WHITE)
      self.mainWindows.blit(labelNextLevel, (self.gameWidth / 2 - labelNextLevel.get_width() / 2, 50 + self.gameLevel.GetShowStartLevel()))
      self.gameLevel.SetShowStartLevel(1)


  def _redraw_window(self):
    self.mainWindows.blit(self.bkImage, (0, 0))
    # draw text
    levelLabel = self.mainFont.render(f"Level: {self.gameLevel.GetLevel()}", 1,WHITE)
    self.mainWindows.blit(levelLabel, (10, 10))
    axis_y = 50
    axis_new_y = 22
    axis_line = axis_new_y
    labelCoolDown = self.shipFont.render(f"Weapon cooldown: {self.player.cool_down}", 1, WHITE)
    self.mainWindows.blit(labelCoolDown, (10, axis_y + axis_line))
    axis_line += axis_new_y
    labelEnemyWave = self.shipFont.render(f"Player Speed: {self.player.speed}", 1, WHITE)
    self.mainWindows.blit(labelEnemyWave, (10, axis_y+axis_line))
    axis_line += axis_new_y
    labelEnemyWave = self.shipFont.render(f"Enemy wave: {self.gameLevel.GetWaveLength()}", 1, WHITE)
    self.mainWindows.blit(labelEnemyWave, (10, axis_y+axis_line))
    axis_line += axis_new_y
    labelEnmeySpeed = self.shipFont.render(f"Enemy speed: {ENEMY_SPEED}", 1, WHITE)
    self.mainWindows.blit(labelEnmeySpeed, (10, axis_y+axis_line))
    axis_line += axis_new_y
    labelPowerUp = self.shipFont.render(f"Power up: {len(self.powerUps)}", 1, WHITE)
    self.mainWindows.blit(labelPowerUp, (10, axis_y + axis_line))

    self._redraw_window_with_extra_data()

    for powerUp in self.powerUps:
      powerUp.draw(self.mainWindows)
      if type(powerUp) == Rockets:
        powerUp.DrawAbility(self.mainWindows, self.enemies)

    for enemy in self.enemies:
      enemy.draw(self.mainWindows)

    self.player.draw(self.mainWindows)

    if self.player.Power_up_healed:
      if self.gameLevel.GetHealValueCounter() <= 55:
        self.gameLevel.SetHealValueCounter(1)
        labelPlayerHealed = self.shipHealedFont.render(f"+{self.player.Power_up_healed_value}", 1, WHITE)
        self.mainWindows.blit(labelPlayerHealed, (self.player.x + 10, self.player.y + self.player.imageHeight + (self.player.imageHeight / 2)-10))
      else:
        self.gameLevel.SetHealValueCounter(0, only_set_value=True)
        self.player.Power_up_healed = False

    if self.lost:
      lost_label = self.lostFont.render("You Lost!!", 1, (255, 255, 255))
      self.mainWindows.blit(lost_label, (self.gameWidth / 2 - lost_label.get_width() / 2, 350))

    self.gameGUI.draw()
    self.myGame.display.update()

  def _BuildEnemyWave(self):
    if len(self.enemies) == 0:
      if not self.gameLevel.GetStartOfGame():
        self.gameLevel.AddLevel(1)
        self.gameLevel.SetStartLevel(True)
        self.player.ChangeCoolDown(self.gameLevel.ChangeCoolDown())
        self.gameLevel.SetWaveLength(WAVE_LENGTH)
      else:
        self.gameLevel.SetStartOfGame(False)

      enemy_wave_len = self.gameLevel.GetWaveLength()
      enemy_path = random.randint(0, 8)
      for i in range(enemy_wave_len):
        enemy = Enemys.Enemy(1, 1, self.myGame,
                   random.choice(SHIP_LIST), random.choice(LASER_LIST), self.gameSound, Path.get_random_path(enemy_path))
        self.enemies.append(enemy)

  def _BuildPowerUps(self):
    if self.gameLevel.HealthPowerUp():
      powerUp = Health(random.randrange(50, self.gameWidth - 100), random.randrange(-300, -10), self.myGame,self.gameSound)
      self.powerUps.append(powerUp)

    if self.gameLevel.RocketPowerUp():
      powerUp = Rockets(random.randrange(50, self.gameWidth - 100), random.randrange(-300, -10), self.myGame, self.mainWindows, self.gameSound)
      self.powerUps.append(powerUp)

    if self.gameLevel.LifePowerUp():
      powerUp = FullLife(random.randrange(50, self.gameWidth - 100), random.randrange(-300, -10), self.myGame, self.gameSound)
      self.powerUps.append(powerUp)

    if self.gameLevel.LaserLeftPowerUp():
      powerUp = AddShot(random.randrange(50, self.gameWidth - 100), random.randrange(-300, -10), self.myGame, self.mainWindows,self.gameSound)
      self.powerUps.append(powerUp)

    if self.gameLevel.ShieldPowerUp():
      powerUp = Shield(random.randrange(50, self.gameWidth - 100), random.randrange(-300, -10), self.myGame, self.mainWindows, self.gameSound)
      self.powerUps.append(powerUp)

    if self.gameLevel.ClusterBombPowerUp():
      powerUp = ClusterBombPowerUp(random.randrange(50, self.gameWidth - 100), random.randrange(-300, -10), self.myGame, self.mainWindows, self.gameSound)
      self.powerUps.append(powerUp)

  def _PowerUpAction(self):
    self.player.SetShieldTimeCounter(1)
    for powerUp in self.powerUps[:]:
      powerUp.move()
      if type(powerUp) == Rockets:
        if powerUp.ShipInProgress:
          if (powerUp.myShip.x - 300 + powerUp.myShip.get_width()) > self.gameWidth:
            self.powerUps.remove(powerUp)
        """if powerUp.CanDestroyAbility:  #---- from some reason isn't working
            self.powerUps.remove(powerUp)"""

      if powerUp.collide(powerUp, self.player):
        self.gameSound.PowerUpEffect()
        powerUp.Ability(self.player)
        if powerUp.canDestroy:
          self.powerUps.remove(powerUp)
      elif((powerUp.y + powerUp.get_height()) > self.gameHeight) or ((powerUp.x + powerUp.get_width()) > self.gameWidth):
        self.powerUps.remove(powerUp)

  def _EnemyAction(self):
    for enemy in self.enemies[:]:
      if enemy.can_destroy():
        self.enemies.remove(enemy)
        continue

      if not enemy.exploded:
        enemy.move()
        if self.gameLevel.EnemyWeaponShot():
          enemy.shoot()

      enemy.move_lasers(self.player, self.gameHeight, True)

      if self._collide(enemy, self.player):
        enemy.explod_animation = SmallExplosionAnimation(self.myGame, self.gameSound, -50 ,-50)
        enemy.exploded = True
        if not self.player.shield_on:
          self.player.health -= ENEMY_WIN_DAMAGE
      elif enemy.y + enemy.get_height() > self.gameHeight:
        self.enemies.remove(enemy)


  def _CheckPlayerLost(self):
    if self.player.health <= 0:
      self.lost = True
      self.player.exploded = True

  def _CheckKeyPress(self):
    keys = self.myGame.key.get_pressed()
    if keys[self.myGame.K_LEFT] and self.player.x - self.playerSpeed > 0:  # left
      self.player.x -= self.playerSpeed
    if keys[self.myGame.K_RIGHT] and self.player.x + self.playerSpeed + self.player.get_width() < self.gameWidth:  # right
      self.player.x += self.playerSpeed
    if keys[self.myGame.K_UP] and self.player.y - self.playerSpeed > 0:  # up
      self.player.y -= self.playerSpeed
    if keys[self.myGame.K_DOWN] and self.player.y + self.playerSpeed + self.player.get_height() + 15 < self.gameHeight:  # down
      self.player.y += self.playerSpeed
    if keys[self.myGame.K_SPACE]:
      #self.gameSound.PlaySoundEffect(FILE_NAME_LASER_EFFECT, 0.6)
      self.player.shoot()

  def _StartGame(self):
    clock = self.myGame.time.Clock()
    while self.run:
        if not self.lost:
          clock.tick(self.FPS)
          self._redraw_window_with_extra_data()
          self._CheckPlayerLost()
          self._BuildEnemyWave()
          self._BuildPowerUps()
          self._redraw_window()
          self._CheckKeyPress()
          self._EnemyAction()
          self._redraw_window_with_extra_data()
          self._PowerUpAction()
          self.player.move_lasers(self.enemies)
          self.player.move_ClusterSingleBomb(self.enemies)
          self.gameGUI.CheckEvents(self.myGame, self.mainWindows)
          self.gameGUI.RunOnClickEvents()
        else:
          self._redraw_window()
          self.gameGUI.CheckEvents(self.myGame, self.mainWindows)
          self.gameGUI.RunOnClickEvents()
          self.gameGUI.CreatePlayAgain()
          if self.gameGUI.GetPlayagain():
            self._CleanVar()
          #self._CheckGameEvents()
          #self._WaitForUserClick()
          #self.run = False

  def main_menu(self):
    self.gameSound.PlayMusic(FILE_NAME_GAME_MUSIC, 0.2)
    self._StartGame()
    self.myGame.quit()

  def _CleanVar(self):
    self.lost = False
    self.gameLevel = GameLevel()
    self.enemies = []
    self.powerUps = []
    self.player = Player(x = 300, y = 630, player_game = self.myGame, ship_type = PLAYER_SHIP, laser_type = PLAYER_LASER, player_sound = self.gameSound)
    self.playerSpeed = PLAYER_SPEED
    self.run = True


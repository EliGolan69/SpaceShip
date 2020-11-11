from Ships import Ship
from Weapons import Laser, Laser_Left, Laser_Rigth, ClusterBomb, ClusterBombSingle
from Const import *
from ExplosionAnimation import PlayerExplosionAnimation, RocketExplosionAnimation
from Images import GameIamge


class Player(Ship):
  def __init__(self, x, y, player_game, ship_type, laser_type, player_sound, health=100):
    super().__init__(x, y, player_game, ship_type, laser_type, player_sound, health)
    self.playergame = player_game
    self.player_sound = player_sound
    self.max_health = health
    self.extra_shot = 0
    self.speed = PLAYER_SPEED
    self.weapon_speed = -5  # y
    self.weapon_speed_x = -1
    self.Power_up_healed_value = 0
    self.Power_up_healed = False
    self.explod_animation = PlayerExplosionAnimation(player_game, player_sound)
    self.clock = player_game.time.Clock()
    self.extra_left_shot = 0
    self.extra_right_shot = 0
    self.shield_on = False
    self.shield_time_counter = SHIELD_TIME
    self.shield_animation = ShieldAnimation(player_game, x, y)
    self.shield_animation_index = 0
    self.shield_show_time_counter = SHIELD_SHOW_TIME
    self.cluster_bomb_on = False
    self.cluster_bomb_single = []

  def SetShieldTimeCounter(self, value):
    self.shield_time_counter -= 1
    if self.shield_time_counter == 0:
      self.shield_on = False


  def ChangeCoolDown(self, remove_cool_down):
        self.cool_down -= remove_cool_down

  def shoot(self):
    if self.cluster_bomb_on:
      self.cluster_bomb_on = False
      self.ship_sound.RocketLaunchEffect()
      weapon = ClusterBomb(self.x + int(self.imageWidth / 2), self.y, self.ship_game, self.player_sound)
      self.weapons.append(weapon)
    else:
      if self.cool_down_counter == 0:
        self.ship_sound.LaserePlayerEffect()
        weapon = Laser(self.x + int(self.imageWidth / 2), self.y, self.ship_game, self.weapon_type)
        self.weapons.append(weapon)

        next_left_weapon = 10
        for shot in range(self.extra_left_shot):
          weapon1 = Laser_Left(self.x + int(self.imageWidth / 2) - (shot * next_left_weapon), self.y, self.ship_game, PLAYER_LASER_LEFT_RED)
          self.weapons.append(weapon1)

        for shot in range(self.extra_right_shot):
          weapon1 = Laser_Rigth(self.x + int(self.imageWidth / 2) + (shot * next_left_weapon), self.y, self.ship_game, PLAYER_LASER_RIGHT_RED)
          self.weapons.append(weapon1)

        self.cool_down_counter = 1

  def get_cluster_bomb_weapon(self):
    return self.cluster_bomb_single

  def move_ClusterSingleBomb(self, EnemyObjs):
   # self.cooldown()

    for cluster_bomb in self.cluster_bomb_single:
      cluster_bomb.move(self.weapon_speed)

      if cluster_bomb.off_screen(self.GetScreenSizeH()):
        self.cluster_bomb_single.remove(cluster_bomb)
      else:
        for obj in EnemyObjs:
          if cluster_bomb.collision(obj):
            obj.exploded = True
            if cluster_bomb in self.cluster_bomb_single:
              self.cluster_bomb_single.remove(cluster_bomb)


  def move_lasers(self, EnemyObjs):
    self.cooldown()
    for weapon in self.weapons:
      if (type(weapon) == ClusterBomb):
        if weapon.exploded:
          if weapon.start_cluster_single_bomb:
            continue
          else:
            self.create_cluster_bomb_single(weapon.x, weapon.y)
            weapon.start_cluster_single_bomb = True

      if (type(weapon) == Laser_Left):
        weapon.move(self.weapon_speed, self.weapon_speed_x)
      elif (type(weapon) == Laser_Rigth):
        weapon.move(self.weapon_speed, abs(self.weapon_speed_x))
      else:
        weapon.move(self.weapon_speed)

      if weapon.off_screen(self.GetScreenSizeH()):
        self.weapons.remove(weapon)
      else:
        for obj in EnemyObjs:
          if weapon.collision(obj):
            if (type(weapon) == ClusterBomb):
              obj.explod_animation = RocketExplosionAnimation(obj.ship_game, obj.ship_sound)
              self.create_cluster_bomb_single(obj.x, obj.y)
            obj.exploded = True
            if weapon in self.weapons:
              self.weapons.remove(weapon)


  def create_cluster_bomb_single(self, x, y):
    for index in range(30):
      cluster_bomb = ClusterBombSingle(x, y, self.ship_game, index)
      self.cluster_bomb_single.append(cluster_bomb)

  def draw(self, window):
    if not self.exploded:
      window.blit(self.image, (self.x, self.y))
      if self.shield_on:
         if self.shield_time_counter in (2,6,7,12,13,17,20,22,23,25,28,30,33,37,40,43,46,49):
           pass
         else:
           window.blit(self.shield_animation.images[self.shield_animation_index], (self.x-25, self.y-25))

         if self.shield_show_time_counter == 0:
           self.shield_animation_index += 1
           self.shield_show_time_counter = SHIELD_SHOW_TIME
         else:
           self.shield_show_time_counter -= 1

         if self.shield_animation_index > 5:
           self.shield_animation_index = 0


      self.healthbar(window)
    elif self.exploded:
        self.explod_animation.StartAnimation(self.x, self.y, window)

    for weapon in self.weapons:
        weapon.draw(window)

    for cluster_bomb in self.cluster_bomb_single:
        cluster_bomb.draw(window)

  def healthbar(self, window):
    if self.health < 0:
      self.health = 0
    self.playergame.draw.rect(window, (255, 0, 0),
                     (self.x, self.y + self.image.get_height() + 7, self.image.get_width(), 2))
    self.playergame.draw.rect(window, (0, 255, 0), (
    self.x, self.y + self.image.get_height() + 7, self.image.get_width() * (self.health / self.max_health), 2))



class ShieldAnimation():
  def __init__(self, game, x, y):
    self.x = x
    self.y = y
    self.game = game
    self.images = []
    self.masks = []
    self.shield_image1 = GameIamge(game, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_SHIELD_1)
    self.shield_image2 = GameIamge(game, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_SHIELD_1)
    self.shield_image3 = GameIamge(game, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_SHIELD_1)
    self.shield_image4 = GameIamge(game, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_SHIELD_1)
    self.shield_image5 = GameIamge(game, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_SHIELD_1)
    self.shield_image6 = GameIamge(game, IMAGE_FOLDER + IMAGE_FOLDER_POWER_UP, FILE_NAME_SHIELD_6)

    self.image_1 = self.shield_image1.LoadGameIamge()
    self.image_2 = self.shield_image2.LoadGameIamge()
    self.image_3 = self.shield_image3.LoadGameIamge()
    self.image_4 = self.shield_image4.LoadGameIamge()
    self.image_5 = self.shield_image5.LoadGameIamge()
    self.image_6 = self.shield_image6.LoadGameIamge()

    self.mask_1 = self.shield_image1.MaskFromSurface()
    self.mask_2 = self.shield_image2.MaskFromSurface()
    self.mask_3 = self.shield_image3.MaskFromSurface()
    self.mask_4 = self.shield_image4.MaskFromSurface()
    self.mask_5 = self.shield_image5.MaskFromSurface()
    self.mask_6 = self.shield_image6.MaskFromSurface()

    self.images = [self.image_1, self.image_2 ,self.image_3 ,self.image_4 ,self.image_5 ,self.image_6]
    self.masks =  [self.mask_1, self.mask_2, self.mask_3, self.mask_4, self.mask_5, self.mask_6]
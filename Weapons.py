from Const import *
from Images import GameIamge
from ExplosionAnimation import RocketFlame, RocketExplosionAnimation
import random


class Laser():
    def __init__(self, x, y, laser_game, laser_type, damage = 10):
        self.laser_game = laser_game
        self.laser_type = laser_type
        self.WeaponLaser = WeaponsContainer(self.laser_game, laser_type)
        self.image = self.WeaponLaser.GetWeaponImage()
        self.mask = self.WeaponLaser.GetWeaponMask()
        self.imageHeight = self.image.get_height()
        self.imageWidth = self.image.get_width()
        self.x = x - int(self.imageWidth/2)
        self.y = y
        self.damage = damage
        self.speed = 5

    def get_random_not_zero(self):
        while True:
            number = random.randint(-10, 10)
            if number != 0:
                return number

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collide(self, obj1, obj2): #obj1 == Laser, obj2 == Enemy
        if obj2.exploded:
          return False
        else:
          offset_x = obj2.x - obj1.x
          offset_y = obj2.y - obj1.y
          return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def _main_player_collision(self, obj):
        if obj.shield_on:
          return self._collide_shield(self, obj)
        else:
          return self.collide(self, obj)

    def collision(self, obj, main_player = False):
        if main_player:
          return self._main_player_collision(obj)
        else:
          return self.collide(self, obj)

    def _collide_shield(self, obj1, obj2):
            offset_x = obj2.x - 25 - obj1.x
            offset_y = obj2.y - 25 - obj1.y
            return obj1.mask.overlap(obj2.shield_animation.masks[obj2.shield_animation_index],  (offset_x, offset_y)) != None


class Rocket(Laser):
    def __init__(self, x, y, laser_game, sound, laser_type, damage = 10):
        super().__init__(x, y, laser_game, laser_type)
        if laser_type == EXTRA_SHIP_ROCKET:
            self.RocketFlameAnimation = RocketFlame(laser_game, sound)


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if self.laser_type == EXTRA_SHIP_ROCKET:
            self.RocketFlameAnimation.StartAnimation(self.x + 9, self.y + self.imageHeight, window)



class ClusterBomb (Laser):
    def __init__(self, x, y, laser_game, sound, damage = 10):
        super().__init__(x, y, laser_game, PLAYER_CLUSTER_BOMB)
        self.fly_time = 0
        self.sound = sound
        self.BombExplosionAnimation = RocketExplosionAnimation(laser_game, sound)
        self.exploded = False
        self.start_cluster_single_bomb = False

    def move(self, vel):
        self.y += vel
        self.fly_time += vel

    def draw(self, window):
        if self.fly_time <= -300:
            self.BombExplosionAnimation.StartAnimation(self.x, self.y, window)
            self.exploded = True

        else:
            window.blit(self.image, (self.x, self.y))







class ClusterBombSingle(Laser):
    def __init__(self, x, y, laser_game, cluster_index=0, damage = 10):
        super().__init__(x, y, laser_game, PLAYER_CLUSTER_SINGLE_BOMB)
        self.cluster_index = cluster_index
        self.vector_x = self.get_random_not_zero()
        self.vector_y = self.get_random_not_zero()

    def move(self, vel):
        if self.cluster_index == 0:
          self.y += vel
        else:
          self.x += self.vector_x
          self.y += self.vector_y


class Laser_Left():
    def __init__(self, x, y, laser_game, laser_type, damage = 10):
        self.laser_game = laser_game
        self.laser_type = laser_type
        self.WeaponLaser = WeaponsContainer(self.laser_game, laser_type)
        self.image = self.WeaponLaser.GetWeaponImage()
        self.mask = self.WeaponLaser.GetWeaponMask()
        self.imageHeight = self.image.get_height()
        self.imageWidth = self.image.get_width()
        self.x = x - int(self.imageWidth/2)
        self.y = y
        self.damage = damage
        self.speed = 5

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, move_y, move_x = 0):
        self.y += move_y
        self.x += move_x

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collide(self, obj1, obj2): #obj1 == Laser, obj2 == Enemy
        if obj2.exploded:
          return False
        else:
          offset_x = obj2.x - obj1.x
          offset_y = obj2.y - obj1.y
          return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def collision(self, obj):
        return self.collide(self, obj)

class Laser_Rigth(Laser_Left):
    def __init__(self, x, y, laser_game, laser_type, damage = 10):
        super().__init__( x, y, laser_game, laser_type, damage = 10)

class WeaponsContainer():
    def __init__(self, game_weapon, weapon_type):
        self.weapon_type = weapon_type
        self.game_weapon = game_weapon
        if self.weapon_type == RED_LASER:
          self.RED_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_RED_LASER)
        elif self.weapon_type == GREEN_LASER:
          self.GREEN_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_GREEN_LASER)
        elif self.weapon_type == BLUE_LASER:
          self.BLUE_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_BLUE_LASER)
        elif self.weapon_type == YELLOW_LASER:
          self.YELLOW_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_YELLOW_LASER)
        elif self.weapon_type == PLAYER_LASER:
          self.PLAYER_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PALER_LASER)
        elif self.weapon_type == EXTRA_SHIP_ROCKET:
          self.ROCKETS = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_ROCKETS)
        elif self.weapon_type == PLAYER_LASER_LEFT_RED:
          self.PLAYER_LASER_LEFT = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_LASER_LEFT_RED)
        elif self.weapon_type == PLAYER_LASER_RIGHT_RED:
          self.PLAYER_LASER_RIGHT = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_LASER_RIGHT_RED)
        elif self.weapon_type == PLAYER_CLUSTER_BOMB:
           self.PLAYER_CLUSTER_BOMB = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_CLUSTER_BOMB)
        elif self.weapon_type == PLAYER_CLUSTER_SINGLE_BOMB:
           self.PLAYER_CLUSTER_SINGLE_BOMB = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_CLUSTER_SINGLE_BOMB)

    def GetWeaponImage(self):
        if self.weapon_type == RED_LASER:
          return self.RED_LASER.LoadGameIamge()
        elif self.weapon_type == GREEN_LASER:
          return self.GREEN_LASER.LoadGameIamge()
        elif self.weapon_type == BLUE_LASER:
          return self.BLUE_LASER.LoadGameIamge()
        elif self.weapon_type == YELLOW_LASER:
          return self.YELLOW_LASER.LoadGameIamge()
        elif self.weapon_type == PLAYER_LASER:
          return self.PLAYER_LASER.LoadGameIamge()
        elif self.weapon_type == EXTRA_SHIP_ROCKET:
          return self.ROCKETS.LoadGameIamge()
        elif self.weapon_type == PLAYER_LASER_LEFT_RED:
          return self.PLAYER_LASER_LEFT.LoadGameIamge()
        elif self.weapon_type == PLAYER_LASER_RIGHT_RED:
          return self.PLAYER_LASER_RIGHT.LoadGameIamge()
        elif self.weapon_type == PLAYER_CLUSTER_BOMB:
          return self.PLAYER_CLUSTER_BOMB.LoadGameIamge()
        elif self.weapon_type == PLAYER_CLUSTER_SINGLE_BOMB:
          return self.PLAYER_CLUSTER_SINGLE_BOMB.LoadGameIamge()

    def GetWeaponMask(self):
        if self.weapon_type == RED_LASER:
          return self.RED_LASER.MaskFromSurface()
        elif self.weapon_type == GREEN_LASER:
          return self.GREEN_LASER.MaskFromSurface()
        elif self.weapon_type == BLUE_LASER:
          return self.BLUE_LASER.MaskFromSurface()
        elif self.weapon_type == YELLOW_LASER:
          return self.YELLOW_LASER.MaskFromSurface()
        elif self.weapon_type == PLAYER_LASER:
          return self.PLAYER_LASER.MaskFromSurface()
        elif self.weapon_type == EXTRA_SHIP_ROCKET:
          return self.ROCKETS.MaskFromSurface()
        elif self.weapon_type == PLAYER_LASER_LEFT_RED:
          return self.PLAYER_LASER_LEFT.MaskFromSurface()
        elif self.weapon_type == PLAYER_LASER_RIGHT_RED:
          return self.PLAYER_LASER_RIGHT.MaskFromSurface()
        elif self.weapon_type == PLAYER_CLUSTER_BOMB:
          return self.PLAYER_CLUSTER_BOMB.MaskFromSurface()
        elif self.weapon_type == PLAYER_CLUSTER_SINGLE_BOMB:
          return self.PLAYER_CLUSTER_SINGLE_BOMB.MaskFromSurface()
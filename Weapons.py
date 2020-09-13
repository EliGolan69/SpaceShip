from Const import *
from Images import GameIamge


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

    def collision(self, obj, main_player = False):
        if main_player:
          return self._collide_shield(self, obj)
        else:
          return self.collide(self, obj)

    def _collide_shield(self, obj1, obj2):
            offset_x = obj2.x - 25 - obj1.x
            offset_y = obj2.y - 25 - obj1.y
            return obj1.mask.overlap(obj2.shield_animation.masks[obj2.shield_animation_index],  (offset_x, offset_y)) != None


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
        self.RED_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_RED_LASER)
        self.GREEN_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_GREEN_LASER)
        self.BLUE_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_BLUE_LASER)
        self.YELLOW_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_YELLOW_LASER)
        self.PLAYER_LASER = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PALER_LASER)
        self.ROCKETS = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_ROCKETS)
        self.PLAYER_LASER_LEFT = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_LASER_LEFT_RED)
        self.PLAYER_LASER_RIGHT = GameIamge(self.game_weapon, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_LASER_RIGHT_RED)

    def GetWeaponImage(self):
        self.weaponTypes = {
            RED_LASER: (self.RED_LASER.LoadGameIamge()),
            GREEN_LASER: (self.GREEN_LASER.LoadGameIamge()),
            BLUE_LASER: (self.BLUE_LASER.LoadGameIamge()),
            YELLOW_LASER: (self.YELLOW_LASER.LoadGameIamge()),
            PLAYER_LASER: (self.PLAYER_LASER.LoadGameIamge()),
            EXTRA_SHIP_ROCKET: (self.ROCKETS.LoadGameIamge()),
            PLAYER_LASER_LEFT_RED: (self.PLAYER_LASER_LEFT.LoadGameIamge()),
            PLAYER_LASER_RIGHT_RED: (self.PLAYER_LASER_RIGHT.LoadGameIamge())
        }
        return self.weaponTypes[self.weapon_type]

    def GetWeaponMask(self):
        self.weaponTypes = {
          RED_LASER: (self.RED_LASER.MaskFromSurface()),
          GREEN_LASER: (self.GREEN_LASER.MaskFromSurface()),
          BLUE_LASER: (self.BLUE_LASER.MaskFromSurface()),
          YELLOW_LASER: (self.YELLOW_LASER.MaskFromSurface()),
          PLAYER_LASER: (self.PLAYER_LASER.MaskFromSurface()),
          EXTRA_SHIP_ROCKET: (self.ROCKETS.MaskFromSurface()),
          PLAYER_LASER_LEFT_RED: (self.PLAYER_LASER_LEFT.MaskFromSurface()),
          PLAYER_LASER_RIGHT_RED: (self.PLAYER_LASER_RIGHT.MaskFromSurface())

        }
        return self.weaponTypes[self.weapon_type]
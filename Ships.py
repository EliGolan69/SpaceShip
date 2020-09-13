from Const import *
from Weapons import Laser_Left, Laser
from Images import GameIamge
from Sound import Sound
from ExplosionAnimation import *

class Ship():
    def __init__(self, x, y, ship_game, ship_type, weapon_type, ship_sound, health=100):
        self.ship_sound = ship_sound
        self.cool_down = SHIP_COOL_DOWN
        self.x = x
        self.y = y
        self.weapon_type = weapon_type
        self.health = health
        self.weapons = []
        self.cool_down_counter = 0
        self.ship_game = ship_game
        self.ShipType = ShipContainer(ship_game, ship_type)
        self.image = self.ShipType.GetShipImage()
        self.mask = self.ShipType.GetShipMask()
        self.imageHeight = self.image.get_height()
        self.imageWidth = self.image.get_width()
        self.damage = ENEMY_COLLIDE_DAMAGE
        self.speed = 1
        self.exploded = False
        self.shipSound = Sound(self.ship_game, IMAGE_FOLDER + IMAGE_FOLDER_MUSIC, FILE_NAME_GAME_MUSIC, False)
        self.explod_animation = ExplosionAnimation(ship_game, ship_sound)



    def ChangeCoolDown(self, remove_cool_down):
        self.cool_down -= remove_cool_down

    def GetScreenSizeH(self):
        screenWidth, screenHeight = self.ship_game.display.get_surface().get_size()
        return screenHeight

    def GetScreenSizeW(self):
        screenWidth, screenHeight = self.ship_game.display.get_surface().get_size()
        return screenWidth

    def draw(self, window):
        if not self.exploded:
          window.blit(self.image, (self.x, self.y))
        elif self.exploded:
            self.explod_animation.StartAnimation(self.x, self.y, window)

        for weapon in self.weapons:
            weapon.draw(window)

    def move_lasers(self, obj, screenHeight, obj_player = False): # obj = Player
        self.cooldown()
        for weapon in self.weapons:
            weapon.move(weapon.speed)
            if weapon.off_screen(screenHeight):
                self.weapons.remove(weapon)
            elif weapon.collision(obj, obj_player):
                if not obj.shield_on:
                  obj.health -= weapon.damage
                self.weapons.remove(weapon)

    def cooldown(self):
        if self.cool_down_counter >= self.cool_down:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            self.ship_sound.LaserePlayerEffect()
            weapon = Laser(self.x + int(self.imageWidth/2), self.y, self.ship_game, self.weapon_type)
            self.weapons.append(weapon)
            self.cool_down_counter = 1

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

class ShipContainer():
    def __init__(self, shipgame, ship_type):
        self.ship_type = ship_type
        self.shipgame = shipgame
        self.RED_SPACE_SHIP = GameIamge(self.shipgame, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_RED_SPACE_SHIP)
        self.GREEN_SPACE_SHIP = GameIamge(self.shipgame, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_GREEN_SPACE_SHIP)
        self.BLUE_SPACE_SHIP = GameIamge(self.shipgame, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_BLUE_SPACE_SHIP)
        self.YELLOW_SPACE_SHIP = GameIamge(self.shipgame, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_YELLOW_SPACE_SHIP)
        self.PLAYER_SPACE_SHIP = GameIamge(self.shipgame, IMAGE_FOLDER+IMAGE_FOLDER_ENEMY, FILE_NAME_PLAYER_SPACE_SHIP)
        self.EXTRA_SHIP = GameIamge(self.shipgame, IMAGE_FOLDER + IMAGE_FOLDER_ENEMY, FILE_NAME_EXTRA_SHIP)

    def GetShipImage(self):
        self.shipTypes = {
            RED_SHIP: (self.RED_SPACE_SHIP.LoadGameIamge()),
            GREEN_SHIP: (self.GREEN_SPACE_SHIP.LoadGameIamge()),
            BLUE_SHIP: (self.BLUE_SPACE_SHIP.LoadGameIamge()),
            YELLOW_SHIP: (self.YELLOW_SPACE_SHIP.LoadGameIamge()),
            PLAYER_SHIP: (self.PLAYER_SPACE_SHIP.LoadGameIamge()),
            EXTRA_SHIP: (self.EXTRA_SHIP.LoadGameIamge()),
                         }
        return self.shipTypes[self.ship_type]

    def GetShipMask(self):
        self.shipTypes = {
            RED_SHIP: (self.RED_SPACE_SHIP.MaskFromSurface()),
            GREEN_SHIP: (self.GREEN_SPACE_SHIP.MaskFromSurface()),
            BLUE_SHIP: (self.BLUE_SPACE_SHIP.MaskFromSurface()),
            YELLOW_SHIP: (self.YELLOW_SPACE_SHIP.MaskFromSurface()),
            PLAYER_SHIP: (self.PLAYER_SPACE_SHIP.MaskFromSurface()),
            EXTRA_SHIP: (self.EXTRA_SHIP.MaskFromSurface()),
                         }
        return self.shipTypes[self.ship_type]

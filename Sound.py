from Const  import *

class Sound():
  def __init__(self, sound_game, files_path, music_file, load_music = True):
    self.sound_effect = True
    self.sound_game = sound_game
    self.sound_game.mixer.pre_init(44100, -16, 2, 512)
    self.sound_game.mixer.init()
    self.music_file = music_file
    self.files_path = files_path
    if load_music:
      self.sound_game.mixer.music.load(files_path + music_file)

    self.laser_player = sound_game.mixer.Sound(files_path + FILE_NAME_LASER_EFFECT)
    self.laser_player.set_volume(0.4)

    self.laser_enemy = sound_game.mixer.Sound(files_path + FILE_NAME_ENEMY_EFFECT)
    self.laser_enemy.set_volume(1)

    self.rocket_ship = sound_game.mixer.Sound(files_path + FILE_NAME_ROCKET_EFFECT)
    self.rocket_ship.set_volume(0.2)

  def get_sound_effect(self):
      return self.sound_effect

  def set_sound_effect(self, bool_value):
    self.sound_effect = bool_value

  def PlayMusic(self, file_name, volume):
    self.sound_game.mixer.music.play(-1)
    self.sound_game.mixer.music.set_volume(volume)

  def PlaySoundEffect(self, file_name, volume=1):
    if self.sound_effect:
      soundEffect = self.sound_game.mixer.Sound(self.files_path + file_name)
      soundEffect.set_volume(volume)
      soundEffect.play()

  def LaserePlayerEffect(self):
    if self.sound_effect:
      self.laser_player.play()

  def LaserEnemyEffect(self):
    if self.sound_effect:
      self.laser_enemy.play()

  def RockketShipEffect(self):
    if self.sound_effect:
      self.rocket_ship.play()


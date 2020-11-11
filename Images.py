import os

class GameIamge():
  def __init__(self, game_image, image_folder, image_name, scale_width = 0, scale_height = 0):
    self.image_folder = image_folder
    self.image_name = image_name
    self.game_image = game_image
    self.width = None
    self.height = None
    self.scale_width = scale_width
    self.scale_height = scale_height

  def GetImageGameFile(self):
    return os.path.join(self.image_folder, self.image_name)

  def GetScaleIamge(self):
    return self.game_image.transform.scale(self.game_image.image.load(self.GetImageGameFile()), (self.scale_width, self.scale_height))

  def LoadGameIamge(self):
    if os.path.exists(self.GetImageGameFile()):
      return self.game_image.image.load(self.GetImageGameFile())
    else:
      return None

  def MaskFromSurface(self):
    return self.game_image.mask.from_surface(self.game_image.image.load(self.GetImageGameFile()))
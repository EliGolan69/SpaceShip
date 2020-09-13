from Const import *
from Images import *

class Window():
  def __init__(self, engine_game, engine_window, x, y, window_type):
      self.engine_game = engine_game
      self.engine_window = engine_window
      self.x = x
      self.y = y
      self.window_type = window_type
      self.windowType = GUIContainer(engine_game, window_type)
      self.image = self.windowType.GetGUIImage()
      self.mask = self.windowType.GetGUIMask()
      self.imageHeight = self.image.get_height()
      self.imageWidth = self.image.get_width()

  def draw(self):
    self.engine_window.blit(self.image, (self.x, self.y))

class NavBar():
  def __init__(self, engine_game, engine_window, x, y, number_of_buttons, button_types_normal, button_types_hover, button_types_click):
      self.engine_game, self.engine_window, self.x, self.y, self.number_of_buttons = engine_game, engine_window, x, y, number_of_buttons
      self.button_types_normal, self.button_types_hover, self.button_types_click = button_types_normal, button_types_hover, button_types_click
      self.buttons = []
      extra_space_x = 0
      for buttonNumber in range(number_of_buttons):
         button = Button(engine_game, engine_window, x + extra_space_x, y,
                         button_types_normal[buttonNumber],
                         button_types_hover[buttonNumber],
                         button_types_click[buttonNumber])
         self.buttons.append(button)
         extra_space_x += button.imageWidth - 15

  def draw(self):
    for button in self.buttons:
      button.draw()

  def RunEvents(self, windows_events):
     for button in self.buttons:
       button.RunEvents(windows_events)

  def RunButtonsOnClick(self, windows_events):
    for button in self.buttons:
      button.RunOnClick()



class Button():
  def __init__(self, engine_game, engine_window, x, y, button_types_normal, button_types_hover, button_types_click):
    self.button_types_normal, self.button_types_hover, self.button_types_click = button_types_normal, button_types_hover, button_types_click
    self.engine_game = engine_game
    self.engine_window = engine_window
    self.x = x
    self.y = y
    self.screenWidth, self.screenHeight = self.engine_game.display.get_surface().get_size()
    self.buttonNormalType = GUIContainer(engine_game, button_types_normal)
    self.image_normal = self.buttonNormalType.GetGUIImage()
    self.mask_normal = self.buttonNormalType.GetGUIMask()
    self.imageHeightNormal = self.image_normal.get_height()
    self.imageWidth_normal = self.image_normal.get_width()

    self.buttonHoverType = GUIContainer(engine_game, button_types_hover)
    self.image_hover = self.buttonHoverType.GetGUIImage()
    self.mask_hover = self.buttonHoverType.GetGUIMask()
    self.imageHeightNormal = self.image_hover.get_height()
    self.imageWidth_normal = self.image_hover.get_width()

    self.buttonClickType = GUIContainer(engine_game, button_types_click)
    self.image_click = self.buttonClickType.GetGUIImage()
    self.mask_click = self.buttonClickType.GetGUIMask()
    self.imageHeightNormal = self.image_click.get_height()
    self.imageWidth_normal = self.image_click.get_width()
    self.OnMouseHover = False
    self.OnMouseClick = False
    self.OnClick = None
    self.mouse_pos = self.engine_game.mouse.get_pos()
    self.image = self.buttonNormalType.GetGUIImage()
    self.mask = self.buttonNormalType.GetGUIMask()
    self.imageHeight = self.image.get_height()
    self.imageWidth = self.image.get_width()

  def RunOnClick(self):
    if self.OnMouseClick:
      self.OnMouseClick = False
      self.OnClick()


  def RunEvents(self, windows_events):
    if len(windows_events) > 0:
     self.OnMouseHover = False
     self.OnMouseClick = False
     for windows_event in windows_events:
       self.mouse_pos = self.engine_game.mouse.get_pos()
       if self.mouse_pos[0] > self.x and self.mouse_pos[0] < self.x + self.imageWidth-15:
          if self.mouse_pos[1] > self.y and self.mouse_pos[1] < self.y + self.imageHeight-15:
           if windows_event.type == self.engine_game.MOUSEBUTTONDOWN:
              self.OnMouseClick = True
              self.OnMouseHover = True
           else:
              self.OnMouseHover = True

  def draw(self):
    if self.OnMouseClick:
      self.image = self.image_click
    elif self.OnMouseHover:
      self.image = self.image_hover
    else:
      self.image = self.image_normal

    self.engine_window.blit(self.image, (self.x, self.y))


class CheckBox():
    def __init__(self, engine_game, engine_window, x, y, check_box_types_on, check_box_types_off, active):
      self.engine_game, self.engine_window, self.x, self.y, self.check_box_types_on, self.check_box_types_off = engine_game, engine_window, x, y, check_box_types_on, check_box_types_off
      self.engine_game = engine_game
      self.engine_window = engine_window
      self.x = x
      self.y = y
      self.active = active
      self.screenWidth, self.screenHeight = self.engine_game.display.get_surface().get_size()

      self.check_boxOnType = GUIContainer(engine_game, check_box_types_on)
      self.image_on = self.check_boxOnType.GetGUIImage()
      self.mask_on = self.check_boxOnType.GetGUIMask()
      self.image_height_on = self.image_on.get_height()
      self.image_width_on = self.image_on.get_width()

      self.check_boxOffType = GUIContainer(engine_game, check_box_types_off)
      self.image_off = self.check_boxOffType.GetGUIImage()
      self.mask_off = self.check_boxOffType.GetGUIMask()
      self.image_height_off = self.image_off.get_height()
      self.image_height_off = self.image_off.get_width()

      self.OnMouseClick = False
      self.OnClick = None
      if self.active:
        self.image = self.check_boxOnType.GetGUIImage()
        self.mask = self.check_boxOnType.GetGUIMask()
      else:
        self.image = self.check_boxOffType.GetGUIImage()
        self.mask = self.check_boxOffType.GetGUIMask()

      self.imageHeight = self.image.get_height()
      self.imageWidth = self.image.get_width()

    def RunOnClick(self):
      if self.OnMouseClick:
        self.OnMouseClick = False
        self.OnClick()

    def RunEvents(self, windows_events):
      if len(windows_events) > 0:
        self.OnMouseClick = False
        for windows_event in windows_events:
          self.mouse_pos = self.engine_game.mouse.get_pos()
          if self.mouse_pos[0] > self.x - 2 and self.mouse_pos[0] < self.x + 5 + self.imageWidth - 8:
            if self.mouse_pos[1] > self.y - 2 and self.mouse_pos[1] < self.y + 5 + self.imageHeight - 8:
              if windows_event.type == self.engine_game.MOUSEBUTTONDOWN:
                self.OnMouseClick = True

    def draw(self):
      if self.OnMouseClick:
        if self.active:
          self.image =  self.image_off
          self.active = False
        else:
          self.image = self.image_on
          self.active = True

      self.engine_window.blit(self.image, (self.x, self.y))



class GUIContainer():
  def __init__(self, gameGUI, gui_type):
    self.gameGUI = gameGUI
    self.gui_type = gui_type
    self.WINDOWS_SMALL = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_WINDOWS_SMALL)

    self.BUTTON_PLAY_NORMAL = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_PLAY_NORMAL)
    self.BUTTON_PLAY_HOVER = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_PLAY_HOVER)
    self.BUTTON_PLAY_CLICK = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_PLAY_CLICK)

    self.BUTTON_PAUSE_NORMAL = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_PAUSE_NORMAL)
    self.BUTTON_PAUSE_HOVER = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_PAUSE_HOVER)
    self.BUTTON_PAUSE_CLICK = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_PAUSE_CLICK)

    self.BUTTON_OPTIONS_NORMAL = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_OPTIONS_NORMAL)
    self.BUTTON_OPTIONS_HOVER = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_OPTIONS_HOVER)
    self.BUTTON_OPTIONS_CLICK = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_BTN_OPTIONS_CLICK)

    self.CHECKBOX_MUSIC_ON = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_CHECKBOX_ON)
    self.CHECKBOX_MUSIC_OFF = GameIamge(self.gameGUI, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_CHECKBOX_OFF)

  def GetGUIImage(self):
    self.powerupTypes = {
      GUI_WINDOWS_SMALL: (self.WINDOWS_SMALL.LoadGameIamge()),
      GUI_BUTTON_PLAY_NORMAL: (self.BUTTON_PLAY_NORMAL.LoadGameIamge()),
      GUI_BUTTON_PLAY_HOVER: (self.BUTTON_PLAY_HOVER.LoadGameIamge()),
      GUI_BUTTON_PLAY_CLICK: (self.BUTTON_PLAY_CLICK.LoadGameIamge()),

      GUI_BUTTON_PAUSE_NORMAL: (self.BUTTON_PAUSE_NORMAL.LoadGameIamge()),
      GUI_BUTTON_PAUSE_HOVER: (self.BUTTON_PAUSE_HOVER.LoadGameIamge()),
      GUI_BUTTON_PAUSE_CLICK: (self.BUTTON_PAUSE_CLICK.LoadGameIamge()),

      GUI_BUTTON_OPTIONS_NORMAL: (self.BUTTON_OPTIONS_NORMAL.LoadGameIamge()),
      GUI_BUTTON_OPTIONS_HOVER: (self.BUTTON_OPTIONS_HOVER.LoadGameIamge()),
      GUI_BUTTON_OPTIONS_CLICK: (self.BUTTON_OPTIONS_CLICK.LoadGameIamge()),

      GUI_BUTTON_CHECKBOX_ON: (self.CHECKBOX_MUSIC_ON.LoadGameIamge()),
      GUI_BUTTON_CHECKBOX_OFF: (self.CHECKBOX_MUSIC_OFF.LoadGameIamge())
    }
    return self.powerupTypes[self.gui_type]

  def GetGUIMask(self):
    self.powerupTypes = {
      GUI_WINDOWS_SMALL: (self.WINDOWS_SMALL.MaskFromSurface()),

      GUI_BUTTON_PLAY_NORMAL: (self.BUTTON_PLAY_NORMAL.MaskFromSurface()),
      GUI_BUTTON_PLAY_HOVER: (self.BUTTON_PLAY_HOVER.MaskFromSurface()),
      GUI_BUTTON_PLAY_CLICK: (self.BUTTON_PLAY_CLICK.MaskFromSurface()),

      GUI_BUTTON_PAUSE_NORMAL: (self.BUTTON_PAUSE_NORMAL.MaskFromSurface()),
      GUI_BUTTON_PAUSE_HOVER: (self.BUTTON_PAUSE_HOVER.MaskFromSurface()),
      GUI_BUTTON_PAUSE_CLICK: (self.BUTTON_PAUSE_CLICK.MaskFromSurface()),

      GUI_BUTTON_OPTIONS_NORMAL: (self.BUTTON_OPTIONS_NORMAL.MaskFromSurface()),
      GUI_BUTTON_OPTIONS_HOVER: (self.BUTTON_OPTIONS_HOVER.MaskFromSurface()),
      GUI_BUTTON_OPTIONS_CLICK: (self.BUTTON_OPTIONS_CLICK.MaskFromSurface()),

      GUI_BUTTON_CHECKBOX_ON: (self.CHECKBOX_MUSIC_ON.LoadGameIamge()),
      GUI_BUTTON_CHECKBOX_OFF: (self.CHECKBOX_MUSIC_OFF.LoadGameIamge())
    }
    return self.powerupTypes[self.gui_type]

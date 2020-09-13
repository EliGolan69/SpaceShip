from Const import *
from Images import *
from UIControls import *

class GUIObj():
  def __init__(self, engine_game, engine_window, sound_obj):
    self.engine_game = engine_game
    self.engine_window = engine_window
    self.sound_obj = sound_obj
    self.play_again = False
    #self.engine_game.mouse.set_visible(False)
    #self.handPointer = GameIamge(engine_game, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_HAND_POINTER)
    #self.handPointerImage = self.handPointer.LoadGameIamge()
    self.screenWidth, self.screenHeight = self.engine_game.display.get_surface().get_size()
    self.guiInGameNavBar = InGameNavBar(engine_game, engine_window, self.sound_obj, 10, self.screenHeight - 118, 2,
                                        [GUI_BUTTON_PAUSE_NORMAL, GUI_BUTTON_OPTIONS_NORMAL],
                                        [GUI_BUTTON_PAUSE_HOVER, GUI_BUTTON_OPTIONS_HOVER],
                                        [GUI_BUTTON_PAUSE_CLICK, GUI_BUTTON_OPTIONS_CLICK]
                                        )
    self.windowsEvents = []

  def CheckEvents(self, engine_game, engine_window):
    self.windowsEvents = self.engine_game.event.get()
    for event in self.windowsEvents:
       self.guiInGameNavBar.RunEvents(self.windowsEvents)

  def RunOnClickEvents(self):
    self.guiInGameNavBar.RunButtonsOnClick(self.windowsEvents)

  def GetWindowsEvents(self):
    return self.windowsEvents

  def draw(self):
    self.guiInGameNavBar.draw()
    #self.engine_window.blit(self.handPointerImage, (self.engine_game.mouse.get_pos()))

  def GetSoundEffect(self):
    self.guiInGameNavBar.get_stop_sound()

  def CreatePlayAgain(self):
    self.PlayAgain = False
    PlayObj = PlayAgainGUI
    self.PlayObj = PlayAgainGUI(self.engine_game, self.engine_window)
    self.PlayAgain = self.PlayObj.ShowGUI()



  def GetPlayagain(self):
    return self.PlayAgain

class InGameNavBar(NavBar):
  """[GUI_BUTTON_PAUSE_NORMAL, GUI_BUTTON_OPTIONS_NORMAL],
     [GUI_BUTTON_PAUSE_HOVER, GUI_BUTTON_OPTIONS_HOVER],
     [GUI_BUTTON_PAUSE_CLICK, GUI_BUTTON_OPTIONS_CLICK]"""
  def __init__(self, engine_game, engine_window, sound_obj, x, y, number_of_buttons, button_types_normal, button_types_hover, button_types_click):
    super().__init__(engine_game, engine_window, x, y, number_of_buttons, button_types_normal, button_types_hover, button_types_click)
    self.sound_obj = sound_obj
    self.button_pause = self.buttons[0]
    self.button_option = self.buttons[1]
    self.button_pause.OnClick = self.button_pauseOnClick
    self.button_option.OnClick = self.button_optionOnClick
    self.sound_effect = False

  def get_stop_sound(self):
    return self.sound_effect

  def button_pauseOnClick(self):
    pauseGUI = PauseGUI(self.engine_game, self.engine_window)
    pauseGUI.ShowGUI()

  def button_optionOnClick(self):
    optionGUI = OptionGUI(self.engine_game, self.engine_window, self.sound_obj)
    optionGUI.ShowGUI()
    self.sound_obj.set_sound_effect(optionGUI.sound_gui.active)


class OptionGUI():
  def __init__(self, engine_game, engine_window, sound_obj):
    self.sound_obj = sound_obj
    self.engine_game, self.engine_window = engine_game, engine_window
    self.screenWidth, self.screenHeight = self.engine_game.display.get_surface().get_size()
    self.windowType = Window(self.engine_game, self.engine_window, (self.screenWidth / 2),
                             (self.screenHeight / 2), GUI_WINDOWS_SMALL)

    self.button_play = Button(engine_game, engine_window,
                              (self.windowType.x / 2),
                              (self.windowType.y / 2),
                              GUI_BUTTON_PLAY_NORMAL, GUI_BUTTON_PLAY_HOVER, GUI_BUTTON_PLAY_CLICK)
    self.button_play.x = (self.screenWidth / 2) - (self.button_play.imageWidth / 2) + 300
    self.button_play.y = (self.screenHeight / 2) + (self.button_play.imageHeight)

    self.mainFont = self.engine_game.font.SysFont("comicsans", 60)

    self.pause_bkImageObj = GameIamge(engine_game, IMAGE_FOLDER, FILE_NAME_BACK_GROUND_PAUSE, self.screenWidth,
                                      self.screenHeight)
    self.bkImage = self.pause_bkImageObj.GetScaleIamge()
    self.button_play.OnClick = self.button_playOnClick

    self.labelFont = self.engine_game.font.SysFont("comicsans", 40)

    self.label_music = self.labelFont.render("Music", 1, WHITE)
    self.label_sound = self.labelFont.render("Sound", 1, WHITE)
    self.music_gui = CheckBox(engine_game, engine_window, self.button_play.x, (self.windowType.y / 2)+30, GUI_BUTTON_CHECKBOX_ON, GUI_BUTTON_CHECKBOX_OFF, engine_game.mixer.music.get_busy())
    self.sound_gui = CheckBox(engine_game, engine_window, self.button_play.x, self.music_gui.y+90, GUI_BUTTON_CHECKBOX_ON, GUI_BUTTON_CHECKBOX_OFF, self.sound_obj.get_sound_effect())

    self.music_gui.OnClick = self.music_guiOnClick
    self.sound_gui.OnClick = self.sound_guiOnClick

    image_line = GameIamge(self.engine_game, IMAGE_FOLDER + IMAGE_FOLDER_GUI, FILE_NAME_SMALL_LINE, 500 ,10)
    self.small_line_2 = image_line.GetScaleIamge()
    self.small_line_1 = image_line.GetScaleIamge()

  def music_guiOnClick(self):
      if self.music_gui.active:
        self.engine_game.mixer.music.play()
      else:
         self.engine_game.mixer.music.stop()

  def sound_guiOnClick(self):
    if self.sound_gui.active:
      self.sound_obj.set_sound_effect(True)
    else:
      self.sound_obj.set_sound_effect(False)

  def button_playOnClick(self):
      return True

  def ShowGUI(self):
       clock = self.engine_game.time.Clock()
       runProcess = True
       while runProcess:
           clock.tick(60)
           windows_events = self.engine_game.event.get()
           self.engine_window.blit(self.bkImage, (0, 0))
           self.engine_window.blit(self.windowType.image, ((self.screenWidth / 2) - (self.windowType.imageWidth / 2),
                                                           (self.screenHeight / 2) - (self.windowType.imageHeight / 2)))
           self.button_play.RunEvents(windows_events)
           self.button_play.draw()

           self.engine_window.blit(self.label_music, (self.windowType.x/2-70, self.music_gui.y+17))
           self.engine_window.blit(self.small_line_1, (self.windowType.x/2, self.music_gui.y + 45))

           self.engine_window.blit(self.label_sound, (self.windowType.x/2-70, self.music_gui.y + 107))
           self.engine_window.blit(self.small_line_2, (self.windowType.x / 2, self.music_gui.y + 135))

           self.music_gui.RunEvents(windows_events)
           self.sound_gui.RunEvents(windows_events)
           self.music_gui.draw()
           self.sound_gui.draw()
           self.music_gui.RunOnClick()
           self.sound_gui.RunOnClick()
           self.engine_game.display.update()
           if self.button_play.OnMouseClick:
               runProcess = False

           for event in windows_events:
              if event.type == self.engine_game.QUIT:
                runProcess = False
                self.engine_game.quit()


class PauseGUI():
    def __init__(self, engine_game, engine_window):
      self.engine_game, self.engine_window = engine_game, engine_window
      self.screenWidth, self.screenHeight = self.engine_game.display.get_surface().get_size()
      self.windowType = Window(self.engine_game, self.engine_window, (self.screenWidth/ 2),
                              (self.screenHeight/ 2), GUI_WINDOWS_SMALL)
      self.button_play = Button(engine_game, engine_window,
                               (self.windowType.x/2),
                               (self.windowType.y/2) ,
                               GUI_BUTTON_PLAY_NORMAL, GUI_BUTTON_PLAY_HOVER, GUI_BUTTON_PLAY_CLICK)
      self.button_play.x = (self.screenWidth/ 2) - (self.button_play.imageWidth/2)
      self.button_play.y = (self.screenHeight/ 2) - (self.button_play.imageHeight)
      self.mainFont = self.engine_game.font.SysFont("comicsans", 60)
      self.pause_bkImageObj = GameIamge(engine_game, IMAGE_FOLDER, FILE_NAME_BACK_GROUND_PAUSE,  self.screenWidth, self.screenHeight)
      self.bkImage = self.pause_bkImageObj.GetScaleIamge()
      self.button_play.OnClick = self.button_playOnClick

    def button_playOnClick(self):
      return True

    def ShowGUI(self):
       label_play = self.mainFont.render("Continue Playing", 1, WHITE)
       clock = self.engine_game.time.Clock()
       runProcess = True
       while runProcess:
           clock.tick(60)
           windows_events = self.engine_game.event.get()
           self.engine_window.blit(self.bkImage, (0, 0))
           self.engine_window.blit(self.windowType.image, ((self.screenWidth / 2) - (self.windowType.imageWidth / 2),
                                                           (self.screenHeight / 2) - (self.windowType.imageHeight / 2)))
           self.engine_window.blit(label_play, ((self.screenWidth / 2) - (label_play.get_width() / 2), (self.screenHeight / 2) + 40))
           self.button_play.RunEvents(windows_events)
           self.button_play.draw()
           self.engine_game.display.update()
           if self.button_play.OnMouseClick:
               runProcess = False

           for event in windows_events:
              if event.type == self.engine_game.QUIT:
                runProcess = False
                self.engine_game.quit()


class PlayAgainGUI():
  def __init__(self, engine_game, engine_window):
    self.engine_game, self.engine_window = engine_game, engine_window
    self.screenWidth, self.screenHeight = self.engine_game.display.get_surface().get_size()
    self.windowType = Window(self.engine_game, self.engine_window, (self.screenWidth / 2),
                             (self.screenHeight / 2), GUI_WINDOWS_SMALL)
    self.button_play = Button(engine_game, engine_window,
                              (self.windowType.x / 2),
                              (self.windowType.y / 2),
                              GUI_BUTTON_PLAY_NORMAL, GUI_BUTTON_PLAY_HOVER, GUI_BUTTON_PLAY_CLICK)
    self.button_play.x = (self.screenWidth / 2) - (self.button_play.imageWidth / 2)
    self.button_play.y = (self.screenHeight / 2) - (self.button_play.imageHeight)
    self.mainFont = self.engine_game.font.SysFont("comicsans", 60)
    self.pause_bkImageObj = GameIamge(engine_game, IMAGE_FOLDER, FILE_NAME_BACK_GROUND_PAUSE, self.screenWidth,
                                      self.screenHeight)
    self.bkImage = self.pause_bkImageObj.GetScaleIamge()
    self.button_play.OnClick = self.button_playOnClick


  def button_playOnClick(self):
    start_game = True

  def ShowGUI(self):
    label_play = self.mainFont.render("Play Again", 1, WHITE)
    clock = self.engine_game.time.Clock()
    runProcess = True
    while runProcess:
      clock.tick(60)
      windows_events = self.engine_game.event.get()
      self.engine_window.blit(self.bkImage, (0, 0))
      self.engine_window.blit(self.windowType.image, ((self.screenWidth / 2) - (self.windowType.imageWidth / 2),
                                                      (self.screenHeight / 2) - (self.windowType.imageHeight / 2)))
      self.engine_window.blit(label_play,
                              ((self.screenWidth / 2) - (label_play.get_width() / 2), (self.screenHeight / 2) + 40))
      self.button_play.RunEvents(windows_events)
      self.button_play.draw()
      self.engine_game.display.update()
      if self.button_play.OnMouseClick:
        runProcess = False
        return True
      for event in windows_events:
        if event.type == self.engine_game.QUIT:
          runProcess = False
          self.engine_game.quit()
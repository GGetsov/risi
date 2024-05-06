import win32api, win32gui, win32con
import pygame
from pygame._sdl2 import Window as Sdl2Win

class Size():
  def __init__(self) -> None:
    # self.x = 96
    # self.y = 96
    self.x = 64
    self.y = 64

class Screen():
  def __init__(self, win_size: Size) -> None:
    # remove titlebar and border
    self.real = pygame.display.set_mode((win_size.x, win_size.y), pygame.NOFRAME)

    # get screen size
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
    work_area = monitor_info.get("Work")
    self.width = work_area[2]
    self.height = work_area[3]

class Position():
  def __init__(self, screen: Screen, win_size: Size, window: Sdl2Win) -> None:
    self.max_x = screen.width - win_size.x
    self.max_y = screen.height - win_size.y
    self.x = 0
    self.y = self.max_y


class Window():
  def __init__(self, screen: Screen) -> None:
    self.size = Size()
    self.real = Sdl2Win.from_display_module()
    self.pos = Position(screen, win_size=self.size, window=self.real)
    
    # hwnd is used for transparancy and placing on top
    self.hwnd = pygame.display.get_wm_info()["window"]
    self.place_on_top()

  def move(self, x: int, y: int):
    self.real.position = (x, y)
    self.place_on_top()

  def place_on_top(self):
    win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


screen = Screen(win_size=Size())
win = Window(screen)



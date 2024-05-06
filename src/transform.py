from types import SimpleNamespace
import win32api

# trans = SimpleNamespace()

# get screen size
monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")

# screen = dict(
#   width = work_area[2], 
#   height = work_area[3]
# )
#
# win = dict(
#   width = 96,
#   height = 96,
#   pos = dict(
#     max_x = screen.width - win.width
#   )
# )
#
# # set window size
# trans.win.width = 96
# trans.win.height = 96
#
# # window position
# trans.win.pos.max_x = trans.screen.width - trans.win.width
# trans.win.pos.x = 0
# trans.win.pos.max_y = trans.screen.height - trans.win.height
# trans.win.pos.y = trans.screen.height - trans.win.height
# # 1 means facing right, -1 - left
# trans.win.pos.x_direction = 1

class Screen():
  def __init__(self) -> None:
    # get screen size
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
    work_area = monitor_info.get("Work")
    self.width = work_area[2]
    self.height = work_area[3]

class Size():
  def __init__(self) -> None:
    self.x = 96
    self.y = 96

class Position():
  def __init__(self, screen: Screen, win_size: Size) -> None:
    self.max_x = screen.width - win_size.x
    self.max_y = screen.height - win_size.y
    self.x = 0
    self.y = self.max_y
    # 1 means facing right, -1 - left
    self.x_direction = 1

class Window():
  def __init__(self, screen: Screen) -> None:
    self.size = Size()
    self.pos = Position(screen, win_size=self.size)

screen = Screen()
win = Window(screen)

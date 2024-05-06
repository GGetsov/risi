import pygame
import win32gui, win32con, win32api

from src.states import Idle
from src.transform import screen, win

# remove background/add tranparency
background_color = (255,255,255)
win32gui.SetWindowLong(win.hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(win.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(win.hwnd, win32api.RGB(*background_color), 0, win32con.LWA_COLORKEY)

win.move(win.pos.x, win.pos.y)
#set on top
win32gui.SetWindowPos(win.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

from src.states import Idle

current_state = Idle(facing_left=False)

pygame.init()
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if current_state.should_change_state():
    current_state = current_state.get_next_state()

  current_state.on_update()

  # pygame.display.flip()
  clock.tick(30)

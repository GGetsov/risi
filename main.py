import pygame
from pygame._sdl2 import Window
import win32gui, win32con, win32api
import random

from src.states import Idle
from src.transform import screen, win

background_color = (255,255,255)
(window_width, window_height) = (100, 100)
(x_scale,y_scale) = (window_width, window_height)

# remove titlebar and border
screen = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
window = Window.from_display_module()

# get screen size
monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
(screen_width, screen_height) = (work_area[2], work_area[3])

# remove background/add tranparency
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*background_color), 0, win32con.LWA_COLORKEY)

screen.fill(background_color)
image = pygame.image.load("./sprites/risi.png") 
image = pygame.transform.scale(image,(x_scale,y_scale))

window.position = (win.pos.x, win.pos.y)
#set on top
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

screen.fill(background_color)
screen.blit(image,(0,0))

pygame.display.flip()

from src.states import Idle

current_state = Idle()

pygame.init()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if current_state.should_change_state():
    current_state = current_state.get_next_state()

  current_state.on_update()

  screen.fill(background_color)
  screen.blit(image,(0,0))

  pygame.display.flip()

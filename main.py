import pygame
import win32gui, win32con, win32api

from src.states import Stand
from src.transform import screen, win
from src.path import resource_path

logo = pygame.image.load(resource_path('sprites\\bread_5.png'))
pygame.display.set_icon(logo)

# remove background/add tranparency
background_color = (255,255,255)
win32gui.SetWindowLong(win.hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(win.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(win.hwnd, win32api.RGB(*background_color), 0, win32con.LWA_COLORKEY)

# win.move(win.pos.x, win.pos.y)

current_state = Stand(facing=False)

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

  clock.tick(30)

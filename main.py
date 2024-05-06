import pygame
import win32gui, win32con, win32api

from src.states import Idle
from src.transform import screen, win

background_color = (255,255,255)

# remove background/add tranparency
win32gui.SetWindowLong(win.hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(win.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(win.hwnd, win32api.RGB(*background_color), 0, win32con.LWA_COLORKEY)

image = pygame.image.load("./sprites/risi.png") 
image_size_in_px = 32
image = pygame.transform.scale_by(image,win.size.x/image_size_in_px)

win.move(win.pos.x, win.pos.y)
#set on top
win32gui.SetWindowPos(win.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

screen.real.fill(background_color)
screen.real.blit(image,(0,0))

pygame.display.flip()

from src.states import Idle

current_state = Idle()

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

  # screen.fill(background_color)
  # screen.blit(image,(0,0))

  # pygame.display.flip()
  clock.tick(60)

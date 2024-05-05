from types import TracebackType
import pygame
from pygame._sdl2 import Window
import win32gui, win32con, win32api
import random

background_color = (255,255,255)
(window_width, window_height) = (100, 100)
(x_scale,y_scale) = (window_width, window_height)

states = ["idle", "walking", "busy", "waiting"]
current_state = "idle"

# remove titlebar and border
screen = pygame.display.set_mode((window_width, window_height), pygame.NOFRAME)
window = Window.from_display_module()

# get screen size
monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
(screen_width, screen_height) = (work_area[2], work_area[3])

x = 0
y = screen_height - window_width
destination = 0
step = 0

# remove background/add tranparency
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*background_color), 0, win32con.LWA_COLORKEY)

screen.fill(background_color)
image = pygame.image.load("./sprites/risi.png") 
image = pygame.transform.scale(image,(x_scale,y_scale))

window.position = (x, y)
#set on top
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

screen.fill(background_color)
screen.blit(image,(0,0))

pygame.display.flip()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if current_state == "waiting":
    current_state = states[random.randint(0,1)]
    print(current_state)

  if current_state == "idle":
    current_state = "busy"
    pygame.time.wait(500)
    current_state = "waiting"

  if current_state == "walking":
    destination = random.randint(0, screen_width - window_width)
    if x > destination: step = -1 
    else: step = 1
    current_state = "moving"
    print(current_state)

  if current_state == "moving":
    if x == destination: current_state = "waiting"
    else: x += step
    pygame.time.wait(10)
    window.position = (x, y)
    #set on top
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
  
  screen.fill(background_color)
  screen.blit(image,(0,0))

  pygame.display.flip()

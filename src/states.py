import pygame
from pygame._sdl2 import Window
import win32gui, win32con, win32api
import random
from typing import TypeVar

from src.transform import screen, win

# remove titlebar and border
screen = pygame.display.set_mode((win.size.x, win.size.y), pygame.NOFRAME)
window = Window.from_display_module()

# remove background/add tranparency
hwnd = pygame.display.get_wm_info()["window"]

TState = TypeVar("TState", bound="State")

class State:
  def __init__(self) -> None:...
  def on_update(self) -> None:...
  def should_change_state(self) -> bool: ...
  def get_next_state(self) -> TState: ... 

class Idle(State):
  def __init__(self) -> None:
    self.starting_time = pygame.time.get_ticks()

  def should_change_state(self) -> bool:
    return (pygame.time.get_ticks() - self.starting_time >= 5000)
  
  def get_next_state(self):
    return Walking()


class Walking(State):
  def __init__(self) -> None:
    self.destination = random.randint(0, win.pos.max_x)
    self.x = win.pos.x 
    if (self.x > self.destination): self.step = -1 
    else: self.step = 1

  def on_update(self) -> None:
    self.x += self.step
    win.move(self.x, win.pos.max_y)

  def should_change_state(self) -> bool:
    return self.x == self.destination 
  
  def get_next_state(self):
    win.pos.x = self.x
    return Idle()

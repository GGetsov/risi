import pygame
from pygame._sdl2 import Window
import win32gui, win32con, win32api
import random
from typing import TypeVar

from src.transform import  screen, win
from src.animation import draw_frame, idle, walking_frames

#direction values
left = True
right = False

TState = TypeVar("TState", bound="State")

class State:
  def __init__(self) -> None:...
  def on_update(self) -> None:...
  def should_change_state(self) -> bool: ...
  def get_next_state(self) -> TState: ... 

class Idle(State):
  def __init__(self, facing_left: bool) -> None:
    self.starting_time = pygame.time.get_ticks()
    draw_frame(idle, facing_left)

  def should_change_state(self) -> bool:
    return (pygame.time.get_ticks() - self.starting_time >= 500)
  
  def get_next_state(self):
    return Walking()

class Walking(State):
  def __init__(self) -> None:
    self.destination = random.randint(0, win.pos.max_x)
    self.x = win.pos.x 
    self.step = 4
    # self.step = 3
    if (self.x > self.destination): 
      self.direction = left
      self.step *= -1
    else: 
      self.direction = right
    self.current_frame = 0
    
  def on_update(self) -> None:
    self.x += self.step
    win.move(self.x, win.pos.max_y)
    image = walking_frames[self.current_frame]
    draw_frame(image, self.direction)
    self.current_frame += 1
    if self.current_frame == len(walking_frames): self.current_frame = 0
    

  def should_change_state(self) -> bool:
    # return self.x == self.destination 
    if self.step > 0: return self.x >= self.destination
    return self.x <= self.destination
  
  def get_next_state(self):
    win.pos.x = self.x
    return Idle(facing_left=self.direction)

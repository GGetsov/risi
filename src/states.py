import pygame
from pygame._sdl2 import Window
import win32gui, win32con, win32api
import random
from typing import TypeVar

from src.transform import  screen, win

background_color = (255,255,255)
image_size_in_px = 32
scaling_factor = win.size.x/image_size_in_px

def load_sprite(name: str):
  return pygame.transform.scale_by(pygame.image.load('./sprites/'+name+'.png'),scaling_factor)

def load_animation(name:str, frames: int):
  animation = []
  for i in range(frames):
    animation.append(load_sprite(name + str(i+1)))
  return animation

def draw_frame(image: pygame.Surface):
  screen.real.fill(background_color)
  screen.real.blit(image,(0,0))
  pygame.display.flip()

idle = load_sprite("idle")

walking_frames = load_animation('walking_', 8)

TState = TypeVar("TState", bound="State")

class State:
  def __init__(self) -> None:...
  def on_update(self) -> None:...
  def should_change_state(self) -> bool: ...
  def get_next_state(self) -> TState: ... 

class Idle(State):
  def __init__(self) -> None:
    self.starting_time = pygame.time.get_ticks()
    draw_frame(idle)

  def should_change_state(self) -> bool:
    return (pygame.time.get_ticks() - self.starting_time >= 500)
  
  def get_next_state(self):
    return Walking()

class Walking(State):
  def __init__(self) -> None:
    self.destination = random.randint(0, win.pos.max_x)
    self.x = win.pos.x 
    if (self.x > self.destination): self.step = -3
    else: self.step = 3
    self.current_frame = 0
    
  def on_update(self) -> None:
    self.x += self.step
    win.move(self.x, win.pos.max_y)
    image = walking_frames[self.current_frame]
    draw_frame(image)
    self.current_frame += 1
    if self.current_frame == len(walking_frames): self.current_frame = 0
    

  def should_change_state(self) -> bool:
    # return self.x == self.destination 
    if self.step > 0: return self.x >= self.destination
    return self.x <= self.destination
  
  def get_next_state(self):
    win.pos.x = self.x
    return Idle()

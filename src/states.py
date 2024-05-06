import pygame
from pygame._sdl2 import Window
import win32gui, win32con, win32api
import random
from typing import TypeVar, Type

from src.transform import  screen, win
from src.animation import draw_frame, idle, walking_frames, bread_frames, eye_frames, lying_frames

#facing values
left = True
right = False

class IdleVars:
  def __init__(self, frame: pygame.Surface, time: int, state_list) -> None:
    self.frame = frame
    self.time = time
    self.state_list = state_list

class TransitionVars:
  def __init__(self, frames: list[pygame.Surface], state_list, first_frame:int = 0) -> None:
    self.first_frame = first_frame
    if first_frame != 0: 
      self.first_frame = len(frames) - 1
      self.last_frame = 0 - 1
      self.step = -1
    else:
      self.last_frame = len(frames)
      self.step = 1
    self.frames = frames
    self.state_list = state_list

TState = TypeVar("TState", bound="State")

class State:
  def __init__(self, facing: bool) -> None:
    self.facing = facing
  def on_update(self) -> None:...
  def should_change_state(self) -> bool: ...
  def get_next_state(self) -> TState: ... 

def random_state(state_list):
  return state_list[random.randint(0,len(state_list)-1)]

class IdleState(State):
  def __init__(self, facing: bool) -> None:
    self.facing = facing
    self.starting_time = pygame.time.get_ticks()
    self.vars = self.create_vars()
    draw_frame(self.vars.frame, facing)

  def create_vars(self) -> IdleVars:...
  def should_change_state(self) -> bool:
    return (pygame.time.get_ticks() - self.starting_time >= self.vars.time)
  
  def get_next_state(self):
    next_state = random_state(self.vars.state_list)(self.facing)
    return next_state

class TransitionState(State):
  def __init__(self, facing: bool) -> None:
    self.facing = facing
    self.vars = self.create_vars()
    self.current_frame = self.vars.first_frame

  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames=[], state_list=[])

  def on_update(self) -> None:
    draw_frame(self.vars.frames[self.current_frame], self.facing)
    self.current_frame += self.vars.step

  def should_change_state(self) -> bool:
    return self.current_frame == self.vars.last_frame

  def get_next_state(self):
    next_state = random_state(self.vars.state_list)(self.facing)
    return next_state

class Stand(IdleState):
  def create_vars(self) -> IdleVars:
    return IdleVars(idle, random.randint(1000, 3000), [Walking, ToBread])

class Walking(State):
  def __init__(self, facing) -> None:
    self.destination = random.randint(0, win.pos.max_x)
    self.x = win.pos.x 
    # self.step = 4
    self.step = 3
    if (self.x > self.destination): 
      self.facing = left
      self.step *= -1
    else: 
      self.facing = right
    self.current_frame = 0
    
  def on_update(self) -> None:
    self.x += self.step
    win.move(self.x, win.pos.max_y)
    image = walking_frames[self.current_frame]
    draw_frame(image, self.facing)
    self.current_frame += 1
    if self.current_frame == len(walking_frames): self.current_frame = 0
    
  def should_change_state(self) -> bool:
    # return self.x  self.destination 
    if self.step > 0: return self.x >= self.destination
    return self.x <= self.destination
  
  def get_next_state(self):
    win.pos.x = self.x
    return Stand(facing=self.facing)

class ToBread(TransitionState):
  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames=bread_frames, state_list=[Bread])
  
class Bread(IdleState):
  def create_vars(self) -> IdleVars:
    return IdleVars(bread_frames[4] ,random.randint(10000, 30000), state_list=[FromBread, CloseEyes])

class FromBread(TransitionState):
  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames=bread_frames, state_list=[Stand], first_frame=4)

class CloseEyes(TransitionState):
  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames = eye_frames, state_list=[ClosedEyes])

class ClosedEyes(IdleState):
  def create_vars(self) -> IdleVars:
    return IdleVars(frame=eye_frames[2], time=random.randint(5000,15000), state_list = [ClosedEyes, OpenEyes, Lie])

class OpenEyes(TransitionState):
  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames= eye_frames, first_frame= -1, state_list=[Bread, CloseEyes])

class Lie(TransitionState):
  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames = lying_frames, state_list=[Lying])

class Lying(IdleState):
  def create_vars(self) -> IdleVars:
    return IdleVars(frame=lying_frames[-1], time=random.randint(30000,60000), state_list = [Lying ,StandUp])

class StandUp(TransitionState):
  def create_vars(self) -> TransitionVars:
    return TransitionVars(frames = lying_frames, state_list=[ClosedEyes], first_frame = -1)

import pygame

from src.transform import win, screen

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

def draw_frame(image: pygame.Surface, flip_x: bool):
  screen.real.fill(background_color)
  screen.real.blit(pygame.transform.flip(image,flip_x,False),(0,0))
  pygame.display.flip()

idle = load_sprite("idle")
walking_frames = load_animation('walking_', 8)

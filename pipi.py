import pygame
import sys
from pygame.locals import *
import speech_recognition as sr 
import pyaudio
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Trial")
background_color =(0,254,9)
# red = (1)
RED = (255, 0, 0)
GREEN = (0, 255,0)
GREY = (90, 90, 90)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
screen.fill(background_color)
speed = 5
running = True
rect1x = 20
rect1y = 20
rect1w = 20
rect1h = 20
RECTANGLE1 = pygame.Rect(rect1x, rect1y, rect1w, rect1h)
rect = pygame.Rect(100, 60, 60, 50)
pygame.display.flip()

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False



keys = pygame.get_pressed()
if keys[pygame.K_RIGHT]:
    rect1x += speed
pygame.draw.rect(screen, RED, RECTANGLE1)
pygame.draw.rect(screen, RED, rect)
pygame.display.update()
pygame.quit()
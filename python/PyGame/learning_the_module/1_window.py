import pygame
import sys
from pygame.locals import *
# ===================================================================================
pygame.init()

clock_fps = pygame.time.Clock()
WINDOW_SIZE = (400, 400)
WIN = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("Just a window.")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock_fps.tick(60)

# ===================================================================================

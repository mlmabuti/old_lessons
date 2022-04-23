import pygame
import sys  # imports
from pygame.locals import *
pygame.init()  # initialize pygame

clock_fps = pygame.time.Clock()  # create clock speed / fps
WINDOW_SIZE = (800, 600)  # set window size
WIN = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # create window

pygame.display.set_caption("Rendering")  # window title/caption

player_img = pygame.image.load(
    "learning_the_module/Assets/Lasthe.png")  # import image

player_position = [50, 50]  # player location tracker

player_speed = 10

moving_left = False  # initial player movement
moving_right = False

player_y_momentum = 0
player_x_momentum = 0

# ===========================================================================================

player_rect = pygame.Rect(
    player_position[0], player_position[1], player_img.get_width(), player_img.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

# ===========================================================================================

while True:  # game loop

    # fills the screen with black again just before a new event is triggered
    WIN.fill((0, 0, 0))

    # render image in screen (x16,y16) note: y is inverted
    WIN.blit(player_img, (player_position))

    # if player is touching the y limit then bounce up
    # [1] refers to the y axis
    if player_position[1] > WINDOW_SIZE[1] - player_img.get_height():
        player_y_momentum = -player_y_momentum  # -y axis means to go up// BOUNCE
    else:
        # gravity, this will pull the player down to the y axis at 0.2 rate
        player_y_momentum += 0.2

    # players y will constantlt update based on the y momentum changes
    player_position[1] += player_y_momentum

    if moving_right:
        player_position[0] += player_speed  # 0 stands for x axis
    if moving_left:
        player_position[0] -= player_speed  # 0 stands for x axis

# ===========================================================================================

    player_rect.x = player_position[0]
    player_rect.y = player_position[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(WIN, (9, 0, 255), test_rect)
    else:
        pygame.draw.rect(WIN, (255, 255, 255), test_rect)

# ===========================================================================================
    for event in pygame.event.get():  # event listener
        if event.type == QUIT:  # close button on window
            pygame.quit()  # stop pygame
            sys.exit()  # stop script

        if event.type == KEYDOWN:  # on key press
            if event.key == K_RIGHT:  # RIGHT ARROW KEY
                moving_right = True
            if event.key == K_LEFT:  # LEFT ARROW KEY
                moving_left = True

        if event.type == KEYUP:  # on key release
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()  # updates the screen display
    clock_fps.tick(60)  # sets the fps

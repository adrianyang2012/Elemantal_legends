import pygame
import time
import os
from random import randint
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
i = 0
while running:

    time.sleep(0.01)
    if i < 255:
        i +=1
    elif i == 255:
        i-=255
    print(i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    r = randint(0,10)
    screen.fill((i, 255-i, 255-i))
    pygame.draw.circle(screen, (255-i, i, i), (i+r, i-r), 75)

    pygame.display.flip()

pygame.quit()

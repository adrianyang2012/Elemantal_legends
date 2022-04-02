import pygame
import time

from random import randint
pygame.init()

screen = pygame.display.set_mode([1000, 1000])

running = True
i = 1
t = 0
abs_i = 1
while running:

    if t == 0:
        i +=1
    if t == 1:
        i -=1
    if i == 255:
        t = 1
    if i == 0:
        t = 0
    abs_i +=1
    
    print(i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    r = randint(0,10)
    screen.fill((i,i,i))
    pygame.draw.circle(screen, (255, i, i), (abs_i+r, abs_i-r), 75)

    pygame.display.flip()

pygame.quit()

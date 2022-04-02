import pygame
import time

from random import randint
pygame.init()

screen = pygame.display.set_mode([1000, 1000])

running = True
i = 1
t = 0
abs_i = 1
b = 0
exploded = False
while running:
    time.sleep(0.01)
    if t == 0:
        i +=1
    if t == 1:
        i -=1
    if i == 255:
        t = 1
    if i == 0:
        t = 0
    abs_i +=1
    if abs_i == 900:
        exploded = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    r = randint(0,10)
    screen.fill((i,i,i))
    if exploded:
        b = int(abs_i/3)
    pygame.draw.circle(screen, (255, i, i), (abs_i+r, abs_i-r), 75+b)
    
    pygame.display.flip()

pygame.quit()

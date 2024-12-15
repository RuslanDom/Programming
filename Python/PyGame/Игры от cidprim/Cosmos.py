import pygame
from random import random, randint
pygame.init()

WIDTH = 1200
HEIGHT = 800
FPS = 60
display = pygame.display.set_mode((WIDTH, HEIGHT))
play = True
clock = pygame.time.Clock()

class Star:
    def __init__(self):
        objects.append(self)
        self.px = WIDTH//2
        self.py = HEIGHT//2
        self.speed = random() * 3
        r = 255
        g = randint(200, 255)
        b = randint(0, 255)
        self.color = [r, g, b]
        self.dx = random() - 0.5
        self.dy = random() - 0.5

    def update(self):
        self.px += self.dx * self.speed
        self.py += self.dy * self.speed
        if self.px > WIDTH or self.py > HEIGHT or self.px < 0 or self.py < 0:
            objects.remove(self)
    def draw(self):
        pygame.draw.aaline(display, self.color, (self.px, self.py), (self.px, self.py))

objects = []
for _ in range(1000):
    Star()
while play:
    display.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    for _ in range(1):
        Star()
    for obj in objects:
        obj.update()
    for obj in objects:
        obj.draw()
    pygame.display.update()
    clock.tick(FPS)



pygame.quit()
import pygame
from random import randint
pygame.init()

WIDTH = 1600
HEIGHT = 900
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Game rain")
FPS = 60
ON = True


class Rain:
    def __init__(self):
        self.px = randint(0, WIDTH)
        self.py = randint(0, HEIGHT)
        self.size = randint(1, 5)
        x = randint(0, 255)
        a = randint(0, 255)
        c = randint(0, 255)
        self.color = (x, a, c)
    def update(self):
        self.py += self.size * 2
        if self.py > HEIGHT:
            self.py = randint(-HEIGHT, 0)
    def draw(self):
        pygame.draw.circle(display, self.color, (self.px, self.py), self.size)
rain = []

for _ in range(1000):
    rain.append(Rain())




while ON:

    display.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False
            pygame.quit()
    for drop in rain:
        drop.update()
    for drop in rain:
        drop.draw()
    pygame.display.update()
    clock.tick(FPS)




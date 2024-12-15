import pygame
from random import randint
pygame.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
class Drop:
    def __init__(self):
        self.px, self.py = randint(0, WIDTH), randint(0, HEIGHT)
        self.size = randint(1, 3)

         # Игра цвета
        c = randint(0, 255)
        x = randint(0, 50)
        a = randint(0, 255)
        self.color = (x, a, c)


    def update(self):
        if self.py > HEIGHT and self.dy > HEIGHT:
             self.py = randint(-HEIGHT, 0)
        self.py += self.size * 3
        self.dy = self.py + 10

    def draw(self):

        pygame.draw.line(display, self.color, (self.px, self.py), (self.px, self.dy), self.size)
rain = []
for _ in range(1000):
    rain.append(Drop())
ON = True
while ON:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False

    for drop in rain:
         drop.update()
    display.fill('black')
    for drop in rain:
         drop.draw()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()






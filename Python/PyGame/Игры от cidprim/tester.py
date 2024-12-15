import pygame
import random
pygame.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
play = True

class Star:
    def __init__(self):
        stars.append(self)
        self.px = WIDTH//2
        self.py = HEIGHT//2
        self.speed = random.random() * 5
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = [r, g, b]
        self.dx = (random.random() - 0.5)
        self.dy = (random.random() - 0.5)
        self.size = random.randint(1, 3)

    def update(self):
        self.px += self.dx * self.speed
        self.py += self.dy * self.speed
        self.nx = self.px + self.dx * self.size * 3
        self.ny = self.py + self.dy * self.size * 3
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            stars.remove(self)
    def draw(self):
        pygame.draw.line(display, self.color, (self.px, self.py), (self.nx, self.ny), self.size)

stars = []

for _ in range(1000):
    for _ in range(random.randint(1, 2)):
        Star()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    display.fill('black')
    for _ in range(random.randint(1, 3)):
        Star()
    for star in stars:
        star.update()

    for star in stars:
        star.draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
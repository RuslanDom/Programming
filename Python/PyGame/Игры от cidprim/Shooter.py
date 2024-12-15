import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
play = True

class Bullet:
    def __init__(self, direct):
        bullets.append(self)
        self.px = WIDTH//2
        self.py = HEIGHT//2
        self.color = 'black'

        self.speed = 10
        # Создание катетов треугольника
        dx, dy = direct[0] - self.px, direct[1] - self.py
        # Находим гипотенузу этого треугольника, она укажет направление выстрела
        dist = (dx ** 2 + dy ** 2) ** 0.5
        # Создание едичного вектора направления выстрела катет делить на гипотенузу
        self.sx, self.sy = dx/dist * self.speed, dy/dist * self.speed
    def update(self):
        self.px += self.sx
        self.py += self.sy
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
    def draw(self):
        pygame.draw.circle(surface, self.color, (self.px, self.py), 2)

bullets = []


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos

            Bullet((mx, my))

    surface.fill('white')
    for bul in bullets:
        bul.update()

    for bul in bullets:
        bul.draw()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
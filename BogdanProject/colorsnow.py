# import pygame
# from random import randint
# pygame.init()
# width = 1280
# height = 1024
# clock = pygame.time.Clock()
# fps = 60
# display = pygame.display.set_mode((width, height))
#
# class SNOW:
#     def __init__(self, px, py):
#         snezinka.append(self)
#         self.px = px
#         self.py = py
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         self.color = (r, g, b)
#         self.size = randint(1, 5)
#
#
#
#     def update(self):
#         self.py += self.size
#         if self.py > height:
#             self.py = randint(- height, 0)
#     def draw(self):
#         pygame.draw.circle(display, self.color, (self.px, self.py), self.size)
#
#
# snezinka = []
#
# for _ in range(1000):
#     x = randint(0, width)
#     y = randint(0, height)
#     SNOW(x, y)
#
# play = True
# while play:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             play = False
#
#     display.fill('black')
#     for snez in snezinka:
#         snez.update()
#     for snez in snezinka:
#         snez.draw()
#
#     pygame.display.update()
#     clock.tick(fps)
# pygame.quit()
#
import pygame
from random import randint

pygame.init()
W = 1200
H = 800
win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
play = True
rain = []


class Rain:
    def __init__(self, x, y):
        rain.append(self)
        self.x = x
        self.y = y
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.color = [r, g, b]
        self.speed = 2
        self.size = randint(1, 5)
    def update(self):
        self.y += self.size * self.speed
        if self.y > H:
            rain.remove(self)
            x = randint(0, W)
            y = randint(-100, 0)
            Rain(x, y)
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)


for _ in range(1000):
    x = randint(0, W)
    y = randint(-800, 0)
    Rain(x, y)


while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    win.fill("black")
    for r in rain:
        r.update()
    for r in rain:
        r.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()































# class Rain:
#     def __init__(self, x, y):
#         Play.rain.append(self)
#         self.x = x
#         self.y = y
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         self.color = [r, g, b]
#         self.speed = 2
#         self.size = randint(1, 5)
#     def update(self):
#         self.y += self.size * self.speed
#         if self.y > Play.H:
#             Play.rain.remove(self)
#             x = randint(0, Play.W)
#             y = randint(-100, 0)
#             Rain(x, y)
#
#     def draw(self):
#         pygame.draw.circle(Play.win, self.color, (self.x, self.y), self.size)
#
# class Play:
#     pygame.init()
#     W = 1200
#     H = 800
#     win = pygame.display.set_mode((W, H))
#     clock = pygame.time.Clock()
#     play = True
#     rain = []
#     for i in range(1000):
#         x = randint(0, W)
#         y = randint(-100, 0)
#         R = Rain(x, y)
#     def start(self):
#         while Play.play:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     Play.play = False
#
#         for r in Play.rain:
#             r.update()
#         for r in Play.rain:
#             r.draw()
#         pygame.display.update()
#         Play.clock.tick(60)
#         Play().stop()
#     def stop(self):
#
#         if Play.play == False:
#             pygame.quit()
#
# game = Play()
# game.start()

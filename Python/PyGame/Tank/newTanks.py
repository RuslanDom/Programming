import pygame
import sys
pygame.init()
width = 1200
height = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Танки")
FPS = 60
clock = pygame.time.Clock()

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
class Tank:
    def __init__(self, color, px, py, direct, keylist):
        objects.append(self)
        self.type = "tank"

        self.color = color
        self.rect = pygame.Rect(px, py, 32, 32)
        self.direct = direct
        self.moveSpeed = 15

        self.keyLEFT = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyUP = keylist[2]
        self.keyDOWN = keylist[3]
        self.keySHOOT = keylist[4]




    def update(self):
        if keys[self.keyLEFT] and self.rect.centerx > 40:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT] and self.rect.centerx < 1160:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP] and self.rect.centery > 40:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN] and self.rect.centery < 760:
            self.rect.y += self.moveSpeed
            self.direct = 2
    def draw(self):
        pygame.draw.rect(display,self.color, self.rect)
        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(display, 'yellow', self.rect.center, (x, y), 4)
class Bullet:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

class Brick:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

objects = []
Tank("red", 500, 700, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP0))
Tank("blue", 700, 700, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
while True:
    display.fill((0,0,0))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for obj in objects:
        obj.update()
    for obj in objects:
        obj.draw()
    pygame.display.update()

    clock.tick(FPS)
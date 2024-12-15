import pygame
from random import randint
pygame.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
DIRECT = [[0, -1], [1, 0], [0, 1], [-1, 0]]
play = True
size = 32

class QI:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass


class Tank:
    def __init__(self, color, px, py, direct, keylist):
        objects.append(self)
        self.type = 'tank'
        self.color = color
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.speed = 3
        self.speedShoot = 10
        self.rank = 1
        self.HP = 3
        self.direct = direct
        self.keyUP = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyDOWN = keylist[2]
        self.keyLEFT = keylist[3]
        self.keySHOOT = keylist[4]
        self.shootTime = 0
        self.shootDelay = 60
    def update(self):
        oldX, oldY = self.rect.x, self.rect.y
        if keys[self.keyUP] and self.rect.centery > 0:
            self.rect.y -= self.speed
            self.direct = 0
        elif keys[self.keyRIGHT] and self.rect.centerx < WIDTH:
            self.rect.x += self.speed
            self.direct = 1
        elif keys[self.keyDOWN] and self.rect.centery < HEIGHT:
            self.rect.y += self.speed
            self.direct = 2
        elif keys[self.keyLEFT] and self.rect.centerx > 0:
            self.rect.x -= self.speed
            self.direct = 3

        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.x, self.rect.y = oldX, oldY

        if keys[self.keySHOOT] and self.shootTime == 0:
            dx = DIRECT[self.direct][0] * self.speedShoot
            dy = DIRECT[self.direct][1] * self.speedShoot
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, 1)
            self.shootTime = self.shootDelay
        if self.shootTime > 0:
            self.shootTime -= 1
    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)
        x = self.rect.centerx + DIRECT[self.direct][0] * 30
        y = self.rect.centery + DIRECT[self.direct][1] * 30
        pygame.draw.line(display, 'yellow', (self.rect.centerx, self.rect.centery), (x, y), 3)
    def damage(self, value):
        self.HP -= value
        if self.HP <= 0:
            objects.remove(self)

class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage


    def update(self):
        self.px += self.dx
        self.py += self.dy
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    bullets.remove(self)
                    obj.damage(self.damage)
                    break
    def draw(self):
        pygame.draw.circle(display, 'white', (self.px, self.py), 2)

class Bang:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass


class Block:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'block'
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.color = [r, g, b]
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.hp = 2
    def update(self):
        pass
    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)
        pygame.draw.rect(display, 'white', self.rect, 2)
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)




objects = []
bullets = []

Tank('blue', int(WIDTH * 0.25), HEIGHT//2, 0, (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a, pygame.K_SPACE))
Tank('red', int(WIDTH * 0.75), HEIGHT//2, 0, (pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_KP0))
for _ in range(200):
    x = randint(0, WIDTH//size - 1) * size
    y = randint(1, HEIGHT//size - 1) * size
    rect = pygame.Rect(x, y, size, size)
    fined = False
    for obj in objects:
        if rect.colliderect(obj.rect):
            fined = True
            break
    if not fined:
        Block(x, y)
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys = pygame.key.get_pressed()

    for bul in bullets:
        bul.update()
    for obj in objects:
        obj.update()
    display.fill('black')
    for bul in bullets:
        bul.draw()
    for obj in objects:
        obj.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
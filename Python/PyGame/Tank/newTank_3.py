import pygame
import sys
import random
pygame.init()

WIDTH = 1200
HEIGHT = 800
FPS = 60
DIRECT = [[0, -1], [1, 0], [0, 1], [-1, 0]]
size = 34

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Tank:
    def __init__(self, color, px, py, direct, keylist):
        objects.append(self)
        self.type = "tank"
        self.color = color
        self.rect = pygame.rect.Rect(px, py, 30, 30)
        self.direct = direct
        self.moveSpeed = 3
        self.HP = 5

        self.keyLEFT = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyUP = keylist[2]
        self.keyDOWN = keylist[3]
        self.keySHOOT = keylist[4]

        self.timeShoot = 0
        self.shootDelay = 60
        self.shootSpeed = 10


    def update(self):
        old_X, old_Y = self.rect.topleft

        if keys[self.keyUP] and self.rect.centery > 20:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyRIGHT] and self.rect.centerx < WIDTH-20:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyDOWN] and self.rect.centery < HEIGHT - 20:
            self.rect.y += self.moveSpeed
            self.direct = 2
        elif keys[self.keyLEFT] and self.rect.centerx > 20:
            self.rect.x -= self.moveSpeed
            self.direct = 3

        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.topleft = old_X, old_Y

        if keys[self.keySHOOT] and self.timeShoot == 0:
            dx = DIRECT[self.direct][0] * self.shootSpeed
            dy = DIRECT[self.direct][1] * self.shootSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, 1)
            self.timeShoot = self.shootDelay
        if self.timeShoot > 0:
            self.timeShoot -= 1


    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)
        x = self.rect.centerx + DIRECT[self.direct][0] * 30
        y = self.rect.centery + DIRECT[self.direct][1] * 30
        pygame.draw.line(display, 'white', self.rect.center, (x, y), 5)

    def damage(self, value):
        self.HP -= value
        if self.HP <= 0:
            objects.remove(self)

class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px = px
        self.py = py
        self.dx, self.dy = dx, dy
        self.damage = damage


    def update(self):
        self.px += self.dx
        self.py += self.dy
        if self.px > WIDTH or self.px < 0 or self.py > HEIGHT or self.py < 0:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    bullets.remove(self)
                    obj.damage(self.damage)
                    break


    def draw(self):
        pygame.draw.circle(display, 'white', (self.px, self.py), 3)


class Brick:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'brick'
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.HP = 1
    def update(self):
        pass
    def draw(self):
        pygame.draw.rect(display, (51, 9, 9), self.rect)
        pygame.draw.rect(display, 'grey', self.rect, 2)

    def damage(self, value):
        self.HP -= value
        if self.HP <= 0:
            objects.remove(self)

objects = []
bullets = []

Tank('yellow', 300, 300, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank('red', 700, 300, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL))



# --------------------------------Случайное создание объектов на экране------------------------------------
for _ in range(100):
    while True:
        x = random.randint(0, WIDTH//size - 1) * size
        y = random.randint(0, HEIGHT//size - 1) * size
        rect = pygame.rect.Rect(x, y, size, size)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    Brick(x, y, size)

    
ON = True
while ON:
    display.fill('black')
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False
            sys.exit()
    for bul in bullets:
        bul.update()
    for bul in bullets:
        bul.draw()
    for obj in objects:
        obj.update()
    for obj in objects:
        obj.draw()
    pygame.display.update()
    clock.tick(FPS)
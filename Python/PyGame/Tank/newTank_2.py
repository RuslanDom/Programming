import pygame
import sys

pygame.init()
pygame.display.set_caption("Танки на 3")
font_ = pygame.font.Font(None, 10)
WIDTH = 1200
HEIGHT = 800
FPS = 60
clock = pygame.time.Clock()
DIRECT = [[0, -1], [1, 0], [0, 1], [-1, 0]]
display = pygame.display.set_mode((WIDTH, HEIGHT))

"""--------------------------------------------------------Classes--------------------------------------------------------"""

class Tank:
    def __init__(self, color, px, py, direct, keylist):
        objects.append(self)
        self.type = "tank"
        self.color = color
        self.rect = pygame.Rect(px, py, 32, 32)
        self.direct = direct

        self.bulletDamage = 1
        self.bulletSpeed = 10
        self.shootTime = 0
        self.shootDelay = 60

        self.keyLEFT = keylist[0]
        self.keyRight = keylist[1]
        self.keyUP = keylist[2]
        self.keyDown = keylist[3]
        self.keySHOOT = keylist[4]
        self.moveSpeed = 5
        self.HP = 5

    def update(self):
        if keys[self.keyLEFT] and self.rect.centerx > 20:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRight] and self.rect.centerx < 1180:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP] and self.rect.centery > 20:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDown] and self.rect.centery < 780:
            self.rect.y += self.moveSpeed
            self.direct = 2
        if keys[self.keySHOOT] and self.shootTime == 0:
            dx = DIRECT[self.direct][0] * self.bulletSpeed
            dy = DIRECT[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shootTime = self.shootDelay
        if self.shootTime > 0:
            self.shootTime -= 1
    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

        x = self.rect.centerx + DIRECT[self.direct][0] * 30
        y = self.rect.centery + DIRECT[self.direct][1] * 30

        pygame.draw.line(display, "white", self.rect.center, (x, y), 5)
    def damage(self, value):
        self.HP -= value
        if self.HP <= 0:
            objects.remove(self)
class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.px = px
        self.py = py
        self.dx = dx
        self.dy = dy
        self.damage = damage
        self.parent = parent
    def update(self):
        self.px += self.dx
        self.py += self.dy
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    break
    def draw(self):
        pygame.draw.circle(display, 'yellow', (self.px, self.py), 2 )

class Brick:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

objects = []
bullets = []
Tank('green', 300, 300, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP0))
Tank('red', 600, 300, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank('blue', 450, 600, 0, (pygame.K_KP4, pygame.K_KP6, pygame.K_KP8, pygame.K_KP5, pygame.K_KP_PLUS))
ON = True
while ON:
    display.fill((0, 0, 0))

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

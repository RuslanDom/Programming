import pygame
import sys
from random import randint

pygame.init()

WIDTH = 1200
HEIGHT = 800
FPS = 60
DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
clock = pygame.time.Clock()
sizeTank = 28
size = 32
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TANK")
font_ = pygame.font.Font(None, 30)
font_2 = pygame.font.Font(None, 100)

imgTank = [pygame.image.load('image/tank1.png'),
           pygame.image.load('image/tank2.png'),
           pygame.image.load('image/tank3.png'),
           pygame.image.load('image/tank4.png'),
           pygame.image.load('image/tank5.png'),
           pygame.image.load('image/tank6.png'),
           pygame.image.load('image/tank7.png'),
           pygame.image.load('image/tank8.png')]
imgBrick = pygame.image.load('image/block_brick.png')
imgBang = [pygame.image.load('image/bang1.png'),
           pygame.image.load('image/bang2.png'),
           pygame.image.load('image/bang3.png')]
ON = True


class UI:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        i = 1
        for obj in objects:
            if obj.type == 'tank':

                display.blit(font_.render("PLAYER " + str(i) + ": " + str(obj.HP), True, obj.color), (250 + i * 200, 10))
                i += 1

class Tank:
    def __init__(self, color, px, py, direct, keylist):
        objects.append(self)
        self.type = "tank"
        self.color = color
        self.rect = pygame.rect.Rect(px, py, sizeTank, sizeTank)
        self.direct = direct
        self.HP = 5
        self.speed = 3
        self.bulletSpeed = 10
        self.shootTime = 0
        self.shootDelay = 60

        self.keyLEFT = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyUP = keylist[2]
        self.keyDOWN = keylist[3]
        self.keySHOOT = keylist[4]

        self.rank = 0
        self.image = pygame.transform.rotate(imgTank[self.rank], - self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        old_X, old_Y = self.rect.topleft

        self.rank = 0
        self.image = pygame.transform.rotate(imgTank[self.rank], - self.direct * 90 )
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center=self.rect.center)

        if keys[self.keyUP] and self.rect.centery > 20:
            self.rect.y -= self.speed
            self.direct = 0
        elif keys[self.keyRIGHT] and self.rect.centerx < 1180:
            self.rect.x += self.speed
            self.direct = 1
        elif keys[self.keyDOWN] and self.rect.centery < 780:
            self.rect.y += self.speed
            self.direct = 2
        elif keys[self.keyLEFT] and self.rect.centerx > 20:
            self.rect.x -= self.speed
            self.direct = 3
        for obj in objects:
            if obj != self and obj.type != 'bang' and self.rect.colliderect(obj.rect):
                self.rect.topleft = old_X, old_Y

        if keys[self.keySHOOT] and self.shootTime == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, 1)
            self.shootTime = self.shootDelay
        if self.shootTime > 0:
            self.shootTime -= 1
    def draw(self):
        # pygame.draw.rect(display, self.color, self.rect)
        display.blit(self.image, self.rect)

        # x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        # y = self.rect.centery + DIRECTS[self.direct][1] * 30
        # pygame.draw.line(display, 'white', self.rect.center, (x, y), 3)
    def damage(self, value):
        self.HP -= value
        if self.HP == 0:
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
        if self.px < 0 or self.px > 1200 or self.py < 0 or self.py > 800:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj. rect.collidepoint(self.px, self.py):
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    obj.damage(self.damage)


    def draw(self):
        pygame.draw.circle(display, 'white', (self.px, self.py), 2)


class Bang:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'
        self.img_I = 0
        self.px, self.py = px, py
    def update(self):
        self.img_I += 0.1
        if self.img_I > 3:
            objects.remove(self)
    def draw(self):
        image = imgBang[int(self.img_I)]
        rect = image.get_rect(center=(self.px, self.py))
        display.blit(image, rect)


class Block:
    def __init__(self, color, px, py, hp):
        objects.append(self)
        self.type = 'block'
        self.color = color
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.hp = hp
    def update(self):
        pass
    def draw(self):
        display.blit(imgBrick, self.rect)
        # pygame.draw.rect(display, self.color, self.rect)
        # pygame.draw.rect(display, 'grey', self.rect, 3)
    def damage(self, value):
        self.hp -= value
        if self.hp == 0:
            objects.remove(self)

objects = []
bullets = []
ui = UI()

Tank("blue", 200, 600, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank("yellow", 1000, 600, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP0))

for _ in range(150):
    while True:
        x = randint(0, WIDTH//size - 1) * size
        y = randint(1, HEIGHT//size - 1) * size
        rect = pygame.Rect(x, y, size, size)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect):
                fined = True
        if not fined:
            break
    Block('brown', x, y, 1)



while ON:
    display.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    for bul in bullets:
        bul.update()
    for obj in objects:
        obj.update()
    ui.update()

    for bul in bullets:
        bul.draw()
    for obj in objects:
        obj.draw()
    ui.draw()

    pygame.display.update()
    clock.tick(FPS)
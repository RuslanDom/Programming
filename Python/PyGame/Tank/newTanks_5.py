import pygame
import sys
from random import randint
from threading import Timer
pygame.init()

WIDTH = 1200
HEIGHT = 800
FPS = 60
clock = pygame.time.Clock()
DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
ON = True
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Good game')
font_ = pygame.font.Font(None, 30)
size = 32

imgTank = [pygame.image.load('image/tank1.png'),
           pygame.image.load('image/tank5.png'),
           pygame.image.load('image/tank7.png'),
           pygame.image.load('image/tank6.png'),
           pygame.image.load('image/tank2.png'),
           pygame.image.load('image/tank3.png'),
           pygame.image.load('image/tank4.png'),
           pygame.image.load('image/tank8.png'),
           pygame.image.load('image/tank8.png')]
imgBang = [pygame.image.load('image/bang1.png'),
           pygame.image.load('image/bang2.png'),
           pygame.image.load('image/bang3.png')]
imgBrick = pygame.image.load('image/block_brick.png')

imgStar = pygame.image.load('image/bonus_star.png')
imgHP = pygame.image.load('image/bonus_tank.png')

class UI:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        i = 1
        for obj in objects:
            if obj.type == 'tank':
                display.blit(font_.render('TANK: ' + str(i) + ' Health: ' + str(int(obj.HP)), True, obj.color), (200 + i * 200, 10))
            i += 1

class Tank:
    def __init__(self, color, px, py, direct, keylist):
        objects.append(self)
        self.type = 'tank'
        self.color = color
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.direct = direct
        self.keyLEFT = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyUP = keylist[2]
        self.keyDOWN = keylist[3]
        self.keySHOOT = keylist[4]
        self.tankSpeed = 2
        self.bulletSpeed = 10
        self.timeShoot = 0
        self.shootDelay = 60
        self.HP = 3
        self.rank = 0
        self.image = pygame.transform.rotate(imgTank[int(self.rank)], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        old_X, old_Y = self.rect.topleft


        if self.rank > 8: self.rank = 8
        if self.rank < 0: self.rank = 0
        self.image = pygame.transform.rotate(imgTank[int(self.rank)], -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.tankSpeed > 8:
            self.tankSpeed = 8

        if keys[self.keyLEFT] and self.rect.centerx > 20:
            self.rect.x -= self.tankSpeed
            self.direct = 3
        elif keys[self.keyRIGHT] and self.rect.centerx < 1180:
            self.rect.x += self.tankSpeed
            self.direct = 1
        elif keys[self.keyUP] and self.rect.centery > 20:
            self.rect.y -= self.tankSpeed
            self.direct = 0
        elif keys[self.keyDOWN] and self.rect.centery < 780:
            self.rect.y += self.tankSpeed
            self.direct = 2
        for obj in objects:
            if obj != self and obj.type != 'bang' and self.rect.colliderect(obj.rect):
                if obj.type == 'upgrade':
                    obj.inprovment(self)
                    objects.remove(obj)

                self.rect.topleft = old_X, old_Y

        if keys[self.keySHOOT] and self.timeShoot == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, 1)
            if self.shootDelay < 20:
                self.shootDelay = 20
            self.timeShoot = self.shootDelay
        if self.timeShoot > 0:
            self.timeShoot -= 1
    def draw(self):

        # pygame.draw.rect(display, self.color, self.rect)
        display.blit(self.image, self.rect)
        # x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        # y = self.rect.centery + DIRECTS[self.direct][1] * 30
        # pygame.draw.line(display, 'white', self.rect.center, (x, y), 3)
    def damage(self, value):
        self.HP -= value
        if self.HP <= 0:
            objects.remove(self)
class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.i = 0
        self.i += 1
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.rect = pygame.rect.Rect(px, py, 3, 3)
    def update(self):
        self.px += self.dx
        self.py += self.dy
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)


        else:
            # for en, bul in enumerate(bullets):
            #     if en == self.i and bul.rect.colliderect(self.rect):
            #         bullets.remove(self)

            for obj in objects:
                if obj != self.parent and obj.type != 'upgrade' and obj.type != 'bang' and obj.rect.collidepoint(self.px, self.py):
                    bullets.remove(self)
                    obj.damage(self.damage)
                    Bang(self.px, self.py)



    def draw(self):
        pygame.draw.rect(display, 'yellow', (self.px, self.py, 5, 5))


class Bang:
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'
        self.px, self.py = px, py
        self.bangInx = 0
    def update(self):
        self.bangInx += 0.1
        if self.bangInx > 3:
            objects.remove(self)
    def draw(self):
        self.image = imgBang[int(self.bangInx)]
        self.rect = self.image.get_rect(center=(self.px, self.py))
        display.blit(self.image, self.rect)


class Block:
    def __init__(self, px, py, hp):
        objects.append(self)
        self.type = 'block'
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.hp = hp
    def update(self):
        pass
    def draw(self):
        display.blit(imgBrick, self.rect)
        # pygame.draw.rect(display, 'blue', self.rect)
        # pygame.draw.rect(display, 'white', self.rect, 3)
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)

class Upgrade:
    def __init__(self, color, px, py):
        objects.append(self)
        self.type = 'upgrade'
        self.color = color
        self.rect = pygame.rect.Rect(px, py, size, size)
    def update(self):
        pass
    def draw(self):
        # pygame.draw.rect(display, self.color, self.rect)
        if self.color == 'green':
            rect = imgStar.get_rect(center=(self.rect.centerx, self.rect.centery))
            display.blit(imgStar, rect)
        if self.color == 'red':
            rect = imgHP.get_rect(center=(self.rect.centerx, self.rect.centery))
            display.blit(imgHP, rect)

    def damage(self, value):
        pass
    def inprovment(self, parent):
        if self.color == 'red':
            for obj in objects:
                if obj.type == 'tank':
                    parent.HP += 1
                    break
        if self.color == 'green':
            for obj in objects:
                if obj.type == 'tank':
                    parent.rank += 1
                    parent.tankSpeed += 0.5
                    parent.shootDelay -= 5
                    break

objects = []
bullets = []
colorUp = ['green', 'red']
ui = UI()



Tank('orange', 200, 200, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
Tank('purple', 900, 200, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP0))

for _ in range(200):
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
    Block(x, y, 1)

def up():
    for _ in range(2):
        while True:
            colorInx = randint(0,1)
            x = randint(0, WIDTH//size - 1) * size
            y = randint(1, HEIGHT//size - 1) * size
            rect = pygame.Rect(x, y, size, size)
            fined = False
            for obj in objects:
                if rect.colliderect(obj.rect):
                    fined = True
            if not fined:
                break
        Upgrade(colorUp[colorInx], x, y)
    Timer(30, up).start()

up()

while ON:
    display.fill('black')
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False
            pygame.quit()
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

sys.exit()






















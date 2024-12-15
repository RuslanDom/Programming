import pygame
import sys
import random
from threading import Timer

pygame.init()



WIDTH = 799
HEIGHT = 1000
FPS = 60
SIZE = 64
clock = pygame.time.Clock()
Points = 0
fontUI = pygame.font.Font(None, 30)
fontEnd = pygame.font.Font(None, 50)
play = True
way = 0
fontEnder = fontEnd.render("RESTART MISSION", True, 'white')
fondRect = fontEnder.get_rect(topleft=(250, 900))

imgPlayer = pygame.image.load('image/plane1.png')
imgBG = pygame.image.load('image/background.png')
imgBG_1 = pygame.image.load('image/background_1.png')
imgEnemy = pygame.image.load('image/aircraft.png')
imgBullet = pygame.image.load('image/missileReady.png')
imgFinal = pygame.image.load('image/finally.png')

display = pygame.display.set_mode((WIDTH, HEIGHT))

class Player:
    def __init__(self, px, py, keylist):
        objects.append(self)
        self.type = 'sky'
        self.rect = pygame.rect.Rect(px, py, 69, 107)
        self.moveSpeed = 10
        self.timeSpeed = 0
        self.timeDelay = 30
        self.HP = 5


        self.keyLEFT = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyShoot = keylist[2]

        self.rect = imgPlayer.get_rect(center=(self.rect.centerx, self.rect.centery))


    def update(self):
        if keys[self.keyLEFT] and self.rect.centerx > 42:
            self.rect.x -= self.moveSpeed
        elif keys[self.keyRIGHT] and self.rect.centerx < WIDTH - 42:
            self.rect.x += self.moveSpeed

        if keys[self.keyShoot] and self.timeSpeed == 0:

            Bullet(self, self.rect.centerx, self.rect.centery, 1)
            self.timeSpeed = self.timeDelay
        if self.timeSpeed > 0:
            self.timeSpeed -= 1





    def draw(self):
        # pygame.draw.rect(display, "red", self.rect)
        display.blit(imgPlayer, self.rect)

    def damage_Player(self):
        self.HP -= 1
        if self.HP <= 0:
            objects.remove(self)
class Bullet:
    def __init__(self, parent, px, py, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        # self.dx, self.dy = dx, dy
        self.p2x, self.p2y = self.px, self.py - 60
        self.damage = damage
        self.bulletSpeed = 15

    def update(self):
        self.py -= self.bulletSpeed
        self.p2y -= self.bulletSpeed
        if self.p2y < 0:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.p2y):
                    bullets.remove(self)
                    obj.damage(self.damage)
                    break
    def draw(self):
        # pygame.draw.line(display, 'yellow', (self.px, self.py), (self.p2x, self.p2y), 5)
        display.blit(imgBullet, (self.px - 10, self.p2y))
class Enemy:
    def __init__(self, px, py, SIZE):
        objects.append(self)
        self.type = 'en'
        self.rect = pygame.rect.Rect(px, py, SIZE, SIZE)

        self.HP = 1
        self.rect = imgEnemy.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):
        self.rect.y += 2
        if self.rect.y >= 1000:
            objects.remove(self)


        else:
            for obj in objects:
                if obj != self and self.rect.colliderect(obj.rect):
                    obj.damage_Player()
                    objects.remove(self)
                    ui.hp()


    def draw(self):
        # pygame.draw.rect(display, 'blue', self.rect)
        display.blit(imgEnemy, self.rect)

    def damage(self, value):
        self.HP -= value
        if self.HP <= 0:
            objects.remove(self)
            ui.update()
            print("DESTROY")

class UI:
    def __init__(self, Points, HP):
        self.Points = Points
        self.HP = HP
    def update(self):
        self.Points += 1
    def hp(self):
        self.HP -= 1
    def draw(self):
        display.blit(fontUI.render('POINTS: ' + str(self.Points), True, 'white'), (50, 60))
        display.blit(fontUI.render('HEALTH: ' + str(self.HP), True, 'red'), (50, 40))
        display.blit(fontUI.render('DISTANCE: ' + str(int(way)) + ' KM', True, 'yellow'), (50, 20))



objects = []
bullets = []


PL = Player(WIDTH/2 - 20, HEIGHT - 110, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE))


# -------------------Новый метод!!!!! Получение значения полей в классах  getattr(имя класса, "нужная переменная без self.")---------------------------------
ui = UI(Points, getattr(PL, 'HP'))

def started():
    for _ in range(3):
        while True:
            x = random.randint(0, WIDTH//SIZE - 1) * SIZE
            y = random.randint(0, 100//SIZE - 1) * SIZE
            rect = pygame.rect.Rect(x, y, SIZE, SIZE)
            fined = False
            for obj in objects:
                if rect.colliderect(obj.rect):
                    fined = True
            if not fined:
                break
        Enemy(x, y, SIZE)
    Timer(5, started).start()
bg_y = 0

started()
"""--------------------------------------------Главный цикл--------------------------------------------------"""
ON = True
while ON:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ON = False
            sys.exit()

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    if way < 2000:
        display.fill('black')
        display.blit(imgBG, (0, bg_y))
        display.blit(imgBG_1, (0, bg_y - 1200))
        display.blit(imgBG, (0, bg_y - 2396))
        bg_y += 2
        way += 0.1
        if bg_y >= 2400:
            bg_y = 0

        for bul in bullets:
            bul.update()
        for obj in objects:
            obj.update()

        for bul in bullets:
            bul.draw()
        for obj in objects:
            obj.draw()
            ui.draw()
    else:
        display.blit(imgFinal, (0, 0))
        display.blit(fontEnd.render("CONGRATULATIONS!!!", True, 'white'), (220, 850))
        display.blit(fontEnder, fondRect)
        if fondRect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            way = 0
            Points = 0
            bullets.clear()

            for obj in objects:
                obj.HP = 5

            for i, obj in enumerate(objects):
                if obj.type == 'en':
                    objects.remove(objects[i])
                    objects.pop()





    pygame.display.update()
    clock.tick(FPS)

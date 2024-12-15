import pygame
from random import randint
pygame.init()

width, height = 1200, 800
FPS = 60
Tile = 32

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

fontUI = pygame.font.Font(None, 30)

imgBrick = pygame.image.load('image/block_brick.png')
imgTankList = [
    pygame.image.load('image/tank1.png'),
    pygame.image.load('image/tank2.png'),
    pygame.image.load('image/tank3.png'),
    pygame.image.load('image/tank4.png'),
    pygame.image.load('image/tank5.png'),
    pygame.image.load('image/tank6.png'),
    pygame.image.load('image/tank7.png'),
    pygame.image.load('image/tank8.png')
]
imgBanks = [
    pygame.image.load('image/bang1.png'),
    pygame.image.load('image/bang2.png'),
    pygame.image.load('image/bang3.png')
]
# Направления (стороны) объекта
DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
class UI:
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == "tank":
                pygame.draw.rect(display,obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.hp), True, obj.color)
                rect = text.get_rect(center=(5 + i * 70 + 32, 5 + 11))
                display.blit(text, rect)
                i += 1
class Tank:
    # Этому классу можно внести эти характеристики
    def __init__(self, color, px, py, direct, keylist):
        # Добавит созданный объект в список objects
        objects.append(self)
        # Характеристики
        self.type = 'tank'
        # Цвет
        self.color = color
        # Расположение и размер
        self.rect = pygame.Rect(px, py, Tile, Tile)
        # Изначальное направление объекта
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1
        # Управление объектом
        self.keyLeft = keylist[0]
        self.keyRight = keylist[1]
        self.keyUp = keylist[2]
        self.keyDown = keylist[3]
        self.keyFire = keylist[4]

        self.rank = 0
        self.image = pygame.transform.rotate(imgTankList[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)
    # Функция движения
    def update(self):
        self.image = pygame.transform.rotate(imgTankList[self.rank], -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center=self.rect.center)


        oldX, oldY = self.rect.topleft
        if keys[self.keyLeft]:
            self.rect.x -= self.moveSpeed
            self.direct = 3

        elif keys[self.keyRight]:
            self.rect.x += self.moveSpeed
            self.direct = 1

        elif keys[self.keyUp]:
            self.rect.y -= self.moveSpeed
            self.direct = 0

        elif keys[self.keyDown]:
            self.rect.y += self.moveSpeed
            self.direct = 2


        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keyFire] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1


    # Функция отрисовки на display, цвет и расположение
    def draw(self):
        display.blit(self.image, self.rect)

        # pygame.draw.rect(display, self.color, self.rect)
        # x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        # y = self.rect.centery + DIRECTS[self.direct][1] * 30
        # pygame.draw.line(display,"white", self.rect.center, (x, y), 4)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
            print(self.color, "Dead")
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

        if self.px < 0 or self.px > width or self.py < 0 or self.py > height:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    bullets.remove(self)
                    Bang(self.px, self.py)
                    break

    def draw(self):
        pygame.draw.circle(display,'yellow',(self.px, self.py), 2)

class Bang:
    def __init__(self,px, py):
        objects.append(self)
        self.type = 'bang'
        self.px, self.py = px, py
        self.frame = 0
    def update(self):
        self.frame += 0.2
        if self.frame >= 3:
            objects.remove(self)
    def draw(self):
        image = imgBanks[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        display.blit(image, rect)

class Block:
    def __init__(self,px, py, size):
        objects.append(self)
        self.type = "block"
        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass
    def draw(self):
        display.blit(imgBrick, self.rect)
        # pygame.draw.rect(display,"blue", self.rect)
        # pygame.draw.rect(display, 'grey', self.rect, 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)




bullets = []
objects = []
# Добавили объект, дали ему характеристики, расположение и управление
Tank("green", 100,275, 0, (pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_SPACE))
Tank("red", 650,275, 0, (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_KP0))

# Расстановка блоков
for _ in range(350):
    while True:
        x = randint(0, width // Tile - 1) * Tile
        y = randint(1, height // Tile - 1) * Tile
        rect = pygame.Rect(x, y, Tile, Tile)
        finded = False
        for obj in objects:
            if rect.colliderect(obj.rect):
                finded = True
        if not finded:
            break

    Block(x, y, Tile)

ui = UI()

play = True
while play:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            play = False

    # Переменная отслеживания нажатия на какую либо клавишу
    keys = pygame.key.get_pressed()

    # Перебор списка и его обновдение
    for bullet in bullets:
        bullet.update()
    for obj in objects:
        obj.update()
    ui.update()
    display.fill("black")
    # Перебор списка и отрисовка если появился новый объект
    for bullet in bullets:
        bullet.draw()
    for obj in objects:
        obj.draw()
    ui.draw()
    pygame.display.update()



    clock.tick(FPS)



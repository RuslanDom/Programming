import pygame
import random
pygame.init()
Height = 1000
Width = 799
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Space wars")
BG_color = (0, 0, 0)
BG = pygame.image.load('image/background.png')

play = True
FPS = 60
clock = pygame.time.Clock()
list_y = [20, 120, 220]

class Player:
    def __init__(self, keyList):
        objects.append(self)
        self.type = 'Player'
        self.image = pygame.image.load('image/plane1.png')
        self.rect = self.image.get_rect()
        self.display_rect = display.get_rect()
        self.rect.centerx = self.display_rect.centerx
        self.rect.bottom = self.display_rect.bottom
        self.keyRight = keyList[0]
        self.keyLeft = keyList[1]
        self.keyFire = keyList[2]
        self.timeShot = 60
        self.time_0 = 0

    def update(self):

        if keys[self.keyRight] and self.rect.right < Width:
            self.rect.centerx += 6
        elif keys[self.keyLeft] and self.rect.left > 0:
            self.rect.centerx -= 6


        """ В классе Bullet() передаю параметры координат создания (px, py) ввиде
            полей из класса Player() (self.rect.centerx, self.rect.top)!!!!!!!!!"""


        if keys[self.keyFire] and self.time_0 == 0:

            Bullet(self, self.rect.centerx - 10, self.rect.top - 50, None)
            self.time_0 = self.timeShot
        if self.time_0 > 0:
            self.time_0 -= 2



    def draw(self):
        display.blit(self.image, self.rect)

class Enemy():
    def __init__(self):

        objects.append(self)

        # self.health = health
        # self.damage = damage
        self.image = pygame.image.load('image/aircraft.png')
        self.rect = self.image.get_rect()
        self.bottom = self.rect.bottom

        self.x = random.randint(0, Width - 70)
        self.y = list_y[random.randint(0, 2)]
    def update(self):
        pass
        # self.y += 1
    def draw(self):
        display.blit(self.image, (self.x, self.y))

    
class Bullet():
    def __init__(self, parent, px, py, damage):

        bullet.append(self)
        self.parent = parent
        self.damage = damage
        self.image = pygame.image.load('image/missileReady.png')
        # self.image_1 = pygame.draw.circle(display, "green", (px, py), 5)
        self.rect = self.image.get_rect()
        self.rect_x = px
        self.rect_y = py
        # self.rect_bottom = self.image_rect.bottom


    def update(self):
        self.rect_y -= 10
        if self.rect_y < 0:
            bullet.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.rect_x, self.rect_y):
                    bullet.remove(self)
                    break



    def draw(self):
        display.blit(self.image, (self.rect_x, self.rect_y))






objects = []
bullet = []
Player((pygame.K_RIGHT, pygame.K_LEFT, pygame.K_SPACE))
Enemy()



while play:
    display.fill(BG_color)
    display.blit(BG, (0, 0))

    mouse = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()




    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           play = False
    for obj in objects:
        obj.update()
    for obj in objects:
        obj.draw()
    for bul in bullet:
        bul.update()
    for bul in bullet:
        bul.draw()

    pygame.display.update()
    clock.tick(FPS)

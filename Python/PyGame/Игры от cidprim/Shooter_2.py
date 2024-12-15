import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 800
FPS = 60
clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
play = True
size = 32
class Player:
    def __init__(self, px, py, keylist):
        objects.append(self)
        self.rect = pygame.rect.Rect(px, py, size, size)
        self.keyUP = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyDOWN = keylist[2]
        self.keyLEFT = keylist[3]

        self.speed = 3
        self.timeShoot = 0
        self.delayShoot = 30
    def update(self):
        if keys[self.keyUP] and self.rect.centery > 0:
            self.rect.y -= self.speed
        if keys[self.keyRIGHT] and self.rect.centerx < WIDTH:
            self.rect.x += self.speed
        if keys[self.keyDOWN] and self.rect.centery < HEIGHT:
            self.rect.y += self.speed
        if keys[self.keyLEFT] and self.rect.centerx > 0:
            self.rect.x -= self.speed
        if mouseKey[0]:
            Bullet(self.rect.centerx, self.rect.centery, mousePos)



    def draw(self):
        pygame.draw.rect(surface, "red", self.rect)

class Bullet:
    def __init__(self, px, py, direct):
        bullets.append(self)
        self.px = px
        self.py = py
        self.color = 'black'

        self.speed = 10
        dx, dy = direct[0] - self.px, direct[1] - self.py
        dist = (dx ** 2 + dy ** 2) ** 0.5
        self.sx, self.sy = dx / dist * self.speed, dy / dist * self.speed

    def update(self):
        self.px += self.sx
        self.py += self.sy
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            bullets.remove(self)

    def draw(self):
        pygame.draw.circle(surface, self.color, (self.px, self.py), 2)

objects = []
bullets = []
Player(WIDTH/2, HEIGHT/2, (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a))
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    mouseKey = pygame.mouse.get_pressed()
    surface.fill('white')
    for bul in bullets:
        bul.update()
    for obj in objects:
        obj.update()
    for bul in bullets:
        bul.draw()
    for obj in objects:
        obj.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
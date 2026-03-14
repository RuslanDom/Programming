import pygame as pg
from random import randint



# def src():
pg.init()
HEIGHT = 600
WIDTH = 800
FPS = 90
general = True
clock = pg.time.Clock()
display = pg.display.set_mode((WIDTH, HEIGHT)) 


class PLayer:
    def __init__(self, px, py):
        self.type = 'I'
        _obj.append(self) 
        self.size = 30   
        self.rect = pg.rect.Rect(px, py, self.size, self.size)
        self.shootdelay = 0

    def update(self):
        self.dx, self.dy = pg.mouse.get_pos()
        self.rect.x += (self.dx - self.rect.x) * 0.2

        # Получить нажатие кнопки
        b1, b2, b3 = pg.mouse.get_pressed()
        if b1 and self.shootdelay == 0:
            self.shootdelay = 30 
            Bullet(px=self.rect.x, py=self.rect.y, speed=5)
        if self.shootdelay > 0: self.shootdelay -=1

    def draw(self):
        pg.draw.circle(display, 
                    color='white', 
                    center=(self.rect.x, self.rect.y), 
                    radius=20)
        pg.draw.line(display, 
                    color='red', 
                    start_pos=(self.rect.x, self.rect.y),
                    end_pos=(self.rect.x, self.rect.y - 40), 
                    width=5)


class Bullet:
    def __init__(self, px, py, speed):
        bullets.append(self)
        self.size = 2
        self.rect = pg.rect.Rect(px, py, self.size, self.size)
        self.speed = speed
        
    
    def update(self):
        self.rect.y -= self.speed
        for ob in _obj:
            if ob.type != "I" and self.rect.colliderect(ob.rect):
                bullets.remove(self)
                _obj.remove(ob)

        # Удалили снаряд после выхода за границу
        if self.rect.y < 0: bullets.remove(self)


    def draw(self):
        pg.draw.line(display, 
                       color='red',
                       start_pos=(self.rect.x, self.rect.y),
                       end_pos=(self.rect.x, self.rect.y - 5),
                       width=2)


class Target:
    def __init__(self, px, py, speed):
        self.type = 'rect'
        _obj.append(self)
        self.size = 30
        self.rect = pg.rect.Rect(px, py, self.size, self.size)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT + 10:
            _obj.remove(self)

    def draw(self):
        pg.draw.rect(display, color='blue', rect=self.rect)


playerX, playerY = WIDTH // 2, HEIGHT - 30
_obj = []
bullets = []
my_player = PLayer(px=playerX, py=playerY)
targetDelay = 0

while general:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            general = False

    if targetDelay == 0:
        targetDelay = 60
        Target(px=randint(20, WIDTH - 20), 
               py=-10,
               speed=5)
    if targetDelay > 0: targetDelay -= 1
        

    display.fill('black')
    for bullet in bullets:
        bullet.update()

    for ob in _obj:
        ob.update()

    for bullet in bullets:
        bullet.draw() 

    for ob in _obj:
        ob.draw()


    pg.display.update() 
    clock.tick(FPS)
pg.quit()


# if __name__ == "src":
#     src()
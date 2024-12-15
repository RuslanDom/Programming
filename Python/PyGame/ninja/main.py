import pygame
import json
class Game:
    def __init__(self):
        pygame.init()

        WIDTH = 1200
        HEIGHT = 800
        self.FPS = 60
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play = True

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        ''' .set_colorkey воспринимает указанный цвет как прозрачный'''
        self.img.set_colorkey((0, 0, 0))

        self.img_pos = [200, 400]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)


    def run(self):
        while self.play:
            self.window.fill((14, 219, 248))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if  img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.window, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.window, (0, 50, 255), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 2
            self.window.blit(self.img, self.img_pos)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.play = False
                ''' Отслеживание события
                нажатие клавиши и отпуск клавиши вверх - вниз'''
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_UP:
                        self.movement[0] = True
                    if events.key == pygame.K_DOWN:
                        self.movement[1] = True
                if events.type == pygame.KEYUP:
                    if events.key == pygame.K_UP:
                        self.movement[0] = False
                    if events.key == pygame.K_DOWN:
                        self.movement[1] = False
            pygame.display.update()
            self.clock.tick(self.FPS)

        pygame.quit()

Game().run()
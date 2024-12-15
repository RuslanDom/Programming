import pygame
pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game on VSC')
clock = pygame.time.Clock()
fps = 60
play = True


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
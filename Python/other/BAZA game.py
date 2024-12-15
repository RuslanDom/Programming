import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
play = True

while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            play = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    pygame.display.update()
    clock.tick(FPS)



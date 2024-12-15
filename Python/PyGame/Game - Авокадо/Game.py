
import pygame
import random


# Иницилизируем игру
pygame.init()
# Указываем размеры экрана игры, используем кортеж
screen = pygame.display.set_mode((600, 400)) #flags = pygame.NOFRAME - Убирает рамку окна, пишется внутри скобок через ","

# Создадим название приложения
pygame.display.set_caption("Mr Avocado")

# Ставим иконку для приложения
# icon = pygame.image.load("Python/PyGame/image/ava.png") # Подгрузка изображения
# pygame.display.set_icon(icon)

# Создаём форму объекта
# obj_1 = pygame.Surface((600,50))
# obj_1.fill((33,1,4))

# Пишем текстовые надписи
myFont = pygame.font.Font('Python/PyGame/Font/Agbalumo-Regular.ttf',40)
myFont2 = pygame.font.Font('Python/PyGame/Font/Agbalumo-Regular.ttf',20)
myFont3 = pygame.font.Font('Python/PyGame/Font/Agbalumo-Regular.ttf',10)
text = myFont.render('GAME OVER', False, "white") # Второй параметр сглаживание - False
returnText = myFont2.render("<<<RESTART>>>", False, "white")
returnText_rect = returnText.get_rect(topleft=(230,240))

# Создание врага
zombe = [
    pygame.image.load("Python/PyGame/image/Zombe1.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/Zombe2.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/Zombe3.png").convert_alpha()
]
ghost = [
    pygame.image.load("Python/PyGame/image/ghost1.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/ghost2.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/ghost3.png").convert_alpha()
]
# Подгружаем изображение

vegetables = [
    pygame.image.load("Python/PyGame/image/vegetables1.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/vegetables2.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/vegetables3.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/vegetables4.png").convert_alpha()
]

# Настраиваем FPS
clock = pygame.time.Clock()

# Добавляем звуки
pygame.mixer.init()
bgSound = pygame.mixer.Sound("Python/PyGame/saunds/saundtrek.wav")
gameOverSound = pygame.mixer.Sound("Python/PyGame/saunds/super-mario-game-over.wav")

# Подкачка файла для background
backGr = pygame.image.load("Python/PyGame/image/BG_forest.jpg").convert()
bg_x = 0
# Загружаем файлы для анимации ходьбы и прыжка
walk = [
    pygame.image.load("Python/PyGame/image/play.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/play1.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/play2.png").convert_alpha()
    ]
jump = [
    pygame.image.load("Python/PyGame/image/play4.png").convert_alpha(),
    pygame.image.load("Python/PyGame/image/play3.png").convert_alpha()
]
# Подключаем снаряды
bullet = pygame.image.load("Python/PyGame/image/laser1.png").convert_alpha()
bullets = []
bulletCount = 2

# Координата появления врага
# zombe_x = 550 Не нужна!!!
# Переменная индекса анимации игрока и врага
playerAniCount = 0
playerJumpCount = 0
zombeAniCount = 0
ghostAniCount = 0
vegNum = 0
# Переменные для передвижения игрока и прыжка
playerSpeed = 15
player_x = 100
player_y = 285
isJump = False
jumpCount = 9
ghost_x = 650
ghost_y = 280
veg_y = 280
# Создаем бесконечный цикл с постоянным обновлением экрана
running = True
# Таймер для появления врага
zombeTime = pygame.USEREVENT + 1
ghostTime = pygame.USEREVENT + 2
vegaTime = pygame.USEREVENT + 3
pygame.time.set_timer(zombeTime,5000)
pygame.time.set_timer(ghostTime,8000)
pygame.time.set_timer(vegaTime, 10000)
monstrList = []
monstrList2 = []
vegaList = []
point = 0

# Реализация проигрыша
gamePlay = True

if gamePlay:
    # Включаем музыку
    bgSound.play(-1)


# -------------------------------------------------------------ИГРОВОЙ ГЛАВНЫЙ ЦИКЛ------------------------------------------------------------------------------------------


while running:
    # Цвет заднего фона, в виде кортежа
    # screen.fill((255,255,255))


    # Создаём BG и делаем ему возможность движения с движением игрока
    screen.blit(backGr, (bg_x,0))
    screen.blit(backGr, (bg_x + 600, 0))



    if gamePlay:
        bulletsText = myFont2.render('Shells: ' + str(bulletCount), False, "white")
        screen.blit(bulletsText,(30,30))
        pointText = myFont2.render('Points: ' + str(point), False,"red")
        screen.blit(pointText,(480,30))
        # BackGround движение
        bg_x -= 5
        if bg_x <= -600:
            bg_x = 0

        # Добавляем объкты (труба)
        # screen.blit(truba, (100, 233))

        # Создали квадраты физическая модель игрока
        playerFM = walk[0].get_rect(topleft=(player_x, player_y))


        # Перебор списка по индексу и значениям i - индексы el - элемент списка
        if monstrList:
            for (inx,el) in enumerate(monstrList):
                screen.blit(zombe[zombeAniCount], el)
                # Направление и движение врага по оси x
                el.x -= 10
                # При выходе врага за координату x = -10 идёт удаление врага по его индексу
                if el.x < -10:
                    monstrList.pop(inx)
                    bulletCount += 1
                # Условия соприкосновения
                if playerFM.colliderect(el):
                    gamePlay = False

        if monstrList2:
            for (i,el) in enumerate(monstrList2):
                screen.blit(ghost[ghostAniCount], el)
                el.x -= 25
                if el.x < -10:
                    monstrList2.pop(i)
                    bulletCount += 1
                    ghost_y = random.randrange(180, 290, 50)
                if playerFM.colliderect(el):
                    gamePlay = False
                    ghost_y = random.randrange(180, 290, 50)

        if vegaList:
            for (i,el) in enumerate(vegaList):

                screen.blit(vegetables[vegNum], el)
                el.x -= 25
                if el.x < -10:
                    vegaList.pop(i)
                    vegNum = random.randint(0,3)
                    veg_y = random.randrange(180,290,100)
                    point -= 100

                if playerFM.colliderect(el):
                    vegNum = random.randint(0,3)
                    bulletCount += 1
                    point += 100
                    vegaList.pop(i)
                    veg_y = random.randrange(180, 290, 100)


        # zombeFM = zombe[0].get_rect(topleft=(zombe_x, 280)) Не нужна!!!

        # Добавляем созданный объект
        # screen.blit(obj_1,(0,350))

        # Добавляет отслеживание нажатия на клавиши - key.get_pressed()
        keys = pygame.key.get_pressed()

        # Если нажимаем на прыжок играет jump анимация если стрелочки то walk
        if keys[pygame.K_UP]:
            screen.blit(jump[playerJumpCount], (player_x, player_y))
        elif keys[pygame.K_DOWN]:
            screen.blit(jump[1], (player_x, player_y))
        else:
            screen.blit(walk[playerAniCount], (player_x, player_y))

        # Добавляем врага
        # screen.blit(zombe[zombeAniCount], (zombe_x, 280)) Теперь не нужна эта строчка кода
        if zombeAniCount == 2:
            zombeAniCount = 0
        else:
            zombeAniCount += 1

        if ghostAniCount == 2:
            ghostAniCount = 0
        else:
            ghostAniCount += 1



        # Передвижение игрока

        if  keys[pygame.K_LEFT] and player_x > 10:
            player_x -= playerSpeed

            # Меняем индекс для списка чтобы работала анимация
            if playerAniCount == 2:
                playerAniCount = 0
            else:
                playerAniCount += 1
        elif keys[pygame.K_RIGHT] and player_x < 530:
            player_x += playerSpeed

            if playerAniCount == 2:
                playerAniCount = 0
            else:
                playerAniCount += 1
        elif keys[pygame.K_UP]:
            if playerJumpCount == 1:
                playerJumpCount = 0
            else:
                playerJumpCount += 1


        # Реализация прыжка
        if not isJump:
            # Отслеживание нажатия клавиши вверх
            if keys[pygame.K_UP]:
                isJump = True
        else:
            if jumpCount >= -9:
                if jumpCount > 0:
                    # Движение вверх и скорость движения
                    player_y -= (jumpCount**2)/2
                else:
                    # Движение вниз и скорость движения
                    player_y += (jumpCount**2)/2
                jumpCount -= 1.5
            else:
                # Остановка прыжка
                isJump = False
                jumpCount = 9


        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                # Скорость движения снаряда
                el.x += 10
                # Удаление снарядов
                if el.x > 550:
                    bullets.pop(i)
                # Уничтожение снаряда и врага и соприкосновении
                if monstrList:
                    for(index, monstr) in enumerate(monstrList):
                        # Взаимодействие снаряда(el) с врагом(monstr) через .colliderect()
                        if el.colliderect(monstr):
                            # Удаляем монстра и снаряд по их индексу в переборе данныч списков
                            monstrList.pop(index)
                            bullets.pop(i)
                            bulletCount += 1
        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 10
                if el.x > 550:
                    bullets.pop(i)

                if monstrList2:
                    for(ind, monstr) in enumerate(monstrList2):
                        if el.colliderect(monstr):
                            monstrList2.pop(ind)
                            ghost_y = random.randrange(180,290,50)
                            bullets.pop(i)
                            bulletCount += 1

        # Рисуем объект круг через draw внутри другого объекта( координаты указываем относительно родительского объекта)
        # pygame.draw.circle(screen,'yellow',(50,50), 25)



    #---------------------------------- Условие которое срабатывает при проигрыше---------------------------------------------
    else:
        screen.fill((17, 21, 242))
        # Выводим созданный текст проигрыша
        screen.blit(text, (190, 150))
        screen.blit(returnText, returnText_rect)
        # В переменную помещается позиция мыши
        mouse = pygame.mouse.get_pos()
        # Если позиция мыши на returnText_rect и нажать на клавишу мыши то произойдёт перезапуск игры
        if returnText_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:

            gamePlay = True
            # Обновляется позиция игрока и удалются все созданные ранее враги
            player_x = 100
            monstrList.clear()
            monstrList2.clear()
            bullets.clear()
            vegaList.clear()
            bulletCount = 2

    # Команда которая обновляет экран и переворачивает изображение с невидимой стороны на видимую
    pygame.display.update()


    # ---------------------------------Создаем цикл перебора отслеживания события нажатия на кнопку закрыть-----------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Таймер создания врага вместе с физической моделью и координатами .get_rect(topleft=(620,280))


        if event.type == zombeTime:
            monstrList.append(zombe[zombeAniCount].get_rect(topleft=(620, 280)))

        if event.type == ghostTime:
            monstrList2.append(ghost[ghostAniCount].get_rect(topleft=(720, ghost_y)))

        if event.type == vegaTime:
            vegaList.append(vegetables[3].get_rect(topleft=(800, veg_y)))

        # Создание снарядов. При нажатии на пробел добавляет в список bullets новый элемент
        if gamePlay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bulletCount > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 20, player_y + 10)))
            bulletCount -= 1


    # FPS
    clock.tick(60)
else:
    # Запуск музыки проигрыша
    gameOverSound.play()

        # Добавляем изменение заднего фона при нажатии на клавишу (фон не изменится, потому что в цикле выше опять перекрасится)
        # elif ev.type == pygame.KEYDOWN:
        #     if ev.key == pygame.K_j:
        #         screen.fill((127, 96, 145))







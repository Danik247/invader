import random
import pygame
import time

# Настройки окна
WIDTH = 500
HEIGHT = 500
FPS = 60

# Настройка цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Инициализация
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
# pygame.mixer.music.load('nian.mp3')

# Время
lastTime = 0
currentTime = 0
lastTime1 = 0
currentTime1 = 0
lastTime2 = 0
currentTime2 = 0
lastTime3 = 0
currentTime3 = 0
lastTime4 = 0
currentTime4 = 0
# Персонаж
x = WIDTH // 2
y = HEIGHT // 2
last_x = x
hero = pygame.Rect(x, y, 60, 50)
heroImg = pygame.image.load('razorinv.png')
heroImg_front = pygame.image.load('razorinv.png')
heroImg_left = pygame.image.load('razorinv_left.png')
heroImg_right = pygame.image.load('razorinv_right.png')
LEFT = False
RIGHT = False
UP = False
DOWN = False
sp_left = 0
sp_up = 0
life = 3
ammo = 3

# меню
butonimg = pygame.image.load('buton.png')
hardmode = 2
hardtxt = "norm"
butstxt1 = "wasd:move/space:fire/tab:pause"
butstxt2 = "LMB:less/PMB:more"

# бустеры
duble_ammo_time = 0
triple_ammo_time = 0
laser_ammo_time = 0
boosters = []
boostcd = 5
boostImage1 = pygame.image.load('BULbooster.png')
boostImage2 = pygame.image.load('HPboost.png')
boostImage3 = pygame.image.load('ATC1booster.png')
boostImage4 = pygame.image.load('ATC2booster.png')
boostImage5 = pygame.image.load('ATC3booster.png')
boostImg = [boostImage1, boostImage2, boostImage3, boostImage4, boostImage5]
boostRect = boostImage1.get_rect()
wbost = boostRect.width
hbost = boostRect.height
b_img_index = 0

# Противники
points = +0

enemies = []
enemycd = 5
enemyImage = pygame.image.load('invader1.png')  # .convert()
enemyRect = enemyImage.get_rect()
we = enemyRect.width
he = enemyRect.height
enlife = 2
elife = 2
enlifes = []

# Противники1
enemies1 = []
enemycd1 = 5
enemyImage1 = pygame.image.load('invader2.png')  # .convert()
enemyRect1 = enemyImage1.get_rect()
we1 = enemyRect1.width
he1 = enemyRect1.height
enlife1 = 2
elife1 = 2
enlifes1 = []

# Противники2
enemies2 = []
enemycd2 = 5
enemyImage2 = pygame.image.load('invader3.png')  # .convert()
enemyRect2 = enemyImage2.get_rect()
we2 = enemyRect2.width
he2 = enemyRect2.height
enlife2 = 4
elife2 = 4
enlifes2 = []
firecd = 10
firecd_list = []

# Противники3
enemies3 = []
enemycd3 = 5
enemyImage3 = pygame.image.load('invader4.png')  # .convert()
enemyRect3 = enemyImage3.get_rect()
we3 = enemyRect3.width
he3 = enemyRect3.height
enlife3 = 3
elife3 = 3
enlifes3 = []
firecd3 = 10
firecd_list3 = []

# Противники4
enemies4 = []
enemycd4 = 5
enemyImage4 = pygame.image.load('invader5.png')  # .convert()
enemyRect4 = enemyImage4.get_rect()
we4 = enemyRect4.width
he4 = enemyRect4.height
enlife4 = 7
elife4 = 7
enlifes4 = []

# Звезды
stars = []
starcd = 10
stars1 = []
star1cd = 10
starImg1 = pygame.image.load('SVESDA1.png')
starImg2 = pygame.image.load('SVESDA2.png')
starImg3 = pygame.image.load('SVESDA3.png')
starImg4 = pygame.image.load('SVESDA4.png')
starImg5 = pygame.image.load('SVESDA5.png')
index_bul_img_list = []
starpng = [starImg1, starImg2, starImg3, starImg5, starImg4]
starRect = starImg1.get_rect()
star1Rect = starImg1.get_rect()
ws = starRect.width
hs = starRect.height
img_index = 0

# Пули
wb = 2
hb = 5
wl = 7
hl = 20
herobulimg = pygame.image.load("bullet1.png")
bulletImg = pygame.image.load("bullet.png")
laserImg = pygame.image.load("laser.png")
enbullets = []
enbullets1 = []
enbullets2 = []
bullets = []
bullets1 = []
bullets2 = []
bullets3 = []
laser_list = []
laser_cd = 5
isShot = False
boomimg = pygame.image.load("boom.png")

# Шрифты
pointsT = pygame.font.Font('visitor1.ttf', 20)
lifeT = pygame.font.Font('visitor1.ttf', 20)
bulletT = pygame.font.Font('visitor1.ttf', 20)
gameover = pygame.font.Font('visitor1.ttf', 68)
buttons = pygame.font.Font('visitor1.ttf', 20)
Bboost_time1 = pygame.font.Font('visitor1.ttf', 20)
Bboost_time2 = pygame.font.Font('visitor1.ttf', 20)
Bboost_time3 = pygame.font.Font('visitor1.ttf', 20)
font = pygame.font.Font('visitor1.ttf', 20)
danik = pygame.font.Font('visitor1.ttf', 20)
# Текст
gameover_text = gameover.render('GAME OVER', True, RED)
gamemode = 0

# Музыка
# pygame.mixer.music.play(1)

GO = False
running = True
while running:
    pygame.mixer.music.queue('nian1.mp3')
    pygame.mixer.music.set_volume(0.1)

    if gamemode == 0:
        screen = pygame.display.set_mode((500, 500))
        screen.fill(BLACK)
        screen.blit(butonimg, (170, 100))
        screen.blit(butonimg, (170, 200))
        screen.blit(butonimg, (170, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 100) and (event.pos[1] < 100 + 50):
                    # обработка нажатия на 1 кнопку
                    gamemode = 1

                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 200) and (event.pos[1] < 200 + 50):
                    # обработка нажатия на 2 кнопку
                    gamemode = 0.5

                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 300) and (event.pos[1] < 300 + 50):
                    # обработка нажатия на 3 кнопку
                    running = False

        text = font.render("settings", True, BLACK)
        start = font.render("play", True, BLACK)
        stop = font.render("exit", True, BLACK)
        buters = font.render(butstxt1, True, WHITE)
        diss = font.render("Danik#4309", True, (100, 100, 100))

        screen.blit(start, (230, 115))
        screen.blit(text, (208, 215))
        screen.blit(stop, (232, 315))
        screen.blit(buters, (80, 5))
        screen.blit(diss, (10, 475))

    if gamemode == 0.5:
        screen.fill(BLACK)
        screen = pygame.display.set_mode((500, 500))
        screen.blit(butonimg, (170, 100))
        screen.blit(butonimg, (170, 200))
        screen.blit(butonimg, (170, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 100) and (event.pos[1] < 100 + 50):
                    gamemode = 0
                if ((event.pos[0] > 170) and (event.pos[0] < 170 + 160)) \
                        and ((event.pos[1]) > (200 and event.pos[1] < 200 + 50)):
                    # обработка нажатия на 2 кнопку
                    if event.button == 1:
                        if hardmode >= 0:
                            hardmode -= 1
                    if event.button == 3:
                        if hardmode <= 3:
                            hardmode += 1
                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 300) and (event.pos[1] < 300 + 50):
                    # обработка нажатия на 3 кнопку
                    if event.button == 1:
                        if WIDTH >= 400:
                            WIDTH -= 100
                            HEIGHT -= 100
                    if event.button == 3:
                        if WIDTH < 1000:
                            WIDTH += 100
                            HEIGHT += 100
        if hardmode == 1:
            hardtxt = "easy"
            ammo = 10
            lifed = 10
            elife = 1
            elife1 = 1
            elife2 = 2
            elife3 = 2
            elife4 = 4
        if hardmode == 2:
            hardtxt = "norm"
            ammo = 3
            life = 3
            elife = 2
            elife1 = 2
            elife2 = 3
            elife3 = 3
            elife4 = 6
        if hardmode == 3:
            hardtxt = "hard"
            life = 1
            ammo = 1
            elife = 3
            elife1 = 3
            elife2 = 4
            elife3 = 4
            elife4 = 9

        text = font.render(hardtxt, True, BLACK)
        start = font.render("return", True, BLACK)
        stop = font.render(str(WIDTH) + str(HEIGHT), True, BLACK)
        buters = font.render(butstxt2, True, WHITE)

        screen.blit(text, (225, 215))
        screen.blit(start, (220, 115))
        screen.blit(stop, (215, 315))
        screen.blit(buters, (150, 5))

    if gamemode == 2:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.blit(butonimg, (170, 100))
        screen.blit(butonimg, (170, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 100) and (event.pos[1] < 100 + 50):
                    gamemode = 1

                if (event.pos[0] > 170) and (event.pos[0] < 170 + 160) \
                        and (event.pos[1] > 200) and (event.pos[1] < 200 + 50):
                    running = False

        stop = font.render("return", True, BLACK)
        text = font.render("exit", True, BLACK)

        screen.blit(stop, (217, 115))
        screen.blit(text, (234, 215))
    if gamemode == 1:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BLACK)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_TAB:
                    gamemode = 2
                if i.key == pygame.K_a:
                    LEFT = True
                if i.key == pygame.K_d:
                    RIGHT = True
                if i.key == pygame.K_w:
                    UP = True
                if i.key == pygame.K_s:
                    DOWN = True
                if i.key == pygame.K_SPACE:
                    isShot = True
                if i.key == pygame.K_ESCAPE:
                    running = False
            if i.type == pygame.KEYUP:
                if i.key == pygame.K_a:
                    LEFT = False
                if i.key == pygame.K_d:
                    RIGHT = False
                if i.key == pygame.K_w:
                    UP = False
                if i.key == pygame.K_s:
                    DOWN = False

        # Передвижение персонажа
        if LEFT and sp_left > -5:
            sp_left -= 0.5
        if RIGHT and sp_left < 5:
            sp_left += 0.5
        if UP and sp_up > -5:
            sp_up -= 0.5
        if DOWN and sp_up < 5:
            sp_up += 0.5

        if hero.bottom > HEIGHT:
            sp_up = 0
            hero.top -= 0.1
        if hero.right > WIDTH:
            sp_left = 0
            hero.left -= 0.1
        if hero.top < 0:
            sp_up = 0
            hero.top += 0.1
        if hero.left < 0:
            sp_left = 0
            hero.left += 0.1

        # инерция
        if sp_left > 0:
            sp_left -= 0.1
        if sp_left < 0:
            sp_left += 0.1
        if sp_up < 0:
            sp_up += 0.1
        if sp_up >= 0.1:
            sp_up -= 0.1

        # наклон
        if last_x < hero.x:
            heroImg = heroImg_right
        if last_x > hero.x:
            heroImg = heroImg_left
        if last_x == hero.x:
            heroImg = heroImg_front
        last_x = hero.x

        # движ
        hero.left += sp_left
        hero.top += sp_up
        # СТОЛКНОВЕНИЕ
        # Противник с героем
        index_enemy = 0
        for enemy in enemies:
            if hero.colliderect(enemy):
                life -= 1
                del enemies[index_enemy]
                del enlifes[index_enemy]
            index_enemy += 1
        index_enemy = 0
        for enemy1 in enemies1:
            if hero.colliderect(enemy1):
                life -= 1
                del enemies1[index_enemy]
                del enlifes1[index_enemy]
            index_enemy += 1
        index_enemy = 0
        for enemy2 in enemies2:
            if hero.colliderect(enemy2):
                life -= 1
                del enemies2[index_enemy]
                del enlifes2[index_enemy]
                del firecd_list[index_enemy]
            index_enemy += 1
        index_enemy = 0
        for enemy3 in enemies3:
            if hero.colliderect(enemy3):
                life -= 1
                del enemies3[index_enemy]
                del enlifes3[index_enemy]
                del firecd_list3[index_enemy]
            index_enemy += 1
        index_enemy = 0
        for enemy4 in enemies4:
            if hero.colliderect(enemy4):
                life -= 1
                del enemies4[index_enemy]
                del enlifes4[index_enemy]
            index_enemy += 1

        if life < 1:
            GO = True
        # Противник с пулей
        index_enemy = 0
        for enemy in enemies:
            for bullet in bullets:
                if bullet.colliderect(enemy):
                    enlifes[index_enemy] -= 1
                    bullets.remove(bullet)
                    ammo += 1
                    screen.blit(boomimg, (bullet.left - 25, bullet.top - 25))
            index_enemy += 1
        index_enemy = 0
        for enemy1 in enemies1:
            for bullet in bullets:
                if bullet.colliderect(enemy1):
                    enlifes1[index_enemy] -= 1
                    bullets.remove(bullet)
                    ammo += 1
                    screen.blit(boomimg, (bullet.left - 25, bullet.top - 25))
            index_enemy += 1
        index_enemy = 0
        for enemy2 in enemies2:
            for bullet in bullets:
                if bullet.colliderect(enemy2):
                    enlifes2[index_enemy] -= 1
                    bullets.remove(bullet)
                    ammo += 1
                    screen.blit(boomimg, (bullet.left - 25, bullet.top - 25))
            index_enemy += 1
        index_enemy = 0
        for enemy3 in enemies3:
            for bullet in bullets:
                if bullet.colliderect(enemy3):
                    enlifes3[index_enemy] -= 1
                    bullets.remove(bullet)
                    ammo += 1
                    screen.blit(boomimg, (bullet.left - 25, bullet.top - 25))
            index_enemy += 1
        index_enemy = 0
        for enemy4 in enemies4:
            for bullet in bullets:
                if bullet.colliderect(enemy4):
                    enlifes4[index_enemy] -= 1
                    bullets.remove(bullet)
                    ammo += 1
                    screen.blit(boomimg, (bullet.left - 25, bullet.top - 25))
            index_enemy += 1
        index_enemy = 0
        for enlife in enlifes:
            if enlife <= 0:
                del enemies[index_enemy]
                points += 1
                del enlifes[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enlife1 in enlifes1:
            if enlife1 <= 0:
                del enemies1[index_enemy]
                points += 1
                del enlifes1[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enlife2 in enlifes2:
            if enlife2 <= 0:
                del enemies2[index_enemy]
                points += 1
                del enlifes2[index_enemy]
                del firecd_list[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enlife3 in enlifes3:
            if enlife3 <= 0:
                del enemies3[index_enemy]
                points += 1
                del enlifes3[index_enemy]
                del firecd_list3[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enlife4 in enlifes4:
            if enlife4 <= 0:
                del enemies4[index_enemy]
                points += 1
                del enlifes4[index_enemy]
            index_enemy += 1
        # СЧЕТ
        points_text = pointsT.render('points : ' + str(points), True, WHITE)
        life_text = lifeT.render('lifes  : ' + str(life), True, RED)
        bullet_text = bulletT.render('ammo.  : ' + str(ammo), True, YELLOW)
        Bboost_time1 = pointsT.render('2x :  ' + str(duble_ammo_time), True, WHITE)
        Bboost_time2 = pointsT.render('3x :  ' + str(triple_ammo_time), True, WHITE)
        Bboost_time3 = pointsT.render('10x:  ' + str(laser_ammo_time), True, WHITE)
        screen.blit(points_text, (10, 10))
        screen.blit(life_text, (10, 30))
        screen.blit(bullet_text, (10, 50))

        # БУСТЕРЫ
        # Создание бустеров
        if boostcd < 1:
            b_img_index = random.randint(0, 4)
            x_boost = random.randint(10, WIDTH - wb)
            boosters.append(pygame.Rect(x_boost, -hbost, wbost, hbost))
            boostcd = random.randint(100, 400)
            index_bul_img_list.append(b_img_index)
        boost_index = 0
        boostcd -= 1
        # отрисовка бустеров
        for boost in boosters:
            boost.top += 1.5
            screen.blit(boostImg[index_bul_img_list[boost_index]], (boost.left, boost.top))
            boost_index += 1
        # Удаление бустеров
        boost_index = 0
        for boost in boosters:
            if boost.top > HEIGHT:
                boosters.pop(boost_index)
                index_bul_img_list.pop(boost_index)
            if boost.right > WIDTH:
                boost.left = 5
            boost_index += 1
        # касание бустеров
        boost_index = 0
        for boost in boosters:
            if hero.colliderect(boost):
                if index_bul_img_list[boost_index] == 1:
                    life += 1
                if index_bul_img_list[boost_index] == 0:
                    ammo += 1
                if index_bul_img_list[boost_index] == 2:
                    duble_ammo_time += 1000
                if index_bul_img_list[boost_index] == 3:
                    triple_ammo_time += 1000
                if index_bul_img_list[boost_index] == 4:
                    laser_ammo_time += 500

                boosters.pop(boost_index)
                index_bul_img_list.pop(boost_index)
            index_bul = 0
            for bullet in bullets:
                if boost.colliderect(bullet):
                    bullets.pop(index_bul)
                    boost.top -= 10
                    ammo += 1
                    screen.blit(boomimg, (bullet.left - 25, bullet.top - 25))
                index_bul += 1
            boost_index += 1
        # обработка ефектов
        if duble_ammo_time > 0:
            screen.blit(Bboost_time1, (WIDTH - 120, 10))
            duble_ammo_time -= 1
            if isShot and ammo > 0 and laser_ammo_time < 1:
                bulRect1 = pygame.Rect(hero.left + 22, hero.top - 5, wb, hb)
                bullets1.append(bulRect1)
        if triple_ammo_time > 0:
            screen.blit(Bboost_time2, (WIDTH - 120, 25))
            triple_ammo_time -= 1
            if isShot and ammo > 0 and laser_ammo_time < 1:
                bulRect2 = pygame.Rect(hero.left + 22, hero.top - 5, wb, hb)
                bulRect3 = pygame.Rect(hero.left + 22, hero.top - 5, wb, hb)
                bullets2.append(bulRect2)
                bullets3.append(bulRect3)
        if laser_ammo_time > 0:
            screen.blit(Bboost_time3, (WIDTH - 120, 40))
            laser_ammo_time -= 1
            if laser_cd < 1:
                lasRect = pygame.Rect(hero.left + 21, hero.top + 7, wb, hb)
                laser_list.append(lasRect)
                laser_cd = 2
            laser_cd -= 1
        # ПУЛИ
        # Создание пуль
        if isShot and ammo > 0 and laser_ammo_time < 1:
            bulRect = pygame.Rect(hero.left + 22, hero.top + 5, wb, hb)
            bullets.append(bulRect)
            isShot = False
            ammo -= 1

        # Отрисовка пуль врагов
        for enbullet in enbullets:
            enbullet.top += 4
            screen.blit(bulletImg, (enbullet.left, enbullet.top))
            if enbullet.top > HEIGHT:
                enbullets.remove(enbullet)
        for enbullet in enbullets:
            if enbullet.colliderect(hero):
                enbullets.remove(enbullet)
                life -= 1

        for enbullet1 in enbullets1:
            enbullet1.top += 4
            enbullet1.left += 2
            screen.blit(bulletImg, (enbullet1.left, enbullet1.top))
            if enbullet1.top > HEIGHT:
                enbullets1.remove(enbullet1)
        for enbullet1 in enbullets1:
            if enbullet1.colliderect(hero):
                enbullets1.remove(enbullet1)
                life -= 1

        for enbullet2 in enbullets2:
            enbullet2.top += 4
            enbullet2.left -= 2
            screen.blit(bulletImg, (enbullet2.left, enbullet2.top))
            if enbullet2.top > HEIGHT:
                enbullets2.remove(enbullet2)
        for enbullet2 in enbullets2:
            if enbullet2.colliderect(hero):
                enbullets2.remove(enbullet2)
                life -= 1
        # Отрисовка пуль
        for bullet in bullets:
            screen.blit(herobulimg, (bullet.left, bullet.top))
            bullet.top -= 7

        # Отрисовка пуль при буст1
        for bullet1 in bullets1:
            screen.blit(herobulimg, (bullet1.left, bullet1.top))
            bullet1.top -= 7
            index_enemy = 0
            for enemy in enemies:
                if enemy.colliderect(bullet1):
                    enlifes[index_enemy] -= 1
                    bullets1.remove(bullet1)
                index_enemy += 1
        for bullet1 in bullets1:
            index_enemy = 0
            for enemy1 in enemies1:
                if enemy1.colliderect(bullet1):
                    enlifes1[index_enemy] -= 1
                    bullets1.remove(bullet1)
                index_enemy += 1
            if bullet1.top > HEIGHT:
                bullets1.remove(bullet1)
        for bullet1 in bullets1:
            for boost in boosters:
                if boost.colliderect(bullet1):
                    boost.top -= 10
                    bullets1.remove(bullet1)
        for bullet1 in bullets1:
            index_enemy = 0
            for enemy2 in enemies2:
                if enemy2.colliderect(bullet1):
                    enlifes2[index_enemy] -= 1
                    bullets1.remove(bullet1)
            index_enemy += 1
        for bullet1 in bullets1:
            index_enemy = 0
            for enemy3 in enemies3:
                if enemy3.colliderect(bullet1):
                    enlifes3[index_enemy] -= 1
                    bullets1.remove(bullet1)
                index_enemy += 1
        for bullet1 in bullets1:
            index_enemy = 0
            for enemy4 in enemies4:
                if enemy4.colliderect(bullet1):
                    enlifes4[index_enemy] -= 1
                    bullets1.remove(bullet1)
                index_enemy += 1
        # Отрисовка пуль при буст2 часть1
        for bullet2 in bullets2:
            screen.blit(herobulimg, (bullet2.left, bullet2.top))
            bullet2.right -= 2
            bullet2.top -= 6
            index_enemy = 0
            for enemy in enemies:
                if enemy.colliderect(bullet2):
                    enlifes[index_enemy] -= 1
                    bullets2.remove(bullet2)
                index_enemy += 1
        for bullet2 in bullets2:
            index_enemy = 0
            for enemy1 in enemies1:
                if enemy1.colliderect(bullet2):
                    enlifes1[index_enemy] -= 1
                    bullets2.remove(bullet2)
                index_enemy += 1
            if bullet2.top > HEIGHT:
                bullets2.remove(bullet2)
        for bullet2 in bullets2:
            for boost in boosters:
                if boost.colliderect(bullet2):
                    boost.top -= 10
                    bullets2.remove(bullet2)
            index_enemy = 0
        for bullet2 in bullets2:
            index_enemy = 0
            for enemy2 in enemies2:
                if enemy2.colliderect(bullet2):
                    enlifes2[index_enemy] -= 1
                    bullets2.remove(bullet2)
                index_enemy += 1
        for bullet2 in bullets2:
            index_enemy = 0
            for enemy3 in enemies3:
                if enemy3.colliderect(bullet2):
                    enlifes3[index_enemy] -= 1
                    bullets2.remove(bullet2)
                index_enemy += 1
        for bullet2 in bullets2:
            index_enemy = 0
            for enemy4 in enemies4:
                if enemy4.colliderect(bullet2):
                    enlifes4[index_enemy] -= 1
                    bullets2.remove(bullet2)
                index_enemy += 1
        # Отрисовка пуль при буст2 часть2
        for bullet3 in bullets3:
            screen.blit(herobulimg, (bullet3.left, bullet3.top))
            bullet3.right += 2
            bullet3.top -= 6
            index_enemy = 0
            for enemy in enemies:
                if enemy.colliderect(bullet3):
                    enlifes[index_enemy] -= 1
                    bullets3.remove(bullet3)
                index_enemy += 1
        for bullet3 in bullets3:
            index_enemy = 0
            for enemy1 in enemies1:
                if enemy1.colliderect(bullet3):
                    enlifes1[index_enemy] -= 1
                    bullets3.remove(bullet3)
                index_enemy += 1
            if bullet3.top > HEIGHT:
                bullets1.remove(bullet3)
        for boost in boosters:
            for bullet3 in bullets3:
                if boost.colliderect(bullet3):
                    boost.top -= 10
                    bullets3.remove(bullet3)
        for bullet3 in bullets3:
            index_enemy = 0
            for enemy2 in enemies2:
                if enemy2.colliderect(bullet3):
                    enlifes2[index_enemy] -= 1
                    bullets3.remove(bullet3)
                index_enemy += 1
        for bullet3 in bullets3:
            index_enemy = 0
            for enemy3 in enemies3:
                if enemy3.colliderect(bullet3):
                    enlifes3[index_enemy] -= 1
                    bullets3.remove(bullet3)
                index_enemy += 1
        for bullet3 in bullets3:
            index_enemy = 0
            for enemy4 in enemies4:
                if enemy4.colliderect(bullet3):
                    enlifes4[index_enemy] -= 1
                    bullets3.remove(bullet3)
                index_enemy += 1
        # Отрисовка пуль при буст3
        for laser in laser_list:
            screen.blit(laserImg, (laser.left, laser.top))
            laser.top -= 6
            index_enemy = 0
            for enemy in enemies:
                if enemy.colliderect(laser):
                    enlifes[index_enemy] -= 1
                    laser_list.remove(laser)
                index_enemy += 1
        for laser in laser_list:
            index_enemy = 0
            for enemy1 in enemies1:
                if enemy1.colliderect(laser):
                    enlifes1[index_enemy] -= 1
                    laser_list.remove(laser)
                index_enemy += 1
        for laser in laser_list:
            if laser.top < (hero.top - 200):
                laser_list.remove(laser)
        for laser in laser_list:
            index_enemy = 0
            for enemy2 in enemies2:
                if enemy2.colliderect(laser):
                    enlifes2[index_enemy] -= 1
                    laser_list.remove(laser)
                index_enemy += 1
        for laser in laser_list:
            index_enemy = 0
            for enemy3 in enemies3:
                if enemy3.colliderect(laser):
                    enlifes3[index_enemy] -= 1
                    laser_list.remove(laser)
                index_enemy += 1
        for laser in laser_list:
            index_enemy = 0
            for enemy4 in enemies4:
                if enemy4.colliderect(laser):
                    enlifes4[index_enemy] -= 1
                    laser_list.remove(laser)
                index_enemy += 1
        # Удаление пуль
        index_bul = 0
        for b in bullets:
            if b.bottom < -5:
                bullets.pop(index_bul)
                ammo += 1
            index_bul += 1

        # ЗАХВАТЧИКИ
        currentTime = pygame.time.get_ticks()
        currentTime1 = pygame.time.get_ticks()
        currentTime2 = pygame.time.get_ticks()
        currentTime3 = pygame.time.get_ticks()
        currentTime4 = pygame.time.get_ticks()
        # Создание противников
        if currentTime - lastTime > enemycd:
            x_enemy = random.randint(10, WIDTH - we)
            enemies.append(pygame.Rect(x_enemy, -he, we, he))
            enlifes.append(elife)
            lastTime = currentTime
            enemycd = random.randint(100, 4000)

        if currentTime1 - lastTime1 > enemycd1 and points > 19:
            x_enemy1 = random.randint(10, WIDTH - we1)
            enemies1.append(pygame.Rect(x_enemy1, -he1, we1, he1))
            enlifes1.append(elife1)
            lastTime1 = currentTime1
            enemycd1 = random.randint(200, 6000)

        if currentTime2 - lastTime2 > enemycd2 and points > 39:
            x_enemy2 = random.randint(10, WIDTH - we2)
            enemies2.append(pygame.Rect(x_enemy2, -he2, we2, he2))
            enlifes2.append(elife2)
            firecd_list.append(firecd)
            lastTime2 = currentTime2
            enemycd2 = random.randint(400, 7000)

        if currentTime3 - lastTime3 > enemycd3 and points > 59:
            x_enemy3 = random.randint(10, WIDTH - we3)
            enemies3.append(pygame.Rect(x_enemy3, -he3, we3, he3))
            enlifes3.append(elife2)
            firecd_list3.append(firecd)
            lastTime3 = currentTime3
            enemycd3 = random.randint(400, 8000)

        if currentTime4 - lastTime4 > enemycd4 and points > 79:
            x_enemy4 = random.randint(10, WIDTH - we4)
            enemies4.append(pygame.Rect(x_enemy4, -he4, we4, he4))
            enlifes4.append(elife4)
            lastTime4 = currentTime4
            enemycd4 = random.randint(200, 6000)

        # Отрисовка противников
        for enemy in enemies:
            screen.blit(enemyImage, (enemy.left, enemy.top))
            enemy.top += 2

        for enemy1 in enemies1:
            screen.blit(enemyImage1, (enemy1.left, enemy1.top))
            enemy1.top += 4
            if hero.left > enemy1.left - 1:
                enemy1.left += 1
            else:
                enemy1.top -= 1
            if hero.left < enemy1.left + 1:
                enemy1.left -= 1
            else:
                enemy1.top -= 1

        index_enemy = 0
        for enemy2 in enemies2:
            screen.blit(enemyImage2, (enemy2.left, enemy2.top))
            enemy2.top += 2
            if firecd_list[index_enemy] < 1:
                enbulRect = pygame.Rect(enemy2.left + 50, enemy2.top + 20, wb, hb)
                enbullets.append(enbulRect)
                firecd_list[index_enemy] = 100
            firecd_list[index_enemy] -= 1
            index_enemy += 1
        index_enemy = 0

        for enemy3 in enemies3:
            screen.blit(enemyImage3, (enemy3.left, enemy3.top))
            enemy3.top += 1
            if firecd_list3[index_enemy] < 1:
                enbulRect1 = pygame.Rect(enemy3.left + 50, enemy3.top + 20, wb, hb)
                enbulRect2 = pygame.Rect(enemy3.left + 50, enemy3.top + 20, wb, hb)
                enbullets1.append(enbulRect1)
                enbullets2.append(enbulRect2)
                firecd_list3[index_enemy] = 150
            firecd_list3[index_enemy] -= 1
            index_enemy += 1

        for enemy4 in enemies4:
            screen.blit(enemyImage4, (enemy4.left, enemy4.top))
            enemy4.top += random.randint(0, 1)
        # Удаление противников
        index_enemy = 0
        for enemy in enemies:
            if enemy.top > HEIGHT:
                del enemies[index_enemy]
                del enlifes[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enemy1 in enemies1:
            if enemy1.top > HEIGHT:
                del enemies1[index_enemy]
                del enlifes1[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enemy2 in enemies2:
            if enemy2.top > HEIGHT:
                del enemies2[index_enemy]
                del enlifes2[index_enemy]
                del firecd_list[index_enemy]
            index_enemy += 1

        index_enemy = 0
        for enemy3 in enemies3:
            if enemy3.top > HEIGHT:
                del enemies3[index_enemy]
                del enlifes3[index_enemy]
                del firecd_list3[index_enemy]
            index_enemy += 1
        # ЗВЕЗДЫ
        if points > 19:
            img_index = 1
        if points > 39:
            img_index = 2
        if points > 59:
            img_index = 3
        if points > 79:
            img_index = 4
        starcd -= 1
        if starcd < 0:
            x_star = random.randint(0, WIDTH - ws)
            star = pygame.Rect(x_star, -hs, ws, hs)
            stars.append(star)
            starcd = random.randint(10, 20)

        for star in stars:
            screen.blit(starpng[img_index], (star.left, star.top))
            star.top += 4
            if star.top > HEIGHT:
                stars.remove(star)

        if star1cd < 0:
            x_star = random.randint(0, WIDTH - ws)
            stars1.append(pygame.Rect(x_star, -hs, ws, hs))
            star1cd = random.randint(20, 40)

        # Отрисовка звезд
        for star1 in stars1:
            screen.blit(starpng[img_index], (star1.left, star1.top))
            star1.top += 1.5
            if star1.top > HEIGHT:
                stars1.remove(star1)
        star1cd -= 1

        # Отрисовка персонажа
        screen.blit(heroImg, (hero.left, hero.top))

        if GO:
            pygame.mixer.music.pause()
            screen.fill(BLACK)
            pointsT = pygame.font.Font('visitor1.ttf', 24)
            points_text = pointsT.render('points  :  ' + str(points), True, WHITE)
            screen.blit(gameover_text, (WIDTH / 2 - 180, HEIGHT / 2 - 80))
            screen.blit(points_text, (WIDTH / 2 - 80, HEIGHT / 2 + 30))
            pygame.display.update()
            boosters = []
            enemies = []
            enlifes = []
            enemies1 = []
            enlifes1 = []
            enemies2 = []
            enlifes2 = []
            firecd_list = []
            enemies3 = []
            enlifes3 = []
            firecd_list3 = []
            enemies4 = []
            enlifes4 = []
            firecd_list4 = []
            enemies5 = []
            enlifes5 = []
            enbullets = []
            enbullets1 = []
            enbullets2 = []
            bullets = []
            bullets1 = []
            bullets2 = []
            bullets3 = []
            laser_list = []
            hero.x = WIDTH // 2
            hero.y = HEIGHT // 2
            GO = False
            LEFT = False
            RIGHT = False
            UP = False
            DOWN = False
            points = 0
            ammo = 3
            life = 3
            sp_left = 0
            sp_up = 0
            time.sleep(2)
            gamemode = 0
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

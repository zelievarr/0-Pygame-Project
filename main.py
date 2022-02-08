import pygame
import sys


def race_scene(location, driver, opponent, ep):
    surface = pygame.Surface(size, pygame.SRCALPHA)

    dist = 1000
    is_throttle = 0
    is_brake = 0
    speed_of_player = 0  # м/с

    speed_of_kakyoin = 0

    cars = pygame.sprite.Group()

    car_player = pygame.sprite.Sprite()
    if driver == 0:
        car_player.image = pygame.image.load("pictures/sprites/jotaro_zapor.png")
    car_player.rect = car_player.image.get_rect()
    car_player.rect.x = 500
    car_player.rect.y = 700

    car_enemy = pygame.sprite.Sprite()
    if opponent == 0:
        car_enemy.image = pygame.image.load("pictures/sprites/kakyoin_zhiga.png")
    elif opponent == 1:
        car_enemy.image = pygame.image.load("pictures/sprites/polnareff_moskvich.png")
    car_enemy.rect = car_enemy.image.get_rect()
    car_enemy.rect.x = 500
    car_enemy.rect.y = 650

    cars.add(car_enemy)
    cars.add(car_player)

    sizeb = 1920, 1080
    bgs = pygame.display.set_mode(sizeb)
    bgs1 = pygame.display.set_mode(sizeb)
    cur_bg_pose = 0
    cur_bg1_pose = 7680
    bgmove = pygame.USEREVENT + 1
    pygame.time.set_timer(bgmove, 33)
    splash = pygame.USEREVENT + 2
    pygame.time.set_timer(splash, 1000)
    timer = 0
    while True:
        bg = pygame.image
        if ep == 0:
            bg = pygame.image.load("pictures/backgrounds/spash_screen_0.png")
        elif ep == 1:
            bg = pygame.image.load("pictures/backgrounds/spash_screen_1.png")
        bgs.blit(bg, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == splash:
                timer += 1
        if timer == 3:
            break

    if location == 0:
        bg = pygame.image.load("pictures/backgrounds/race_street.png")
    bgs.blit(bg, (cur_bg_pose, 0))
    bgs1.blit(bg, (cur_bg1_pose, 0))

    cars.draw(screen)
    screen.blit(screen, (0, 0))
    pygame.display.flip()

    while True:
        if is_throttle == 1:
            if speed_of_player < 30:
                speed_of_player += 0.25
            else:
                speed_of_player = 30
        else:
            if speed_of_player > 0:
                speed_of_player -= 0.05
            else:
                speed_of_player = 0
        if is_brake == 1:
            if speed_of_player > 0:
                speed_of_player -= 0.3
            else:
                speed_of_player = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    is_throttle = 1
                if event.key == pygame.K_s:
                    is_brake = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    is_throttle = 0
                if event.key == pygame.K_s:
                    is_brake = 0
            if event.type == bgmove:
                if speed_of_kakyoin < 28:
                    speed_of_kakyoin += 0.28
                else:
                    speed_of_kakyoin = 28
                cur_bg_pose -= speed_of_player * 21 / 30
                cur_bg1_pose -= speed_of_player * 21 / 30
                dist -= speed_of_player / 30
                if cur_bg_pose <= -7680:
                    cur_bg_pose = 0
                    cur_bg1_pose = 7680
        car_enemy.rect.x += speed_of_kakyoin - speed_of_player
        bgs.blit(bg, (cur_bg_pose, 0))
        bgs1.blit(bg, (cur_bg1_pose, 0))
        cars.draw(screen)
        font = pygame.font.Font(None, 50)
        text = font.render("Осталось: " + str(int(dist)), True, (0, 0, 0))
        screen.blit(text, (1600, 20))
        pygame.display.flip()

        if dist <= 0:
            if car_enemy.rect.x <= 500:
                result = 1
            else:
                result = 0
            while True:
                surface.fill((219, 193, 162, 200), pygame.Rect(80, 850, 1760, 200))
                pygame.draw.polygon(surface, (137, 81, 58), [(1750, 850), (1750, 1050), (1840, 950)], 0)
                pygame.draw.polygon(surface, (137, 81, 58), [(150, 850), (150, 1050), (80, 950)], 0)
                screen.blit(surface, (0, 0))
                font = pygame.font.Font(None, 75)
                if result == 1:
                    text = font.render("Вы выиграли.", True, (94, 70, 61))
                else:
                    text = font.render("Вы проиграли.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 1750 < pygame.mouse.get_pos()[0] < 1840 and 850 < pygame.mouse.get_pos()[1] < 1050:
                            return result
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


def main_game():
    part = 0
    res = -1
    res1 = -1
    current_replica = 0
    current_scene = 0
    surface = pygame.Surface(size, pygame.SRCALPHA)
    while True:
        if part == 0:  # первая сцена с тюрячкой
            if current_scene == 0:
                bg = pygame.image.load("pictures/backgrounds/0_jail.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 1:
                bg = pygame.image.load("pictures/backgrounds/0_avdol.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 2:
                bg = pygame.image.load("pictures/backgrounds/0_jotaro.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 3:
                bg = pygame.image.load("pictures/backgrounds/0_dio_photo.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 4:
                bg = pygame.image.load("pictures/backgrounds/0_joseph_zoom.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 5:
                bg = pygame.image.load("pictures/backgrounds/0_jotaro_zoom.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 6:
                bg = pygame.image.load("pictures/backgrounds/0_jotaro_no_keys.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 7:
                bg = pygame.image.load("pictures/backgrounds/0_jotaro_keys.png")
                screen.blit(bg, (0, 0))
            surface.fill((219, 193, 162, 200), pygame.Rect(80, 850, 1760, 200))
            pygame.draw.polygon(surface, (137, 81, 58), [(1750, 850), (1750, 1050), (1840, 950)], 0)
            pygame.draw.polygon(surface, (137, 81, 58), [(150, 850), (150, 1050), (80, 950)], 0)
            screen.blit(surface, (0, 0))
            if current_replica == 0:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Давно тебя не было в уличных гонках, Джотаро.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 1:
                current_scene = 1
                font = pygame.font.Font(None, 50)
                text = font.render("Абдул:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Мистер Джостар говорит правду. Засиделся ты на зоне.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 2:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Есть одно важное дело. Один известный гонщик...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 3:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Пошёл н****, дед. Кто так вообще начинает диалог?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 4:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Этот ниггер рядом с тобой. Я его знаю?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 5:
                current_scene = 1
                font = pygame.font.Font(None, 50)
                text = font.render("Абдул:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Мистер Джостар мой хозяин.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 6:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Всё верно, я купил Абдула в Каире за 10 долларов.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 7:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("У него весьма себе неплохой мозг, даром что ж*** черная.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 8:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Яре яре дазе. Кринжанул, дед.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 9:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Кхм, вернёмся к теме моего визита.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 10:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Один известный гонщик, ", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 11:
                current_scene = 3
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Дио Брандо", True, (0, 0, 0))
                screen.blit(text, (217, 928))
                font = pygame.font.Font(None, 75)
                text = font.render("Дио Брандо", True, (203, 158, 23))
                screen.blit(text, (220, 925))
            elif current_replica == 12:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("В лохматые года угнал у моего деда \"Москвич\".", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 13:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("И что с того?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 14:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("А то, что ныне на нём он забирает все кубки.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 15:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Надо проучить старого гея и забрать машину деда.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 16:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Видишь ли, Дио выпил 20 литров 76-го бензина...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 17:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...и теперь абсолютно бессмертен.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 18:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("А от меня тебе что надо?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 19:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Будешь за рулём.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 20:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Я уже стар для таких приколов,", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 21:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("А этот...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 22:
                current_scene = 1
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 23:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...не то, что водить. Писать не умеет.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 24:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("На выход, Джотаро.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 25:
                current_scene = 5
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Исчезни. Я тебя не звал.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 26:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Твоя мать умрёт, если мы не выграем Дио.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 27:
                current_scene = 5
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Какого хрена, дед?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 28:
                current_scene = 5
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("В этой игре у нас нет стендов.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 29:
                current_scene = 5
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Дио ничего нам не сделает.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 30:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Ах да, забыл.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 31:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Вот ключи.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 32:
                current_scene = 5
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Хорошо, дед.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 33:
                current_scene = 6
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Я возьму.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 34:
                current_scene = 7
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 35:
                current_scene = 7
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...это что, ключи от \"Запорожца\"?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 36:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Да, это они.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 37:
                current_scene = 7
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Ты совсем умом тронулся?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 38:
                current_scene = 7
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Как ты собираешься выигрывать кого-то на этом??", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 39:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Напомню тебе, что у Дио 401 \"Москвич\"!", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 40:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Они производились с 54-го по 56-ой.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 41:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Мощность его двигателя – 26 л.с.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 42:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("У моего \"Запорожца\"...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 43:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...сорок две лошадиные силы!", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 44:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Это при примерно равной массе.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 45:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Не знаю, что у него под капотом...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 46:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...и как он забирает кубки на гонках...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 47:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...но нам он не противник!", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 47:
                current_scene = 4
                font = pygame.font.Font(None, 50)
                text = font.render("Джозеф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...но нам он не противник!", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 48:
                current_scene = 7
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Яре яре...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 49:
                current_scene = 6
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 50:
                current_scene = 6
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...ладно, идём.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 51:
                current_scene = 6
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 52:
                part = 1
                current_replica = 0
                current_scene = 0

        elif part == 1:
            if current_scene == 0:
                bg = pygame.image.load("pictures/backgrounds/1_no_one.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 1:
                bg = pygame.image.load("pictures/backgrounds/1_jotaro.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 2:
                bg = pygame.image.load("pictures/backgrounds/1_both.png")
                screen.blit(bg, (0, 0))
            surface.fill((219, 193, 162, 200), pygame.Rect(80, 850, 1760, 200))
            pygame.draw.polygon(surface, (137, 81, 58), [(1750, 850), (1750, 1050), (1840, 950)], 0)
            pygame.draw.polygon(surface, (137, 81, 58), [(150, 850), (150, 1050), (80, 950)], 0)
            screen.blit(surface, (0, 0))
            if current_replica == 0:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 1:
                current_scene = 1
                font = pygame.font.Font(None, 50)
                text = font.render("", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 2:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 3:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Э, мужик, че за ведро?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 4:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Твоя мать ведро.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 5:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("А это запорожец деда.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 6:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Про мать лишнее было.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 7:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Значит так.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 8:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Едем до следующего светофора, это километр.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 9:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Если проигрываешь - твоя мать ведро.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 10:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 11:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...идёт?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 12:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Идёт.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 13:
                if res == -1:
                    res = race_scene(0, 0, 0, 0)
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            if res == 1:
                if current_replica == 14:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("...б****!", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 15:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Чел гений.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 16:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Как??", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 17:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("У меня машина мощнее. Быстрее.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 18:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("А меня обгоняет чел на запорожце.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 19:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Всё дело в топливе.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 20:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Не знаю, что именно дед льёт в бак...", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 21:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("..но это точно не обычный бензин.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 22:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Заслуживает уважения.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 23:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Я поеду с вами.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 24:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Ок.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 25:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("...", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 26:
                    part = 2
                    current_scene = 0
                    current_replica = 0
            else:
                if current_replica == 14:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Ха-ха-ха!", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 15:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Чел гений.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 16:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Твоя мать ведро.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 17:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("...", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 18:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("...", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Игра окончена. Нажмите, чтобы выйти.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 19:
                    pygame.quit()
                    sys.exit()

        elif part == 2:
            if current_scene == 0:
                bg = pygame.image.load("pictures/backgrounds/2_no_one.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 1:
                bg = pygame.image.load("pictures/backgrounds/2_jotaro.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 2:
                bg = pygame.image.load("pictures/backgrounds/2_both.png")
                screen.blit(bg, (0, 0))
            elif current_scene == 3:
                bg = pygame.image.load("pictures/backgrounds/CONTINUED.png")
                screen.blit(bg, (0, 0))
            surface.fill((219, 193, 162, 200), pygame.Rect(80, 850, 1760, 200))
            pygame.draw.polygon(surface, (137, 81, 58), [(1750, 850), (1750, 1050), (1840, 950)], 0)
            pygame.draw.polygon(surface, (137, 81, 58), [(150, 850), (150, 1050), (80, 950)], 0)
            screen.blit(surface, (0, 0))
            if current_replica == 0:
                current_scene = 0
                font = pygame.font.Font(None, 50)
                text = font.render("", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 1:
                current_scene = 1
                font = pygame.font.Font(None, 50)
                text = font.render("", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 2:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 3:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Польнарефф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Эй, парни, я вижу, что вы хотите погоняться!", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 4:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Нет, мы не хотим.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 5:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Польнарефф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Нет, вы точно хотите.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 6:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Нет.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 7:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Польнарефф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Да.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 8:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Нет.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 9:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Брось, что плохого произойдёт, если мы согласимся?", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 10:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("У нас мало времени.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 11:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Какёин:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Время не ограничено. Мы не торопимся.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 12:
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Джотаро:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("Так уж и быть. Ладно. Но только один раз.", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            elif current_replica == 13:
                if res1 == -1:
                    res1 = race_scene(0, 0, 1, 1)
                current_scene = 2
                font = pygame.font.Font(None, 50)
                text = font.render("Польнарефф:", True, (137, 81, 58))
                screen.blit(text, (170, 860))
                font = pygame.font.Font(None, 75)
                text = font.render("...", True, (94, 70, 61))
                screen.blit(text, (220, 925))
            if res1 == 1:
                if current_replica == 14:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Гений!", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 15:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("На таком ведре и победил меня, Польнареффа.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 16:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Я не эксперт, но судя по всему...", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 17:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("...подшаманил с топливом?", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 18:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Все вопросы к деду. Машина не моя.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 19:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("А где твой дед?", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 20:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Яре яре дазе, Какёин, куда делся дед??", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 21:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Без понятия, ты с самого начала был один", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 22:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Чёрт", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 23:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Твой дед гений. Я поеду с вами.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 24:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Хочу встретиться с ним!", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 25:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Хорошо.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 26:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Куда вы едете?", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 27:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Да, Джотаро, куда мы едем?", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 28:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Нам нужно победить Дио.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 29:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф и Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Дио???", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 30:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("*черт, дио это Бог по-итальянски*", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 31:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Какёин:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("*он что, спятил?*", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 32:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("*Какёин так удивился, он что-то знает?*", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 33:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("*лично я ничего не понимаю*", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 34:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Старый педик украл машину моего прапрадеда.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 35:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Я должен вернуть её деду!", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 36:
                    current_scene = 3
                    font = pygame.font.Font(None, 50)
                    text = font.render("", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Игра завершена. Нажмите, чтобы выйти.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 37:
                    pygame.quit()
                    sys.exit()
            else:
                if current_replica == 14:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Ха-ха-ха!", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 15:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Глотай пыль, школьник.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 16:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Польнарефф:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Твоя машина ведро.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 17:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("Джотаро:", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("...", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 18:
                    current_scene = 2
                    font = pygame.font.Font(None, 50)
                    text = font.render("...", True, (137, 81, 58))
                    screen.blit(text, (170, 860))
                    font = pygame.font.Font(None, 75)
                    text = font.render("Игра окончена. Нажмите, чтобы выйти.", True, (94, 70, 61))
                    screen.blit(text, (220, 925))
                elif current_replica == 19:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1750 < pygame.mouse.get_pos()[0] < 1840 and 850 < pygame.mouse.get_pos()[1] < 1050:
                    current_replica += 1
                elif 80 < pygame.mouse.get_pos()[0] < 150 and 850 < pygame.mouse.get_pos()[1] < 1050:
                    if current_replica > 0:
                        current_replica -= 1
                    else:
                        pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


def menu():
    while True:
        menu_image = pygame.image.load("pictures/backgrounds/menu.png")
        screen.blit(menu_image, (0, 0))

        # надпись меню
        font = pygame.font.Font(None, 150)
        text = font.render("Меню", True, (0, 0, 0))
        screen.blit(text, (175, 700))

        # отрисовка кнопки играть
        if 80 < pygame.mouse.get_pos()[0] < 580 and 800 < pygame.mouse.get_pos()[1] < 900:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main_game()
            screen.fill((0, 50, 150), pygame.Rect(80, 800, 500, 100))
        else:
            screen.fill((0, 150, 255), pygame.Rect(80, 800, 500, 100))

        font = pygame.font.Font(None, 100)
        text = font.render("Играть", True, (255, 255, 255))
        screen.blit(text, (205, 820))

        # отрисовка кнопки выйти
        if 80 < pygame.mouse.get_pos()[0] < 580 and 910 < pygame.mouse.get_pos()[1] < 1010:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
            screen.fill((0, 50, 150), pygame.Rect(80, 910, 500, 100))
        else:
            screen.fill((0, 150, 255), pygame.Rect(80, 910, 500, 100))

        font = pygame.font.Font(None, 100)
        text = font.render("Выйти", True, (255, 255, 255))
        screen.blit(text, (205, 930))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
menu()

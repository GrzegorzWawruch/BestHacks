import pygame
import time


play = True
play_2 = True
play_3 = True
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((800, 1000))
pygame.display.set_caption("my game")
window.fill("black")
clock.tick(60)
who_draw = 1
draw_pos_x = 0
draw_pos_y = 0
turn = 2
draw_menu = 3
win = 0
who_won = 0
tab = [[0,0,0],[0,0,0],[0,0,0]]
a = 0
b = 0


while play:

    font = pygame.font.SysFont('comicsans', 30)
    title = font.render('KOLKO i KRZYZYK', 1, "white")
    no_one_won_text = font.render('NO ONE WON', 1, "red")
    cross_won = font.render('CROSS WIN', 1, "red")
    circle_won = font.render('CIRCLE WON', 1, "red")
    play_again_text = font.render('PLAY AGAIN', 1, "red")
    play_text = font.render('PLAY', 1, "red")
    exit_text = font.render('EXIT', 1, "red")
    window.blit(title, (262, 20))


    if draw_menu % 3 == 0:
        pygame.draw.rect(window, "white", (200, 200, 400, 150))
        pygame.draw.rect(window, "white", (200, 600, 400, 150))
        window.blit(play_text, (360, 250))
        window.blit(exit_text, (360, 650))
        pygame.display.update()
    if draw_menu % 3 == 1:
        pygame.draw.rect(window, "white", (200, 200, 400, 150))
        pygame.draw.rect(window, "white", (200, 600, 400, 150))
        window.blit(play_again_text, (305, 250))
        window.blit(exit_text, (360, 650))
        if who_won == 1:
            window.blit(circle_won, (300,90))
        if who_won == 2:
            window.blit(cross_won, (300, 90))

        pygame.display.update()
    if draw_menu % 3 == 2:
        window.blit(no_one_won_text, (285, 90))
        pygame.draw.rect(window, "white", (200, 200, 400, 150))
        pygame.draw.rect(window, "white", (200, 600, 400, 150))
        window.blit(play_again_text, (305, 250))
        window.blit(exit_text, (360, 650))
        pygame.display.update()


    for event in pygame.event.get():
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            a, b = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            play = False

        if 200 < a < 600 and 600 < b < 750:
            play = False

        if 200 < a < 600 and 200 < b < 350:
            draw_menu = 4
            pygame.draw.rect(window, "black", (0, 0, 800, 1000))
            time.sleep(0.2)
            play_2 = True
            while play_2:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        play_2 = False
                        play = False
                window.blit(title, (262, 20))
                pygame.draw.line(window, "white", (0, 200), (1000, 200), 10)
                pygame.draw.line(window, "white", (30, 466), (770, 466), 6)
                pygame.draw.line(window, "white", (266, 230), (266, 970), 6)
                pygame.draw.line(window, "white", (532, 230), (532, 970), 6)
                pygame.draw.line(window, "white", (30, 732), (770, 732), 6)
                pygame.display.update()

                if turn % 2 == 0:
                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 263 and y < 466 and x > 30 and y > 230 and tab[0][0] == 0:
                            pygame.draw.circle(window, "white", (130, 337), 80)
                            pygame.draw.circle(window, "black", (130, 337), 75)
                            tab[0][0] = 1
                            win = 0

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 263 and y < 732 and x > 30 and y > 466 and tab[1][0] == 0:
                            pygame.draw.circle(window, "white", (130, 603), 80)
                            pygame.draw.circle(window, "black", (130, 603), 75)
                            tab[1][0] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 263 and y < 970 and x > 30 and y > 732 and tab[2][0] == 0:
                            pygame.draw.circle(window, "white", (130, 869), 80)
                            pygame.draw.circle(window, "black", (130, 869), 75)
                            tab[2][0] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 529 and y < 466 and x > 269 and y > 230 and tab[0][1] == 0:
                            pygame.draw.circle(window, "white", (396, 337), 80)
                            pygame.draw.circle(window, "black", (396, 337), 75)
                            tab[0][1] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 529 and y < 732 and x > 269 and y > 466 and tab[1][1] == 0:
                            pygame.draw.circle(window, "white", (396, 603), 80)
                            pygame.draw.circle(window, "black", (396, 603), 75)
                            tab[1][1] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 529 and y < 970 and x > 269 and y > 732 and tab[2][1] == 0:
                            pygame.draw.circle(window, "white", (396, 869), 80)
                            pygame.draw.circle(window, "black", (396, 869), 75)
                            tab[2][1] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 795 and y < 466 and x > 535 and y > 230 and tab[0][2] == 0:
                            pygame.draw.circle(window, "white", (662, 337), 80)
                            pygame.draw.circle(window, "black", (662, 337), 75)
                            tab[0][2] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 795 and y < 732 and x > 535 and y > 466 and tab[1][2] == 0:
                            pygame.draw.circle(window, "white", (662, 603), 80)
                            pygame.draw.circle(window, "black", (662, 603), 75)
                            tab[1][2] = 1

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 795 and y < 970 and x > 535 and y > 732 and tab[2][2] == 0:
                            pygame.draw.circle(window, "white", (662, 869), 80)
                            pygame.draw.circle(window, "black", (662, 869), 75)
                            tab[2][2] = 1

                if turn % 2 == 1:
                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 263 and y < 466 and x > 30 and y > 230 and tab[0][0] == 0:
                            pygame.draw.line(window, "white", (62, 257), (232, 415), 6)
                            pygame.draw.line(window, "white", (62, 415), (232, 257), 6)
                            tab[0][0] = 2
                            win = 0

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 263 and y < 732 and x > 30 and y > 466 and tab[1][0] == 0:
                            pygame.draw.line(window, "white", (62, 523), (232, 681), 6)
                            pygame.draw.line(window, "white", (62, 681), (232, 523), 6)
                            tab[1][0] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 263 and y < 970 and x > 30 and y > 732 and tab[2][0] == 0:
                            pygame.draw.line(window, "white", (62, 789), (232, 947), 6)
                            pygame.draw.line(window, "white", (62, 947), (232, 789), 6)
                            tab[2][0] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 529 and y < 466 and x > 269 and y > 230 and tab[0][1] == 0:
                            pygame.draw.line(window, "white", (298, 257), (500, 415), 6)
                            pygame.draw.line(window, "white", (298, 415), (500, 257), 6)
                            tab[0][1] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 529 and y < 732 and x > 269 and y > 466 and tab[1][1] == 0:
                            pygame.draw.line(window, "white", (298, 523), (500, 681), 6)
                            pygame.draw.line(window, "white", (298, 681), (500, 523), 6)
                            tab[1][1] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 529 and y < 970 and x > 269 and y > 732 and tab[2][1] == 0:
                            pygame.draw.line(window, "white", (298, 789), (500, 947), 6)
                            pygame.draw.line(window, "white", (298, 947), (500, 789), 6)
                            tab[2][1] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 795 and y < 466 and x > 535 and y > 230 and tab[0][2] == 0:
                            pygame.draw.line(window, "white", (575, 257), (760, 415), 6)
                            pygame.draw.line(window, "white", (575, 415), (760, 257), 6)
                            tab[0][2] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 795 and y < 732 and x > 535 and y > 466 and tab[1][2] == 0:
                            pygame.draw.line(window, "white", (575, 523), (760, 681), 6)
                            pygame.draw.line(window, "white", (575, 681), (760, 523), 6)
                            tab[1][2] = 2

                    if pygame.mouse.get_pressed(num_buttons=3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if x < 795 and y < 970 and x > 535 and y > 732 and tab[2][2] == 0:
                            pygame.draw.line(window, "white", (575, 789), (760, 947), 6)
                            pygame.draw.line(window, "white", (575, 947), (760, 789), 6)
                            tab[2][2] = 2

                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    turn = turn + 1
                    time.sleep(0.1)

                if tab[0][0] == tab[0][1] == tab[0][2] and tab[0][0] != 0:
                    pygame.draw.line(window, "red", (20, 330), (780, 330), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[0][0] == 1:
                        who_won = 1
                    if tab[0][0] == 2:
                        who_won = 2
                    play_2 = False


                if tab[1][0] == tab[1][1] == tab[1][2] and tab[1][0] != 0:
                    pygame.draw.line(window, "red", (20, 600), (780, 600), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[1][0] == 1:
                        who_won = 1
                    else:
                        who_won = 2

                if tab[2][0] == tab[2][1] == tab[2][2] and tab[2][0] != 0:
                    pygame.draw.line(window, "red", (20, 870), (780, 870), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[2][0] == 1:
                        who_won =1
                    else:
                        who_won =2

                if tab[0][0] == tab[1][0] == tab[2][0] and tab[0][0] != 0:
                    pygame.draw.line(window, "red", (130, 250), (130, 970), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[0][0] == 1:
                        who_won =1
                    else:
                        who_won =2

                if tab[0][1] == tab[1][1] == tab[2][1] and tab[0][1] != 0:
                    pygame.draw.line(window, "red", (398, 250), (398, 970), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[0][1] == 1:
                        who_won =1
                    else:
                        who_won =2

                if tab[0][2] == tab[1][2] == tab[2][2] and tab[0][2] != 0:
                    pygame.draw.line(window, "red", (667, 250), (667, 970), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[0][2] == 1:
                        who_won =1
                    else:
                        who_won =2

                if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] != 0:
                    pygame.draw.line(window, "red", (30, 250), (770, 970), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[0][0] == 1:
                        who_won =1
                    else:
                        who_won =2

                if tab[2][0] == tab[1][1] == tab[0][2] and tab[2][0] != 0:
                    pygame.draw.line(window, "red", (770, 250), (30, 970), 15)
                    pygame.display.update()
                    win = 1
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    draw_menu = 4
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(2)
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    if tab[2][0] == 1:
                        who_won =1
                    else:
                        who_won =2


                if tab[0][0] and tab[0][1] and tab[0][2] and tab[1][0] and tab[1][1] and tab[1][2] and tab[2][0] and tab[2][1] and tab[2][2] != 0 and win == 0:
                    draw_menu = 5
                    pygame.draw.rect(window, "black", (0, 0, 800, 1000))
                    for i in range(3):
                        for j in range(3):
                            tab[i][j] = 0
                    play_2 = False
                    a = 0
                    b = 0
                    time.sleep(0.2)

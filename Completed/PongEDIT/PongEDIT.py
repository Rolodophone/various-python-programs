import pygame
import random
import os.path
import math

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
bars = pygame.sprite.Group()
sprites = pygame.sprite.Group()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
l_blue = (0, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
f5 = pygame.font.Font(None, 200)
f4 = pygame.font.Font(None, 130)
f3 = pygame.font.Font(None, 90)
f2 = pygame.font.Font(None, 50)
f1_5 = pygame.font.Font(None, 35)
f1 = pygame.font.Font(None, 25)
if not os.path.isfile("pong_highscore.txt"):
    m = open("pong_highscore.txt", "w")
    m.close()
highscore_file = open("pong_highscore.txt", "r")
highscore = (highscore_file.read())
highscore_file.close()
global mode

def message(msg, colour, place, size):
    if size == f1:
        screen_text = f1.render(msg, True, colour, place)
    elif size == f2:
        screen_text = f2.render(msg, True, colour, place)
    elif size == f3:
        screen_text = f3.render(msg, True, colour, place)
    elif size == f4:
        screen_text = f4.render(msg, True, colour, place)
    elif size == f5:
        screen_text = f5.render(msg, True, colour, place)
    else:
        screen_text = f1_5.render(msg, True, colour, place)
    game_display.blit(screen_text, place)

def top_wins():
    Exit = False
    lost = True
    while not Exit:
        game_display.fill(l_blue)
        selected = 1
        message("TOP WINS!", red, [230, 100], f3)
        message("Top score:   " + str(t_points) + "                Bottom score:   " + str(b_points), red, [130, 250], f2)
        message("Play again", yellow, [320, 350], f2)
        message("Quit", red, [370, 450], f2)
        pygame.display.update()
        while lost:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit = True
                    lost = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and selected == 2:
                        selected = 1
                        message("Play again", yellow, [320, 350], f2)
                        message("Quit", red, [370, 450], f2)
                        pygame.display.update()
                    elif event.key == pygame.K_DOWN and selected == 1:
                        selected = 2
                        message("Play again", red, [320, 350], f2)
                        message("Quit", yellow, [370, 450], f2)
                        pygame.display.update()
                    elif event.key == pygame.K_SPACE:
                        if selected == 1:
                            if mode == "2classic":
                                mode_2classic()
                            elif mode == "2crazy":
                                mode_2crazy()
                        else:
                            sprites.empty()
                            main_menu()
    pygame.quit()
    quit()

def bottom_wins():
    Exit = False
    lost = True
    while not Exit:
        game_display.fill(l_blue)
        selected = 1
        message("BOTTOM WINS!", red, [190, 100], f3)
        message("Top score:   " + str(t_points) + "                Bottom score:   " + str(b_points), red, [130, 250], f2)
        message("Play again", yellow, [320, 350], f2)
        message("Quit", red, [370, 450], f2)
        pygame.display.update()
        while lost:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit = True
                    lost = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and selected == 2:
                        selected = 1
                        message("Play again", yellow, [320, 350], f2)
                        message("Quit", red, [370, 450], f2)
                        pygame.display.update()
                    elif event.key == pygame.K_DOWN and selected == 1:
                        selected = 2
                        message("Play again", red, [320, 350], f2)
                        message("Quit", yellow, [370, 450], f2)
                        pygame.display.update()
                    elif event.key == pygame.K_SPACE:
                        if selected == 1:
                            if mode == "2classic":
                                mode_2classic()
                            elif mode == "2crazy":
                                mode_2crazy()
                        else:
                            sprites.empty()
                            main_menu()
    pygame.quit()
    quit()

def crazy_reset():
    ball.speed = 10
    ball_paused = True
    ball.rect.x = 385
    if random.randrange(2) == 1:
        ball.rect.y = 20
        
    else:
        ball.rect.y = 550

def main_menu():
    selected = 1
    game_display.fill(white)
    message("PONG", green, [200, 40], f5)
    message("1 player", yellow, [330, 280], f2)
    message("2 player", black, [330, 380], f2)
    message("Quit", black, [360, 480], f2)
    pygame.display.update()
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected == 2:
                        selected = 1
                        message("1 player", yellow, [330, 280], f2)
                        message("2 player", black, [330, 380], f2)
                        pygame.display.update()
                    elif selected == 3:
                        selected = 2
                        message("2 player", yellow, [330, 380], f2)
                        message("Quit", black, [360, 480], f2)
                        pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    if selected == 1:
                        selected = 2
                        message("2 player", yellow, [330, 380], f2)
                        message("1 player", black, [330, 280], f2)
                        pygame.display.update()
                    elif selected == 2:
                        selected = 3
                        message("Quit", yellow, [360, 480], f2)
                        message("2 player", black, [330, 380], f2)
                        pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    if selected == 1:
                        p1_mode_select()
                    elif selected == 2:
                        p2_mode_select()
                    elif selected == 3:
                        playing = False

    pygame.quit()
    quit()

def p1_mode_select():
    selected = 1
    game_display.fill(white)
    message("SELECT GAMEMODE", green, [80, 80], f3)
    message("Classic", yellow, [330, 280], f2)
    message("Crazy", black, [325, 380], f2)
    message("Back", black, [350, 480], f2)
    pygame.display.update()
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    mainMenu()
                elif event.key == pygame.K_c:
                    mode_classic()
                elif event.key == pygame.K_s:
                    mode_sandbox()
                if event.key == pygame.K_UP:
                    if selected == 2:
                        selected = 1
                        message("Classic", yellow, [330, 280], f2)
                        message("Crazy", black, [325, 380], f2)
                        pygame.display.update()
                    elif selected == 3:
                        selected = 2
                        message("Crazy", yellow, [325, 380], f2)
                        message("Back", black, [350, 480], f2)
                        pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    if selected == 1:
                        selected = 2
                        message("Crazy", yellow, [325, 380], f2)
                        message("Classic", black, [330, 280], f2)
                        pygame.display.update()
                    elif selected == 2:
                        selected = 3
                        message("Back", yellow, [350, 480], f2)
                        message("Crazy", black, [325, 380], f2)
                        pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    if selected == 1:
                        mode_1classic()
                    elif selected == 2:
                        mode_1crazy()
                    elif selected == 3:
                        main_menu()
                        
    pygame.quit()
    quit()

def p2_mode_select():
    selected = 1
    game_display.fill(white)
    message("SELECT GAMEMODE", green, [80, 80], f3)
    message("Classic", yellow, [330, 280], f2)
    message("Crazy", black, [355, 380], f2)
    message("Back", black, [355, 480], f2)
    pygame.display.update()
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected == 2:
                        selected = 1
                        message("Classic", yellow, [330, 280], f2)
                        message("Crazy", black, [355, 380], f2)
                        pygame.display.update()
                    elif selected == 3:
                        selected = 2
                        message("Crazy", yellow, [355, 380], f2)
                        message("Back", black, [355, 480], f2)
                        pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    if selected == 1:
                        selected = 2
                        message("Crazy", yellow, [355, 380], f2)
                        message("Classic", black, [330, 280], f2)
                        pygame.display.update()
                    elif selected == 2:
                        selected = 3
                        message("Back", yellow, [355, 480], f2)
                        message("Crazy", black, [355, 380], f2)
                        pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    if selected == 1:
                        mode_2classic()
                    elif selected == 2:
                        mode_2crazy()
                    elif selected == 3:
                        main_menu()
    
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(l_blue)
        pygame.draw.circle(self.image, black, [15, 15], 15)
        self.dir = [0, "R", 45]
        self.rect = self.image.get_rect()
        self.speed = 10
    def move(self):
        move_x = math.cos(self.dir[2]) * self.speed
        move_y = math.sin(self.dir[2]) * self.speed
        if self.dir[1] == "L":
            self.rect.x -= move_x
        else:
            self.rect.x += move_x
        if self.dir[0] > 0:
            self.rect.y -= move_y
        else:
            self.rect.y += move_y
            
class Bar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([200, 20])
        self.image.fill(black)
        self.rect = self.image.get_rect()

class Edge(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.rect = self.image.get_rect()

def mode_2classic():
    global t_points
    global b_points
    global mode


    mode = "2classic"
    a_down = False
    d_down = False
    l_down = False
    r_down = False
    paused = False
    game_over = False
    playing = True
    t_points = 0
    b_points = 0
    ball_paused = True
    
    game_display.fill(l_blue)
    
    ball = Ball()
    top_bar = Bar()
    bottom_bar = Bar()
    l_edge = Edge(500, 1600)
    r_edge = Edge(500, 1600)
    t_edge = Edge(1800, 500)
    b_edge = Edge(1800, 500)
    
    bars.add(top_bar)
    bars.add(bottom_bar)
    
    sprites.add(ball)
    sprites.add(top_bar)
    sprites.add(bottom_bar)
    sprites.add(l_edge)
    sprites.add(r_edge)
    sprites.add(t_edge)
    sprites.add(b_edge)
    
    top_bar.rect.x = 300
    top_bar.rect.y = 0
    bottom_bar.rect.x = 300
    bottom_bar.rect.y = 580
    ball.rect.x = 400
    ball.rect.y = 300
    l_edge.rect.x = -500
    l_edge.rect.y = -500
    r_edge.rect.x = 800
    r_edge.rect.y = -500
    t_edge.rect.x = -500
    t_edge.rect.y = -500
    b_edge.rect.x = -500
    b_edge.rect.y = 600
    
    pygame.display.update()
    while playing:
        if paused:
            game_display.fill(l_blue)
            message("PAUSED", green, [120, 231], f5)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        a_down = True
                    elif event.key == pygame.K_d:
                        d_down = True
                    elif event.key == pygame.K_LEFT:
                        l_down = True
                    elif event.key == pygame.K_RIGHT:
                        r_down = True
                    elif event.key == pygame.K_SPACE:
                        paused = False
                    elif event.key == pygame.K_q:
                        sprites.empty()
                        main_menu()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        a_down = False
                    elif event.key == pygame.K_d:
                        d_down = False
                    elif event.key == pygame.K_LEFT:
                        l_down = False
                    elif event.key == pygame.K_RIGHT:
                        r_down = False    
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        a_down = True
                    elif event.key == pygame.K_d:
                        d_down = True
                    elif event.key == pygame.K_LEFT:
                        l_down = True
                    elif event.key == pygame.K_RIGHT:
                        r_down = True
                    elif event.key == pygame.K_SPACE:
                        if ball_paused:
                            m = random.randrange(2)
                            if m == 0:
                                ball.dir[0] = random.randrange(10, 80)
                            else:
                                ball.dir[0] = random.randrange(-80, -10)
                            m = random.randrange(2)
                            if m == 0:
                                ball.dir[1] = "L"
                            else:
                                ball.dir[1] = "R"
                            ball_paused = False
                        else:
                            paused = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        a_down = False
                    elif event.key == pygame.K_d:
                        d_down = False
                    elif event.key == pygame.K_LEFT:
                        l_down = False
                    elif event.key == pygame.K_RIGHT:
                        r_down = False
                    
            game_display.fill(l_blue)
            if a_down:
                bottom_bar.rect.x -= 15
                if bottom_bar.rect.x < 0:
                    bottom_bar.rect.x += 15
            if d_down:
                bottom_bar.rect.x += 15
                if bottom_bar.rect.x > 600:
                    bottom_bar.rect.x -= 15
            if l_down:
                top_bar.rect.x -= 15
                if top_bar.rect.x < 0:
                    top_bar.rect.x += 15
            if r_down:
                top_bar.rect.x += 15
                if top_bar.rect.x > 600:
                    top_bar.rect.x -= 15

            collisions = pygame.sprite.spritecollide(ball, sprites, False)
            if len(collisions) > 1:
                if top_bar in collisions or bottom_bar in collisions:
                    ball.dir[0] = -ball.dir[0]
                    ball.speed += 1
                if l_edge in collisions:
                    ball.dir[1] = "R"
                if r_edge in collisions:
                    ball.dir[1] = "L"
                if t_edge in collisions:
                    b_points += 1
                    ball.speed = 10
                    if b_points == 10:
                        bottom_wins()
                    else:  
                        ball.rect.x = 400
                        ball.rect.y = 300
                        ball_paused = True
                if b_edge in collisions:
                    t_points += 1
                    ball.speed = 10
                    print(t_points)
                    if t_points == 10:
                        top_wins()
                    else:  
                        ball.rect.x = 400
                        ball.rect.y = 300
                        ball_paused = True

            if not ball_paused:
                ball.move()
            sprites.draw(game_display)
            message(str(t_points), red, [400, 30], f2)
            message(str(b_points), red, [400, 550], f2)
            pygame.display.update()
            clock.tick(30)

    pygame.quit()
    quit()

def mode_2crazy():
    global t_points
    global b_points
    global mode

    mode = "2crazy"
    a_down = False
    d_down = False
    l_down = False
    r_down = False
    paused = False
    game_over = False
    playing = True
    t_points = 0
    b_points = 0
    
    game_display.fill(l_blue)
    
    ball = Ball()
    top_bar = Bar()
    bottom_bar = Bar()
    middle_bar = Bar()
    l_edge = Edge(500, 1600)
    r_edge = Edge(500, 1600)
    t_edge = Edge(1800, 500)
    b_edge = Edge(1800, 500)
    
    bars.add(top_bar)
    bars.add(bottom_bar)
    
    sprites.add(ball)
    sprites.add(top_bar)
    sprites.add(bottom_bar)
    sprites.add(l_edge)
    sprites.add(r_edge)
    sprites.add(t_edge)
    sprites.add(b_edge)
    sprites.add(middle_bar)
    
    top_bar.rect.x = 300
    top_bar.rect.y = 0
    bottom_bar.rect.x = 300
    bottom_bar.rect.y = 580
    middle_bar.rect.x = 300
    middle_bar.rect.y = 290
    crazy_reset()
    l_edge.rect.x = -500
    l_edge.rect.y = -500
    r_edge.rect.x = 800
    r_edge.rect.y = -500
    t_edge.rect.x = -500
    t_edge.rect.y = -500
    b_edge.rect.x = -500
    b_edge.rect.y = 600
    
    pygame.display.update()
    while playing:
        if paused:
            game_display.fill(l_blue)
            message("PAUSED", green, [120, 231], f5)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        a_down = True
                    elif event.key == pygame.K_d:
                        d_down = True
                    elif event.key == pygame.K_LEFT:
                        l_down = True
                    elif event.key == pygame.K_RIGHT:
                        r_down = True
                    elif event.key == pygame.K_SPACE:
                        paused = False
                    elif event.key == pygame.K_q:
                        sprites.empty()
                        main_menu()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        a_down = False
                    elif event.key == pygame.K_d:
                        d_down = False
                    elif event.key == pygame.K_LEFT:
                        l_down = False
                    elif event.key == pygame.K_RIGHT:
                        r_down = False    
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        a_down = True
                    elif event.key == pygame.K_d:
                        d_down = True
                    elif event.key == pygame.K_LEFT:
                        l_down = True
                    elif event.key == pygame.K_RIGHT:
                        r_down = True
                    elif event.key == pygame.K_SPACE:
                        if ball_paused:
                            m = random.randrange(2)
                            if m == 0:
                                ball.dir[0] = random.randrange(10, 81)
                            else:
                                ball.dir[0] = random.randrange(-80, -10)
                            m = random.randrange(2)
                            if m == 0:
                                ball.dir[1] = "L"
                            else:
                                ball.dir[1] = "R"
                            ball_paused = False
                        else:
                            paused = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        a_down = False
                    elif event.key == pygame.K_d:
                        d_down = False
                    elif event.key == pygame.K_LEFT:
                        l_down = False
                    elif event.key == pygame.K_RIGHT:
                        r_down = False
                    
            game_display.fill(l_blue)
            if a_down and bottom_bar.rect.x >= 15:
                bottom_bar.rect.x -= 15
            if a_down and middle_bar.rect.x >= 15:
                middle_bar.rect.x += 15
            if d_down and bottom_bar.rect.x <= 585:
                bottom_bar.rect.x += 15
            if d_down and middle_bar.rect.x <= 585:
                middle_bar.rect.x -= 15
            if l_down and top_bar.rect.x >= 15:
                top_bar.rect.x -= 15
            if l_down and middle_bar.rect.x >= 15:
                middle_bar.rect.x += 15
            if r_down and top_bar.rect.x <= 585:
                top_bar.rect.x += 15
            if r_down and middle_bar.rect.x <= 585:
                middle_bar.rect.x -= 15

            collisions = pygame.sprite.spritecollide(ball, sprites, False)
            if len(collisions) > 1:
                if top_bar in collisions or bottom_bar in collisions or middle_bar in collisions:
                    ball.dir[0] = -ball.dir[0]
                    ball.speed += 1
                if l_edge in collisions:
                    ball.dir[1] = "R"
                if r_edge in collisions:
                    ball.dir[1] = "L"
                if t_edge in collisions:
                    b_points += 1
                    crazy_reset()
                    if b_points == 10:
                        bottom_wins()
                if b_edge in collisions:
                    t_points += 1
                    crazy_reset()
                    if t_points == 10:
                        top_wins()

            if not ball_paused:
                ball.move()
            sprites.draw(game_display)
            message(str(t_points), red, [400, 30], f2)
            message(str(b_points), red, [400, 550], f2)
            pygame.display.update()
            clock.tick(30)

    pygame.quit()
    quit()
    
main_menu()

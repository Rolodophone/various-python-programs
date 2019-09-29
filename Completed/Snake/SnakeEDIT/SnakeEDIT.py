import pygame
import random
import os.path


pygame.init()
pygame.font.init()


display_width = 800
display_height = 600
block_size = 10
clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 100, 0)
l_blue = (0, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
y_dead = "Oops you broke the game!"
f5 = pygame.font.Font(None, 200)
f4 = pygame.font.Font(None, 130)
f3 = pygame.font.Font(None, 90)
f2 = pygame.font.Font(None, 50)
f1_5 = pygame.font.Font(None, 35)
f1 = pygame.font.Font(None, 25)
if not os.path.isfile("snake_highscore.txt"):
    m = open("snake_highscore.txt", "w")
    m.close()
highscore_file = open("snake_highscore.txt", "r")
highscore = (highscore_file.read())
highscore_file.close()
global mode

def snake(block_size, snakelist, colour):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, colour, [XnY[0], XnY[1], block_size, block_size])


def message(msg, colour, place, size):
    screen_text = size.render(msg, True, colour, place)
    gameDisplay.blit(screen_text, place)


def mode_classic():

    speed = 25
    paused = False
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    rand_apple_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple_y = random.randrange(0, display_height - block_size, block_size)
    snakelist = []
    snakelength = 1
    score = 0
    global highscore
    highscore_int = 0
    while not gameExit:
        while gameOver:
            gameDisplay.fill(l_blue)
            try:
                highscore_int = int(highscore)
            except:
                m = 0
            global highscore_int
            if score > highscore_int:
                highscore = score
                highscore_file = open("snake_highscore.txt", "w")
                highscore_file.write(str(highscore))
                highscore_file.close()
            lost = True
            selected = 1
            message("GAME OVER", red, [220, 100], f3)
            message("Score:   " + str(score) + "                Highscore:   " + str(highscore), red, [130, 250], f2)
            message("Play again", yellow, [320, 350], f2)
            message("Quit", red, [370, 450], f2)
            pygame.display.update()
            while lost:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
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
                                mode_classic()
                            else:
                                mainMenu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    paused = False
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    paused = False
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    paused = False
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    paused = False
                elif event.key == pygame.K_SPACE:
                    lead_x_change = 0
                    lead_y_change = 0
                    paused = True
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            y_dead = "You crashed into the wall!"

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(l_blue)
        message(str(score), white, [10, 10], f3)
        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size, block_size])
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        if not paused:
            snakelist.append(snakehead)
            if len(snakelist) > snakelength:
                del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True
                y_dead = "You ran into yourself!"
        snake(block_size, snakelist, green)
        pygame.display.update()
        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple_y = random.randrange(0, display_height - block_size, block_size)
            snakelength += 1
            score += 1
            speed += 0.5
        clock.tick(speed)


    pygame.quit()
    quit()

def mode_sandbox():

    paused = False
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = -10
    rand_apple_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple_y = random.randrange(0, display_height - block_size, block_size)
    snakelist = []
    snakelength = 1
    score = 0
    while not gameExit:
        while gameOver:
            gameDisplay.fill(l_blue)
            lost = True
            selected = 1
            message("GAME OVER", red, [220, 100], f3)
            message("Score:   " + str(score) + "                Highscore:   " + str(highscore), red, [130, 250], f2)
            message("Play again", yellow, [320, 350], f2)
            message("Quit", red, [370, 450], f2)
            pygame.display.update()
            while lost:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
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
                                mode_sandbox()
                            else:
                                mainMenu()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    paused = False
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    paused = False
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    paused = False
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    paused = False
                elif event.key == pygame.K_b:
                    snakelength += 1
                    score += 1
                elif event.key == pygame.K_n:
                    snakelength += 10
                    score += 10
                elif event.key == pygame.K_m:
                    snakelength += 100
                    score += 100
                elif event.key == pygame.K_SPACE:
                    lead_x_change = 0
                    lead_y_change = 0
                    paused = True
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            y_dead = "You crashed into the wall!"

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(l_blue)
        message(str(score), white, [10, 10], f3)
        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size, block_size])
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        if not paused:
            snakelist.append(snakehead)
            if len(snakelist) > snakelength:
                del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True
                y_dead = "You ran into yourself!"
        snake(block_size, snakelist, green)
        pygame.display.update()
        if lead_x == rand_apple_x and lead_y == rand_apple_y:
            rand_apple_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple_y = random.randrange(0, display_height - block_size, block_size)
            snakelength += 1
            score += 1
        clock.tick(30)


    pygame.quit()
    quit()

def mode_slither():

    global red_score
    global green_score
    global mode
    mode = "slither"
    paused = False
    gameExit = False
    gameOver = False
    red_lead_x = display_width / 4 * 3
    red_lead_y = display_height / 2
    red_lead_x_change = 0
    red_lead_y_change = 10
    green_lead_x = display_width / 4
    green_lead_y = display_height / 2
    green_lead_x_change = 0
    green_lead_y_change = 10
    rand_apple1_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple1_y = random.randrange(0, display_height - block_size, block_size)
    rand_apple2_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple2_y = random.randrange(0, display_height - block_size, block_size)
    rand_apple3_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple3_y = random.randrange(0, display_height - block_size, block_size)
    red_snakelist = []
    red_snakelength = 20
    red_score = 0
    green_snakelist = []
    green_snakelength = 20
    green_score = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not paused:
                        red_lead_x_change = -block_size
                        red_lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if not paused:
                        red_lead_x_change = block_size
                        red_lead_y_change = 0
                elif event.key == pygame.K_UP:
                    if not paused:
                        red_lead_y_change = -block_size
                        red_lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    if not paused:
                        red_lead_y_change = block_size
                        red_lead_x_change = 0
                if event.key == pygame.K_a:
                    if not paused:
                        green_lead_x_change = -block_size
                        green_lead_y_change = 0
                elif event.key == pygame.K_d:
                    if not paused:
                        green_lead_x_change = block_size
                        green_lead_y_change = 0
                elif event.key == pygame.K_w:
                    if not paused:
                        green_lead_y_change = -block_size
                        green_lead_x_change = 0
                elif event.key == pygame.K_s:
                    if not paused:
                        green_lead_y_change = block_size
                        green_lead_x_change = 0
                if event.key == pygame.K_SPACE:
                    if paused:
                        red_lead_x_change = red_lead_x_change_stored
                        red_lead_y_change = red_lead_y_change_stored
                        green_lead_x_change = green_lead_x_change_stored
                        green_lead_y_change = green_lead_y_change_stored
                        paused = False
                    else:
                        red_lead_x_change_stored = red_lead_x_change
                        red_lead_y_change_stored = red_lead_y_change
                        green_lead_x_change_stored = green_lead_x_change
                        green_lead_y_change_stored = green_lead_y_change
                        red_lead_x_change = 0
                        red_lead_y_change = 0
                        green_lead_x_change = 0
                        green_lead_y_change = 0
                        paused = True
                    
        if red_lead_x >= display_width or red_lead_x < 0 or red_lead_y >= display_height or red_lead_y < 0:
            green_wins()
        if green_lead_x >= display_width or green_lead_x < 0 or green_lead_y >= display_height or green_lead_y < 0:
            red_wins()
        red_lead_x += red_lead_x_change
        red_lead_y += red_lead_y_change
        green_lead_x += green_lead_x_change
        green_lead_y += green_lead_y_change
        gameDisplay.fill(l_blue)
        message(str(green_score), white, [10, 10], f3)
        message(str(red_score), white, [750, 10], f3)
        pygame.draw.rect(gameDisplay, red, [rand_apple1_x, rand_apple1_y, block_size, block_size])
        pygame.draw.rect(gameDisplay, red, [rand_apple2_x, rand_apple2_y, block_size, block_size])
        pygame.draw.rect(gameDisplay, red, [rand_apple3_x, rand_apple3_y, block_size, block_size])
        red_snakehead = []
        red_snakehead.append(red_lead_x)
        red_snakehead.append(red_lead_y)
        green_snakehead = []
        green_snakehead.append(green_lead_x)
        green_snakehead.append(green_lead_y)
        if not paused:
            red_snakelist.append(red_snakehead)
            green_snakelist.append(green_snakehead)
            if len(red_snakelist) > red_snakelength:
                del red_snakelist[0]
            if len(green_snakelist) > green_snakelength:
                del green_snakelist[0]
        for eachsegment in green_snakelist[:-1]:
            if eachsegment == red_snakehead:
                green_wins()
        for eachsegment in red_snakelist[:-1]:
            if eachsegment == green_snakehead:
                red_wins()
        snake(block_size, red_snakelist, red)
        snake(block_size, green_snakelist, green)
        pygame.display.update()
        if red_lead_x == rand_apple1_x and red_lead_y == rand_apple1_y:
            rand_apple1_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple1_y = random.randrange(0, display_height - block_size, block_size)
            red_snakelength += 5
            red_score += 1
        elif red_lead_x == rand_apple2_x and red_lead_y == rand_apple2_y:
            rand_apple2_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple2_y = random.randrange(0, display_height - block_size, block_size)
            red_snakelength += 5
            red_score += 1
        elif red_lead_x == rand_apple3_x and red_lead_y == rand_apple3_y:
            rand_apple3_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple3_y = random.randrange(0, display_height - block_size, block_size)
            red_snakelength += 5
            red_score += 1
        if green_lead_x == rand_apple1_x and green_lead_y == rand_apple1_y:
            rand_apple1_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple1_y = random.randrange(0, display_height - block_size, block_size)
            green_snakelength += 5
            green_score += 1
        elif green_lead_x == rand_apple2_x and green_lead_y == rand_apple2_y:
            rand_apple2_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple2_y = random.randrange(0, display_height - block_size, block_size)
            green_snakelength += 5
            green_score += 1
        elif green_lead_x == rand_apple3_x and green_lead_y == rand_apple3_y:
            rand_apple3_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple3_y = random.randrange(0, display_height - block_size, block_size)
            green_snakelength += 5
            green_score += 1
        clock.tick(30)


    pygame.quit()
    quit()

def mode_splix():

    global red_score
    global green_score
    global mode
    mode = "splix"
    paused = False
    gameExit = False
    red_lead_x = display_width / 4 * 3
    red_lead_y = display_height / 2
    red_lead_x_change = 0
    red_lead_y_change = 10
    green_lead_x = display_width / 4
    green_lead_y = display_height / 2
    green_lead_x_change = 0
    green_lead_y_change = 10
    rand_apple1_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple1_y = random.randrange(0, display_height - block_size, block_size)
    rand_apple2_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple2_y = random.randrange(0, display_height - block_size, block_size)
    rand_apple3_x = random.randrange(0, display_width - block_size, block_size)
    rand_apple3_y = random.randrange(0, display_height - block_size, block_size)
    red_snakelist = []
    red_snakelength = 20
    red_score = 0
    green_snakelist = []
    green_snakelength = 20
    green_score = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not paused:
                        red_lead_x_change = -block_size
                        red_lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    if not paused:
                        red_lead_x_change = block_size
                        red_lead_y_change = 0
                elif event.key == pygame.K_UP:
                    if not paused:
                        red_lead_y_change = -block_size
                        red_lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    if not paused:
                        red_lead_y_change = block_size
                        red_lead_x_change = 0
                if event.key == pygame.K_a:
                    if not paused:
                        green_lead_x_change = -block_size
                        green_lead_y_change = 0
                elif event.key == pygame.K_d:
                    if not paused:
                        green_lead_x_change = block_size
                        green_lead_y_change = 0
                elif event.key == pygame.K_w:
                    if not paused:
                        green_lead_y_change = -block_size
                        green_lead_x_change = 0
                elif event.key == pygame.K_s:
                    if not paused:
                        green_lead_y_change = block_size
                        green_lead_x_change = 0
                if event.key == pygame.K_SPACE:
                    if paused:
                        red_lead_x_change = red_lead_x_change_stored
                        red_lead_y_change = red_lead_y_change_stored
                        green_lead_x_change = green_lead_x_change_stored
                        green_lead_y_change = green_lead_y_change_stored
                        paused = False
                    else:
                        red_lead_x_change_stored = red_lead_x_change
                        red_lead_y_change_stored = red_lead_y_change
                        green_lead_x_change_stored = green_lead_x_change
                        green_lead_y_change_stored = green_lead_y_change
                        red_lead_x_change = 0
                        red_lead_y_change = 0
                        green_lead_x_change = 0
                        green_lead_y_change = 0
                        paused = True
                    
        if red_lead_x >= display_width or red_lead_x < 0 or red_lead_y >= display_height or red_lead_y < 0:
            green_wins()
        if green_lead_x >= display_width or green_lead_x < 0 or green_lead_y >= display_height or green_lead_y < 0:
            red_wins()
        red_lead_x += red_lead_x_change
        red_lead_y += red_lead_y_change
        green_lead_x += green_lead_x_change
        green_lead_y += green_lead_y_change
        gameDisplay.fill(l_blue)
        message(str(green_score), white, [10, 10], f3)
        message(str(red_score), white, [750, 10], f3)
        pygame.draw.rect(gameDisplay, red, [rand_apple1_x, rand_apple1_y, block_size, block_size])
        pygame.draw.rect(gameDisplay, red, [rand_apple2_x, rand_apple2_y, block_size, block_size])
        pygame.draw.rect(gameDisplay, red, [rand_apple3_x, rand_apple3_y, block_size, block_size])
        red_snakehead = []
        red_snakehead.append(red_lead_x)
        red_snakehead.append(red_lead_y)
        green_snakehead = []
        green_snakehead.append(green_lead_x)
        green_snakehead.append(green_lead_y)
        if not paused:
            red_snakelist.append(red_snakehead)
            green_snakelist.append(green_snakehead)
            if len(red_snakelist) > red_snakelength:
                del red_snakelist[0]
            if len(green_snakelist) > green_snakelength:
                del green_snakelist[0]
        for eachsegment in green_snakelist[:-1]:
            if eachsegment == green_snakehead:
                red_wins()
        for eachsegment in red_snakelist[:-1]:
            if eachsegment == red_snakehead:
                green_wins()
        for eachsegment in red_snakelist[:-1]:
            if eachsegment == green_snakehead:
                green_wins()
        for eachsegment in green_snakelist[:-1]:
            if eachsegment == red_snakehead:
                red_wins()
        snake(block_size, red_snakelist, red)
        snake(block_size, green_snakelist, green)
        pygame.display.update()
        if red_lead_x == rand_apple1_x and red_lead_y == rand_apple1_y:
            rand_apple1_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple1_y = random.randrange(0, display_height - block_size, block_size)
            red_snakelength += 5
            red_score += 1
        elif red_lead_x == rand_apple2_x and red_lead_y == rand_apple2_y:
            rand_apple2_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple2_y = random.randrange(0, display_height - block_size, block_size)
            red_snakelength += 5
            red_score += 1
        elif red_lead_x == rand_apple3_x and red_lead_y == rand_apple3_y:
            rand_apple3_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple3_y = random.randrange(0, display_height - block_size, block_size)
            red_snakelength += 5
            red_score += 1
        if green_lead_x == rand_apple1_x and green_lead_y == rand_apple1_y:
            rand_apple1_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple1_y = random.randrange(0, display_height - block_size, block_size)
            green_snakelength += 5
            green_score += 1
        elif green_lead_x == rand_apple2_x and green_lead_y == rand_apple2_y:
            rand_apple2_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple2_y = random.randrange(0, display_height - block_size, block_size)
            green_snakelength += 5
            green_score += 1
        elif green_lead_x == rand_apple3_x and green_lead_y == rand_apple3_y:
            rand_apple3_x = random.randrange(0, display_width - block_size, block_size)
            rand_apple3_y = random.randrange(0, display_height - block_size, block_size)
            green_snakelength += 5
            green_score += 1
        clock.tick(30)


    pygame.quit()
    quit()

def mainMenu():
    selected = 1
    gameDisplay.fill(white)
    message("SNAKE", green, [150, 40], f5)
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

def p2_mode_select():
    selected = 1
    gameDisplay.fill(white)
    message("SELECT GAMEMODE", green, [80, 80], f3)
    message("Slither", yellow, [340, 280], f2)
    message("Splix", black, [355, 380], f2)
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
                        message("Slither", yellow, [340, 280], f2)
                        message("Splix", black, [355, 380], f2)
                        pygame.display.update()
                    elif selected == 3:
                        selected = 2
                        message("Splix", yellow, [355, 380], f2)
                        message("Back", black, [355, 480], f2)
                        pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    if selected == 1:
                        selected = 2
                        message("Splix", yellow, [355, 380], f2)
                        message("Slither", black, [340, 280], f2)
                        pygame.display.update()
                    elif selected == 2:
                        selected = 3
                        message("Back", yellow, [355, 480], f2)
                        message("Splix", black, [355, 380], f2)
                        pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    if selected == 1:
                        mode_slither()
                    elif selected == 2:
                        mode_splix()
                    elif selected == 3:
                        mainMenu()

def p1_mode_select():
    selected = 1
    gameDisplay.fill(white)
    message("SELECT GAMEMODE", green, [80, 80], f3)
    message("Classic", yellow, [330, 280], f2)
    message("Sandbox", black, [315, 380], f2)
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
                        message("Sandbox", black, [315, 380], f2)
                        pygame.display.update()
                    elif selected == 3:
                        selected = 2
                        message("Sandbox", yellow, [315, 380], f2)
                        message("Back", black, [350, 480], f2)
                        pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    if selected == 1:
                        selected = 2
                        message("Sandbox", yellow, [315, 380], f2)
                        message("Classic", black, [330, 280], f2)
                        pygame.display.update()
                    elif selected == 2:
                        selected = 3
                        message("Back", yellow, [350, 480], f2)
                        message("Sandbox", black, [315, 380], f2)
                        pygame.display.update()
                elif event.key == pygame.K_SPACE:
                    if selected == 1:
                        mode_classic()
                    elif selected == 2:
                        mode_sandbox()
                    elif selected == 3:
                        mainMenu()
                        
    pygame.quit()
    quit()

def red_wins():
    Exit = False
    lost = True
    while not Exit:
        gameDisplay.fill(l_blue)
        selected = 1
        message("RED WINS!", red, [230, 100], f3)
        message("Red score:   " + str(red_score) + "                Green score:   " + str(green_score), red, [130, 250], f2)
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
                            if mode == "slither":
                                mode_slither()
                            else:
                                mode_splix()
                        else:
                            mainMenu()
    pygame.quit()
    quit()
    
def green_wins():
    Exit = False
    lost = True
    while not Exit:
        gameDisplay.fill(l_blue)
        lost = True
        selected = 1
        message("GREEN WINS!", red, [210, 100], f3)
        message("Red score:   " + str(red_score) + "                Green score:   " + str(green_score), red, [100, 250], f2)
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
                            if mode == "slither":
                                mode_slither()
                            else:
                                mode_splix()
                        else:
                            mainMenu()
    pygame.quit()
    quit()

mainMenu()

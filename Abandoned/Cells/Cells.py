import pygame
import os.path
from decimal import Decimal

pygame.init()
pygame.font.init()
game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cells")
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
f5 = pygame.font.Font(None, 200)
f4 = pygame.font.Font(None, 130)
f3 = pygame.font.Font(None, 90)
f2 = pygame.font.Font(None, 50)
f1 = pygame.font.Font(None, 25)
if not os.path.isfile("cells.txt"):
    m = open("cells.txt", "w")
    m.write("1")
    m.close()
m = open("cells.txt", "r")
try:
    cells = int(m.read())
except:
    print("You broke the game, back to 1!")
    cells = 0.1
    div_speed = 0.1
m.close

def message(msg, colour, place, size, center):
    if size == f1:
        screen_text = f1.render(msg, True, colour, place)
    elif size == f2:
        screen_text = f2.render(msg, True, colour, place)
    elif size == f3:
        screen_text = f3.render(msg, True, colour, place)
    elif size == f4:
        screen_text = f4.render(msg, True, colour, place)
    else:
        screen_text = f5.render(msg, True, colour, place)
    if center:
        place[0] = 400 - screen_text.get_rect().width / 2
    pygame.draw.rect(game_display, white, [0, place[1], 800, screen_text.get_rect().height])
    game_display.blit(screen_text, place)
    
def quit_game():
    m = open("cells.txt", "w")
    m.write(str(cells))
    m.close
    pygame.quit()
    quit()

def game_loop():
    global cells
    global div_speed
    game_exit = False
    game_display.fill(white)
    message("CELLS", green, [0, 20], f5, True)
    message(str(cells), green, [0, 200], f3, True)
    pygame.display.update()
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        cells *= 2
        display_cells = "%E" % Decimal(str(cells))
        message(str(display_cells), green, [0, 200], f3, True)
        pygame.display.update()
        clock.tick(div_speed)
        
    quit_game()
    
game_loop()

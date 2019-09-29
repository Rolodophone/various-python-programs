import pygame, sys, math
from pygame.locals import *

global WINDOWHEIGHT

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
GRIDWIDTH = 80
GRIDHEIGHT = 50
SQUARESIZE = 20
assert WINDOWWIDTH % SQUARESIZE == 0 and WINDOWHEIGHT % SQUARESIZE == 0, "Window height and width must be divisible by the square size"

DGREY    = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
LBLUE    = (  0, 255, 255)
GREY     = (160, 160, 160)
DGREEN   = (  0, 100,   0)
LGREY    = (200, 200, 200)
BROWN    = (165,  42,  42)

BGCOLOUR     = LBLUE
BUTTONIN     = GREY
BUTTONOUT    = DGREY
TITLECOLOUR  = DGREEN
OPTIONCOLOUR = BLACK

def main():
    global DISPLAYSURF, TITLEFONT, SUBTITLEFONT, BUTTONFONT, CLOCK
    
    pygame.init()
    pygame.font.init()
    CLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    TITLEFONT    = pygame.font.Font(None, 120)
    SUBTITLEFONT = pygame.font.Font(None, 100)
    BUTTONFONT   = pygame.font.Font(None, 50)
    TEXTFONT     = pygame.font.Font(None, 25)
    
    pygame.display.set_caption("Get To The Flag")

    menu(True, "GET TO THE FLAG", [["Play campaign", ["print('Coming soon...')"]], ["Load level", ["print('Coming soon...')"]], ["Create level", ["create()"]], ["Quit", ["pygame.quit()", "sys.exit()"]]])

def message(msg, colour, place, font):
    if place[0] == None:
        place[0] = WINDOWWIDTH / 2 - font.size(msg)[0] / 2
    if place[1] == None:
        place[1] = WINDOWHEIGHT / 2 - font.size(msg)[1] / 2
    screen_text = font.render(msg, True, colour, place)
    DISPLAYSURF.blit(screen_text, place)

def menu(isMain, title, options):
    global WINDOWHEIGHT, DISPLAYSURF, TITLEFONT, SUBTITLEFONT, BUTTONFONT, CLOCK, inMenu

    BUTTONMARGINS = (10, 5)

    inMenu = True
    optionSpace = 0
    optionHeight = 0
    optionWidth = 0
    optionMargin = 0
    titleSize = 0
    buttonOut = 0
    buttonIn = 0
    buttonTop = 0
    buttonNum = None
    optionHeights = []
    optionWidths = []
    buttonList = []
    DISPLAYSURF.fill(BGCOLOUR)
    if isMain:
        message(title, TITLECOLOUR, [None, 30], TITLEFONT)
        titleSize = TITLEFONT.size(title)[1] + 30
        optionSpace = WINDOWHEIGHT - titleSize
    else:
        message(title, TITLECOLOUR, [None, 20], SUBTITLEFONT)
        titleSize = SUBTITLEFONT.size(title)[1] + 20
        optionSpace = WINDOWHEIGHT - titleSize
    for option in options:
        optionHeights.append(BUTTONFONT.size(option[0])[1])
        optionWidths.append(BUTTONFONT.size(option[0])[0])
    optionHeight = max(optionHeights)
    optionWidth = max(optionWidths)
    optionMargin = -(2 * sum(BUTTONMARGINS) * len(options) + len(options) * optionHeight + titleSize - WINDOWHEIGHT) / (len(options) + 2)
    buttonOut = WINDOWWIDTH / 2 - (optionWidth / 2 + sum(BUTTONMARGINS))
    buttonIn = buttonOut + BUTTONMARGINS[1]
    buttonTop = titleSize + optionMargin * 2
    for option in options:
        pygame.draw.rect(DISPLAYSURF, BUTTONOUT, (buttonOut, buttonTop, optionWidth + sum(BUTTONMARGINS) * 2, optionHeight + sum(BUTTONMARGINS) * 2))
        buttonList.append((buttonOut, buttonOut + optionWidth + sum(BUTTONMARGINS) * 2, buttonTop, buttonTop + optionHeight + sum(BUTTONMARGINS) * 2))
        buttonTop += BUTTONMARGINS[1]
        pygame.draw.rect(DISPLAYSURF, BUTTONIN, (buttonIn, buttonTop, optionWidth + BUTTONMARGINS[0] * 2, optionHeight + BUTTONMARGINS[0] * 2))
        buttonTop += BUTTONMARGINS[0]
        message(option[0], OPTIONCOLOUR, [None,  buttonTop], BUTTONFONT)
        buttonTop += optionHeight + sum(BUTTONMARGINS) + optionMargin
    while inMenu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    buttonNum = None
                    if event.pos[0] > buttonList[0][0] and event.pos[0] < buttonList[0][1]:
                        i = 0
                        for button in buttonList:
                            if event.pos[1] > button[2] and event.pos[1] < button[3]:
                                buttonNum = i
                                buttonTop = buttonList[buttonNum][2]
                                pygame.draw.rect(DISPLAYSURF, BUTTONIN, (buttonOut, buttonTop, optionWidth + sum(BUTTONMARGINS) * 2, optionHeight + sum(BUTTONMARGINS) * 2))
                                buttonTop += BUTTONMARGINS[1]
                                pygame.draw.rect(DISPLAYSURF, BUTTONOUT, (buttonIn, buttonTop, optionWidth + BUTTONMARGINS[0] * 2, optionHeight + BUTTONMARGINS[0] * 2))
                                buttonTop += BUTTONMARGINS[0]
                                message(options[buttonNum][0], OPTIONCOLOUR, [None,  buttonTop], BUTTONFONT)
                                break
                            i += 1
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if buttonNum != None:
                        if event.pos[0] > buttonList[0][0] and event.pos[0] < buttonList[0][1] and event.pos[1] > buttonList[buttonNum][2] and event.pos[1] < buttonList[buttonNum][3]:
                            for code in options[buttonNum][1]:
                                exec(code)
                        if inMenu:
                            buttonTop = buttonList[buttonNum][2]
                            pygame.draw.rect(DISPLAYSURF, BUTTONOUT, (buttonOut, buttonTop, optionWidth + sum(BUTTONMARGINS) * 2, optionHeight + sum(BUTTONMARGINS) * 2))
                            buttonTop += BUTTONMARGINS[1]
                            pygame.draw.rect(DISPLAYSURF, BUTTONIN, (buttonIn, buttonTop, optionWidth + BUTTONMARGINS[0] * 2, optionHeight + BUTTONMARGINS[0] * 2))
                            buttonTop += BUTTONMARGINS[0]
                            message(options[buttonNum][0], OPTIONCOLOUR, [None,  buttonTop], BUTTONFONT)
        pygame.display.update()
        CLOCK.tick(FPS)

def create():
    global inMenu, lastPos, elementList, squareList
    
    inMenu = False
    inCreate = True
    selectedElement = 0
    lastPos = (0, 0)
    mousex = pygame.mouse.get_pos()[0]
    mousey = pygame.mouse.get_pos()[1]
    #                           Still  Moving
    #              Blank  Wall  death  death   Key   Door  Checkpoint Start Finish   Coin
    elementList = [LGREY, BLACK, RED,   RED,  WHITE, BROWN,  GREEN,   BLUE, DGREEN, YELLOW]
    squareList = []
    for x in range(40):
        squareList.append([])
        for y in range(25):
            squareList[x].append(0)
    DISPLAYSURF.fill(BGCOLOUR)
    pygame.draw.rect(DISPLAYSURF, DGREY, (0, 0, WINDOWWIDTH, WINDOWHEIGHT - 100))
    for y in range(int((WINDOWHEIGHT - 100) / SQUARESIZE)):
        squareList.append([])
        for x in range(int(WINDOWWIDTH / SQUARESIZE)):
            squareList[y].append(0)
            pygame.draw.rect(DISPLAYSURF, LGREY, (x * SQUARESIZE + 1, y * SQUARESIZE + 1, SQUARESIZE - 2, SQUARESIZE - 2))
    while inCreate:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == KEYDOWN:
                if event.key == K_0:
                    selectedElement = 0
                elif event.key == K_1:
                    selectedElement = 1
                elif event.key == K_2:
                    selectedElement = 2
                elif event.key == K_3:
                    selectedElement = 3
                elif event.key == K_4:
                    selectedElement = 4
                elif event.key == K_5:
                    selectedElement = 5
                elif event.key == K_6:
                    selectedElement = 6
                elif event.key == K_7:
                    selectedElement = 7
                elif event.key == K_8:
                    selectedElement = 8
                elif event.key == K_9:
                    selectedElement = 9
        drawElement(getCurrentSquare(mousex, mousey), [elementList[selectedElement], 100])
        pygame.display.update()
        CLOCK.tick(FPS)

def drawElement(pos, colour):
    global lastPos, elementList, squareList
    
    if pos != lastPos and pos[1] < 25:
        realLastPos = [lastPos[0] * SQUARESIZE + 1, lastPos[1] * SQUARESIZE + 1, SQUARESIZE - 2, SQUARESIZE - 2]
        pygame.draw.rect(DISPLAYSURF, elementList[squareList[pos[0]][pos[1]]], (realLastPos[0], realLastPos[1], SQUARESIZE - 2, SQUARESIZE - 2))
        realPos = [pos[0] * SQUARESIZE + 1, pos[1] * SQUARESIZE + 1, SQUARESIZE - 2, SQUARESIZE - 2]
        s = pygame.Surface((SQUARESIZE - 2,SQUARESIZE - 2))
        s.set_alpha(colour[1])
        darkColour = []
        for val in colour[0]:
            darkColour.append(val - val / 3)
        s.fill(darkColour)
        DISPLAYSURF.blit(s, realPos)
        lastPos = pos

def getCurrentSquare(x, y):
    return math.floor(x / SQUARESIZE), math.floor(y / SQUARESIZE)
    
main()

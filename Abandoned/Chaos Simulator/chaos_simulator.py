import pygame, sys, gui
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

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

BGCOLOUR = LBLUE
TITLECOLOUR = DGREEN
OPTIONCOLOUR = BLACK
BUTTONIN = GREY
BUTTONOUT = DGREY

def main():
    global DISPLAYSURF, TITLEFONT, SUBTITLEFONT, BUTTONFONT, CLOCK
    
    pygame.init()
    pygame.font.init()
    CLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    TITLEFONT    = pygame.font.Font(None, 110)
    SUBTITLEFONT = pygame.font.Font(None, 100)
    BUTTONFONT   = pygame.font.Font(None, 90)
    TEXTFONT     = pygame.font.Font(None, 25)
    
    pygame.display.set_caption("Chaos Simulator")

    exec(gui.menu(DISPLAYSURF, (TITLEFONT, BUTTONFONT), "CHAOS SIMULATOR", [["Start", ["start_menu()"]], ["Quit", ["pygame.quit()", "sys.exit()"]]]))

def start_menu():
    exec(gui.menu(DISPLAYSURF, (TITLEFONT, BUTTONFONT), "Chaos", [["Start", ["start()"]], ["Settings", ["settings()"]]]))

def start():
    global dotColour, dotSize, dotNumber, dotList
    
    speed = 10

def settings():
    #global dotColour, dotSize, dotNumber, dotList
   exec(gui.menu(DISPLAYSURF, (TITLEFONT, BUTTONFONT), "fa", ["start", ["start()"]]))

main()

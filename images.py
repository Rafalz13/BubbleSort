import pygame,os

#butons
BUT_L = pygame.image.load(os.path.join('game', 'button_L.png'))
BUT_LLIGHT = pygame.image.load(os.path.join('game', 'button_L_light.png'))
BUT_R = pygame.image.load(os.path.join('game', 'button_R.png'))
BUT_RLIGHT = pygame.image.load(os.path.join('game', 'button_R_light.png'))
BUT_O = pygame.image.load(os.path.join('game', 'button_O.png'))
BUT_OLIGHT = pygame.image.load(os.path.join('game', 'button_O_light.png'))
BUT_D = pygame.image.load(os.path.join('game', 'button_D.png'))
BUT_DLIGHT = pygame.image.load(os.path.join('game', 'button_D_light.png'))
BUT_LIST1 = [BUT_L, BUT_R, BUT_O, BUT_D]
BUT_LIST2 = [ BUT_LLIGHT, BUT_RLIGHT, BUT_OLIGHT, BUT_DLIGHT]

FRAME = pygame.image.load(os.path.join('game', 'frame.png'))
FRAME = pygame.transform.scale(FRAME, (170,102))
FRAME2 = pygame.image.load(os.path.join('game', 'frame_2.png'))

START = pygame.image.load(os.path.join('game', 'start.png'))

SIZESCREEN = WIDTH, HEIGHT = 1530, 870
BACKGR = pygame.image.load(os.path.join('game','chest.png'))

GREEN = pygame.color.THECOLORS['darkgreen']
GREY = pygame.color.THECOLORS['grey10']
RED = pygame.color.THECOLORS['red']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
WHITE = pygame.color.THECOLORS['white']


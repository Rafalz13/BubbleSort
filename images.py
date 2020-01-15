import pygame,os
#litery
LET_A = pygame.image.load(os.path.join('game', 'letter_A.png'))
LET_A = pygame.transform.scale(LET_A, (80,95))
LET_B = pygame.image.load(os.path.join('game', 'letter_B.png'))
LET_B = pygame.transform.scale(LET_B, (80,95))
LET_C = pygame.image.load(os.path.join('game', 'letter_C.png'))
LET_C = pygame.transform.scale(LET_C, (80,95))
LET_D = pygame.image.load(os.path.join('game', 'letter_D.png'))
LET_D = pygame.transform.scale(LET_D, (80,95))
LET_E = pygame.image.load(os.path.join('game', 'letter_E.png'))
LET_E = pygame.transform.scale(LET_E, (80,95))
LET_F = pygame.image.load(os.path.join('game', 'letter_F.png'))
LET_F = pygame.transform.scale(LET_F, (80,95))
LET_G = pygame.image.load(os.path.join('game', 'letter_G.png'))
LET_G = pygame.transform.scale(LET_G, (80,95))
LET_H = pygame.image.load(os.path.join('game', 'letter_H.png'))
LET_H = pygame.transform.scale(LET_H, (80,95))
LET_X = pygame.image.load(os.path.join('game', 'letter_X.png'))
LET_X = pygame.transform.scale(LET_X, (80,95))
LET_J = pygame.image.load(os.path.join('game', 'letter_J.png'))
LET_J = pygame.transform.scale(LET_J, (80,95))
LET_K = pygame.image.load(os.path.join('game', 'letter_K.png'))
LET_K = pygame.transform.scale(LET_K, (80,95))
LET_P = pygame.image.load(os.path.join('game', 'letter_P.png'))
LET_P = pygame.transform.scale(LET_P, (80,95))
LET_N = pygame.image.load(os.path.join('game', 'letter_N.png'))
LET_N = pygame.transform.scale(LET_N, (80,95))
LET_O = pygame.image.load(os.path.join('game', 'letter_O.png'))
LET_O = pygame.transform.scale(LET_O, (80,95))
LET_LIST = [LET_C,LET_K, LET_A, LET_N, LET_E, LET_O, LET_G, LET_H, LET_X,
            LET_J, LET_B, LET_P, LET_D, LET_F]
LET_LIST_SORTED = [(LET_A,'A'),(LET_B,'B'),(LET_C,'C'), (LET_D,'D'), (LET_E,'E'), (LET_F,'F'), (LET_G,'G'), (LET_H,'H'), (LET_J,'J'),
                   (LET_K,'K'), (LET_N,'N'), (LET_O,'O'), (LET_P,'P'), (LET_X,'X')]

#przyciski
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


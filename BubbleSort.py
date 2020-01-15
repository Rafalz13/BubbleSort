
import pygame,sys,random,os
import images as im
import copy

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Gra bąbelkowa ')
clock = pygame.time.Clock()

class Pillar(pygame.sprite.Sprite):
    def __init__(self,h,x,color):
        self.h = h
        self.x = x
        self.color = color
        screen = pygame.display.set_mode((1280,720))
        text = Text("cos",im.RED,20)

    def draw(self):
        y = 650
        rect = pygame.Rect(self.x, y, 30, -self.h)
        #screen, color,rect
        pygame.draw.rect(screen, self.color, rect)

    def sort(self,list,sorted):
        list_org = copy.deepcopy(list)
        if list[i].h > list[i + 1].h:
            list[i + 1].h, list[i].h = list[i].h, list[i + 1].h

        elif list[i].h < list[i + 1].h:
            Game.draw_text(None, " Zła próba :( ", im.WHITE, 90)
            pygame.time.delay(900)
            list = self.start_list(list,list_org)
            pygame.display.flip()
            print("Zmiana")

        list[i-1].color  = im.GREY
        same = 1

        #sprawdzenie czy jest gotowa
        for j in range(len(list1)-1):
            if list[j].h == sorted[j].h:
                #list[j].color = im.LIGHTBLUE
                same +=1
                print("same = ",same)

            else:
                print("not")

            if same == 12:
                print("*"*30)
                Game.draw_text(None, "Sortowanie skończone !! ", im.LIGHTBLUE, 90)
                sys.exit(0)

    def next(self,list):
        list[i].color = im.RED
        list[i+1].color = im.RED

##check
    def start_list(self,list1,list2):
        for i in range(len(list1)-1):
            list1[i].h = list2[i].h
        return list1

class Button(pygame.sprite.Sprite):
    def __init__(self, file_image):
        self.image = file_image
        self.rect = self.image.get_rect()

    def draw(self,surface):
        x=150
        for y in range (3):
            surface.blit(im.BUT_LIST1[y], (x, 20))
            x += 150

    def draw_active(self,surface,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                surface.blit(im.BUT_LIST2[1], (280, 0))

            if event.key == pygame.K_SPACE:
                surface.blit(im.BUT_LIST2[2], (430, 0))

            if event.key == pygame.K_LEFT:
                print("Aktywna spacja")
                surface.blit(im.BUT_LIST2[0], (130, 0))


class Game(pygame.sprite.Sprite):
    def __init__(self,list_of_pill):
        self.screen = pygame.display.set_mode((1280, 720))
        self.pillars = list_of_pill
        self.button = Button(im.BUT_L)

    def update(self):
        self.button.draw(self.screen)
        pillar.draw()
        button.draw_active(screen,event)
        pillar.next(self.pillars)


    def draw_text(self,text,colour,size):
        text = Text(text,colour,size)
        text.rect.center = screen.get_rect().center
        #game.screen.fill((150, 100, 60))
        text.draw(screen)
        pygame.display.flip()
        pygame.time.delay(800)

class Text(pygame.sprite.Sprite):
    def __init__(self, text, text_colour, size):
        self.text = text
        self.text_colour = text_colour
        self.size = size
        self.font = pygame.font.SysFont(None, self.size)
        self.image = self.font.render(self.text, 1, self.text_colour)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#kolor

#konkretyzacja
text = Text("Koniec gry", im.GREEN, 100)
text.rect.center = screen.get_rect().center
button = Button(im.BUT_R)

screen.blit(im.START, (0,0))

list = []
#tworzenie słpuków
for i in range(400,850,40):
    r = random.randint(20, 450)
    pillar = Pillar(r,i,im.GREY)
    print("poz ",i,"  wysokosc ",r)
    list.append(pillar)

#sortowanie automatyczne
q = True
list1 = copy.deepcopy(list)
while q == True:
    q = False
    for i in range(len(list1)-1):
        if list1[i].h > list1[i + 1].h:
            list1[i + 1].h, list1[i].h = list1[i].h, list1[i + 1].h
            q = True


game = Game(list)
running = True
#Głowna petla programu :
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

 #przechodzenie i zmiana
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pillar.next(list)
                button.draw_active(screen,event)

            if event.key == pygame.K_SPACE:
                pillar.sort(list,list1)
                button.draw_active(screen,event)

            if event.key == pygame.K_LEFT:
                i = 0
            if event.key == pygame.K_s:
                game.screen.fill((70, 210, 120))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                i += 1
                if i == 1:
                    pass
                else:
                    list[i-1].color = im.GREY
                if i == len(list)-1:
                    list[i].color = im.GREY
                    i = 0
    screen.blit(im.START, (im.WIDTH /2 - 300 ,im.HEIGHT /2 -100))

    game.screen.fill((170, 210, 120))
    game.update()
    for j in list:
        j.draw()
    pygame.display.flip()


game.screen.fill((200,200,160))
text.draw(screen)
pygame.display.flip()
pygame.time.delay(400)
pygame.quit()

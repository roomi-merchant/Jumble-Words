import pygame
from pygame.locals import *
import time

class W(pygame.sprite.Sprite):
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("resources/w.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class A(pygame.sprite.Sprite):
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("resources/a1.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class S(pygame.sprite.Sprite):
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("resources/s.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class D(pygame.sprite.Sprite):
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("resources/d.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class F(pygame.sprite.Sprite):
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("resources/f.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class G(pygame.sprite.Sprite):
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load("resources/g.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

    def kill(self):
        pygame.sprite.Sprite.kill(self)

pygame.init()

screen = pygame.display.set_mode((1150,800))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
green = (0,128,0)
light_green = (0, 255, 0)
gray = (128,128,128)
yellow = (255,255,0)
light_yellow = (200, 200, 0)
red = (255,0,0)
light_red = (200, 0, 0)

x,y = 30,90

pygame.display.set_caption("Jumble Words")

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def msg(text, fontsize, center_x, center_y, color):
    largeText = pygame.font.Font('freesansbold.ttf', fontsize)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((center_x), (center_y))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def intro():
    menu = True
    menu_image = pygame.image.load("resources/menu.jpg")
    screen.blit(menu_image, (0,0))
    pygame.display.update()
    while menu:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 310 > mouse[0] > 110 and 560 > mouse[1] > 460:
            if click[0] == 1:
                menu = False
                pause = False
                run()
            pygame.draw.rect(screen, green, (110, 460, 200, 100))
            msg("PLAY", 50, 200, 515, black)
        else:
            pygame.draw.rect(screen, gray, (110, 460, 200, 100))
            msg("PLAY", 50, 200, 515, black)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        clock.tick(100)
    
def run():
    global clock, screen, red, green, gray, x, y

    words = ["dags","daws","dada","fads","fags","gads","swag","wads","wags","wafd",
         "add","ads","ags","ass","dag","dad","das","daw","fad","fag","fas","gad","gag","gas","sad","sag","saw","wad","wag","was",
         "ad","ag","as","aw","da","fa"]
    
    gameExit = False
    score = 0

##    w = W()
##    a = A()
##    s = S()
##    d = D()
##    f = F()
##    g = G()

    all_sprites_list = pygame.sprite.Group()
    background = pygame.image.load("resources/background.png")

    letters = []
    current=  ""
    check_word = []
    correct_words = []

    while not gameExit:
        msg("SCORE "+str(score), 30, 500, 20, red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    x,y = 30,90
                    intro()
                elif event.key == pygame.K_w:
                    w = W()
                    all_sprites_list.add(w)
                    letters.append(w)
                    current = current + "w"
                    w.rect.x,w.rect.y = x,y+20
                    x += 45
                elif event.key == pygame.K_a:
                    a = A()
                    all_sprites_list.add(a)
                    letters.append(a)
                    current = current + "a"
                    a.rect.x,a.rect.y = x,y
                    x += 45
                elif event.key == pygame.K_s:
                    s = S()
                    all_sprites_list.add(s)
                    letters.append(s)
                    current = current + "s"
                    s.rect.x,s.rect.y = x,y
                    x += 45
                elif event.key == pygame.K_d:
                    d = D()
                    all_sprites_list.add(d)
                    letters.append(d)
                    current = current + "d"
                    d.rect.x,d.rect.y = x,y
                    x += 45
                elif event.key == pygame.K_f:
                    f = F()
                    all_sprites_list.add(f)
                    letters.append(f)
                    current = current + "f"
                    f.rect.x,f.rect.y = x,y
                    x += 45
                elif event.key == pygame.K_g:
                    g = G()
                    all_sprites_list.add(g)
                    letters.append(g)
                    current = current + "g"
                    g.rect.x,g.rect.y = x,y
                    x += 45
                elif event.key == pygame.K_SPACE:
                    print(x)
                    if x > 850:
                        x = 0
                        y += 80
                    check_word.append(current)
                    current = ""
                    x += 60
                    for i in check_word:
                        if i in words and i not in correct_words:
                            correct_words.append(i)
                            del check_word[:]
                            msg("CORRECT ", 100, 500, 300, green)
                            del letters[:]
                            score += 1
                            time.sleep(1)
                        elif i in correct_words and i in words:
                            del check_word[:]
                            msg("THAT'S ALREADY DONE ", 60, 500, 300, gray)
                            if x > 850:
                                x = 0
                                y += 80
                            else:
                                x -= 200
                                if x < 0:
                                    x = 30
                            for i in letters:
                                all_sprites_list.remove(i)
                            del letters[:]
                            time.sleep(1)
                        else:
                            del check_word[:]
                            msg("TRY AGAIN ", 100, 500, 300, red)
                            del letters[:]
                            time.sleep(1)

        screen.blit(background,(0, 0))
        all_sprites_list.draw(screen)
        all_sprites_list.update()
        pygame.display.update()
        clock.tick(500)

    pygame.quit()

intro()
                    






        

import pygame
from pygame.locals import *
from random import *
pygame.init()
pygame.display.set_caption("NSI-Livet 2020")
fenetre=pygame.display.set_mode( (640, 480) )
fond=pygame.image.load("background.jpg")
skin1 = pygame.image.load("s1.png")
skin2 = pygame.image.load("s3.png")
boucle = True


class Virus:

    def __init__(self, img, win, dx, dy):
        self.virus=pygame.image.load(img)
        self.pos=self.virus.get_rect()
        self.window = win
        self.x = dx
        self.y = dy

    def actualiser(self):
        self.window.blit(self.virus, self.pos)
        self.pos=self.pos.move(self.x,self.y)
        if self.pos.right>640 or self.pos.left<0 : self.x=-self.x
        if self.pos.bottom>480 or self.pos.top<0 : self.y=-self.y

    def detecterCollision(self, posx, posy):
        if self.pos.collidepoint((posx, posy)):
            return True
        else : return False



table = []
for i in range(7):
    table.append(Virus("virus.png", fenetre, randint(1, 9),randint(1, 9)))



while boucle:
    for event in pygame.event.get() :
        if event.type==KEYDOWN :
            perso=skin2
            if event.key == pygame.K_ESCAPE:
                boucle = False
        else : perso=skin1
    persorect = perso.get_rect()
    persorect.x = 288
    persorect.y = 208
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso,persorect )
    for i in table:
        i.actualiser()
        if i.detecterCollision(persorect.x, persorect.y):
            if perso != skin2 :
                boucle = False
    pygame.time.delay(1)
    pygame.display.flip()

pygame.quit()

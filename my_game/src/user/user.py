import pygame

class User:
    #def __init__(self):
    def ui_login(self):
        font = pygame.font.SysFont('arial',16)
        font_username = font.render("Username",True,(0,0,0),(255,255,255))


pygame.init()
screen = pygame.display.set_mode((200,200),0,32)
font = pygame.font.SysFont('arial',16)
font_username = font.render("Username",True,(0,0,0),(255,255,255))
screen.blit(font_username,(10,20))
pygame.display.update()
import pygame
pygame.init()

def get_list(argument):
    switcher = {
        'modes' : pygame.display.list_modes(),
        'fronts' : pygame.font.get_fonts()
    }
    return switcher.get(argument,"nothing")

params = ['modes','fronts']

list = get_list(params[1])
print list
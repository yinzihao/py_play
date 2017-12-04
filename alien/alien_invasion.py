#coding=utf-8
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Allien Invasion")
    ship = Ship(ai_settings,screen)
    bullets=Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_aliens(aliens)
        #删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
        #print len(bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        pygame.display.flip()
run_game()


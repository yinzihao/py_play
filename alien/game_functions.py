#coding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien

def update_aliens(alines):
    alines.update()

def create_fleet(ai_settings,screen,aliens):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        aliens.add(alien)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    elif event.key == 273:
        ship.moving_top = True
    elif event.key == 274:
        ship.moving_bottom = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == 273:
        ship.moving_top = False
    elif event.key == 274:
        ship.moving_bottom = False

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print screen.get_rect()

            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        #elif event.key == pygame.K_SPACE:
            #new_bullet = Bullet(ai_settings,screen,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    screen.fill(ai_settings.bg_color)
   # background = pygame.image.load(ai_settings.background_image).convert()
   # screen.blit(background, (0, 0))
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

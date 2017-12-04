#coding=utf-8
class Settings():
    def __init__(self):
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(123,104,238)
        self.background_image = "images/sky.jpg"
        self.ship_speed_factor = 1.5

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed=10
        #1 right move -1 left move
        self.fleet_direction=1

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

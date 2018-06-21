

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 19:09
# @Author  : Jackendoff
# @Site    : 
# @File    : plane_main.py
# @Software: PyCharm

import pygame
from plane_sprites import *

class PlaneGame(object):
    '''飞机战争主程序'''

    def __init__(self):
        print('初始化')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):
        bg1 = Background() # Background 内部判断
        bg2 = Background(True) # Background 内部判断
        self.back_group = pygame.sprite.Group(bg1, bg2) # 创建精灵组

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('start')
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self): # 事件监听
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                #print('GO')
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # 根据事件监听判断按键
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print('move')
        # 使用键盘提供的方法获取键盘按键，按键元组
        keys_pressed = pygame.key.get_pressed() # 元组
        if keys_pressed[pygame.K_RIGHT]: # 按下该键 K_RIGHT = 1
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('over')
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

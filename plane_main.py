#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 18:12
# @Author  : Jackendoff
# @Site    : 
# @File    : plane_sprites.py
# @Software: PyCharm
import random # 标准模块
import pygame # 第三方模块
                # 自定义模块

SCREEN_RECT = pygame.Rect(0,0,480,700) # 定义常量
FRAME_PER_SEC = 60
CREAT_ENEMY_EVENT = pygame.USEREVENT # 定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    '''精灵'''
    def __init__(self, image_name, speed=1):
        super().__init__() # 调用父类方法
        self.image = pygame.image.load(image_name) # 加载到内存
        self.rect = self.image.get_rect() # 返回加载图像位置大小
        self.speed = speed

    def update(self): # 重写父类方法
        # 垂直移动
        self.rect.y += self.speed


class Background(GameSprite):
    '''背景精灵'''
    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    '''敌机'''
    def __init__(self):
        super(Enemy, self).__init__('./images/enemy1.png')
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super(Enemy, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill() # 将精灵从所有精灵组中移除，精灵就会自动销毁


class Hero(GameSprite):
    '''主机'''
    def __init__(self):
        super(Hero, self).__init__('./images/me1.png', 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)


class Bullet(GameSprite):
    '''子弹'''
    def __init__(self):
        super(Bullet, self).__init__('./images/bullet1.png',-2)
    def update(self):
        super(Bullet, self).update()
        if self.rect.bottom < 0:
            self.kill()



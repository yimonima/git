#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#导入包
import pygame,sys
from pygame.locals import *

#屏幕初始化
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Draw Circle")

#事件处理机制
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    #屏幕颜色初始化
    screen.fill((255,255,255))

    #定义园所需要的参数
    circleColor=255,0,0
    circlePosition=300,250
    circleRadius=100
    circleWidth=100

    #开始画圆
    pygame.draw.circle(screen,circleColor,circlePosition,circleRadius,circleWidth)

    #页面刷新
    pygame.display.update()

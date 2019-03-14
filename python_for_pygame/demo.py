#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pygame,sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Demo")

bcgColor=255,255,255
setFont=pygame.font.Font(None,60)
fontColor=255,255,0
textImage=setFont.render("LH",True,fontColor)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill(bcgColor)
    screen.blit(textImage,(250,300))
    pygame.display.update()

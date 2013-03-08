#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import pygame
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
pygame.mouse.set_visible(0)

ship = pygame.image.load("image/ship.png")
ship_top = screen.get_height() - ship.get_height()
shot = pygame.image.load("image/shot.png")
shoot_y = 0

while True:
	clock.tick(60)
	screen.fill((0,0,0))
	
	x,y = pygame.mouse.get_pos()
	screen.blit(ship, (x-ship.get_width()/2, ship_top))
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			shoot_y = 500
			shoot_x = x
	if shoot_y > 0:
		screen.blit(shot, (shoot_x, shoot_y))
		shoot_y -= 5
	pygame.display.update()

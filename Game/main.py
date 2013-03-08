#!/usr/bin/env python
# encoding: utf-8
"""
main.py

Created by Mikael Hallgren on 2012-03-19.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import os, sys
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('Monkey Fever')
bgImg = "image/bg.jpg"
shipImg = "image/ship.png"
invaderImg = "image/invader.png"
shotImg = "image/shot.png"
background = pygame.image.load(bgImg).convert()
ship = pygame.image.load(shipImg).convert_alpha()
invader = pygame.image.load(invaderImg).convert_alpha()
laser = pygame.image.load(shotImg).convert_alpha()

def exit(events):
	for event in events:
		if event.type == QUIT:
			sys.exit(0)		
	
def shot(x,y):
	while True:
		y +=3
		screen.blit(invader, (x,y))

def main():

	x, y, moveX, moveY, invaderX = 300,420,0,0, 0
	shotX, shotY = 0, 0
	Shot = False
	
	while True:
		screen.blit(background, (0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					moveX = -2
				elif event.key == K_RIGHT:
					moveX = +2
				elif event.key == K_UP:
					moveY = -2
				elif event.key == K_DOWN:
					moveY = +2
				elif event.key == K_SPACE:
					#shot(x,y)
					Shot = True
					shotX = x
					shotY = y
			
			if event.type == KEYUP:
				if event.key == K_LEFT:
					moveX = 0
				elif event.key == K_RIGHT:
					moveX = 0
				elif event.key == K_UP:
					moveY = 0
				elif event.key == K_DOWN:
					moveY = 0
					
		x += moveX
		y += moveY
		if Shot:
			shotY -= 5
			if shotY < 480:
				screen.blit(laser, (shotX+10,shotY))
			else:
				Shot = False
				shotY = 0
				shotX = 0
		
		screen.blit(invader, (invaderX,50))
		screen.blit(ship, (x,y))
		
		invaderX += 2
		if invaderX > 860:
			invaderX = -30
			
		pygame.display.update()
		
		
	



if __name__ == '__main__':
	main()


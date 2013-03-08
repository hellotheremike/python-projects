#!/usr/bin/env python
# encoding: utf-8

import random,os
import pygame
from pygame.locals import *

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('ship.png')
		self.rect.center =(320,450)
		self.x_velocity = 0
		self.y_velocity = 0
	def update(self):
		self.rect.move_ip((self.x_velocity, self.y_velocity))
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > 640:
			self.rect.right = 640
		
		if self.rect.top <= 260:
			self.rect.top = 260
		elif self.rect.bottom >= 480:
			self.rect.bottom = 480		

class ShotsFierd(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.label, self.rect = pygame.font.SysFont("Helvetica", 20), (80,100)
	def update(self, shots):
		pass


		
class Enemy(pygame.sprite.Sprite):
	def __init__(self, startx):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('invader.png')
		self.rect.centerx = startx
		self.rect.centery = 120
		self.distance = 0
		self.x_velocity = 0
		self.y_velocity = 0
	def update(self):
		if self.distance == 0:
			self.distance = random.randint(3,15)
			self.x_velocity = random.randint(-2,2)
			self.y_velocity = random.randint(-2,2)
			
		self.rect.move_ip((self.x_velocity, self.y_velocity))
		self.distance -= 1
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > 640:
			self.rect.right = 640
		
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= 220:
			self.rect.bottom = 220
		
		fire = random.randint(1,60)
		if fire == 1:
			ebomb_sprites.add(Ebomb(self.rect.midbottom))
			#shot.play()
class bomb(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('shot.png', -1)
		self.rect.center =startpos
	def update(self):
		if self.rect.bottom <= 0:
			self.kill()
		else:
			self.rect.move_ip((0, -4))
class Ebomb(pygame.sprite.Sprite):
	def __init__(self, startpos):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('shot.png', -1)
		self.rect.center =startpos
	def update(self):
		if self.rect.bottom >= 480:
			self.kill()
		else:
			self.rect.move_ip((0, 4))


def load_image(file_name, colorkey=None):
	try:
		image = pygame.image.load('image/' + file_name)
	except:
		print 'Cant load image: ', file_name
		raise SystemExit	
	image = image.convert_alpha()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	
	return image, image.get_rect()
def load_sound(name):
	class No_Sound:
		def play(self):pass
	if not pygame.mixer or not pygame.mixer.get_init():
		return No_Sound()
	try:
		sound = pygame.mixer.Sound('sound/' + name)
	except:
		print 'File does not exist:', name
		return No_Sound
	return sound

def printText(txtText, Textfont, Textsize , Textx, Texty):
	myfont = pygame.font.SysFont(Textfont, Textsize)
	label = myfont.render(txtText, 1, (255,255,255))
	screen.blit(label, (Textx, Texty))
	pygame.display.flip()

def main():
	random.seed()
	pygame.init()
	global screen
	screen = pygame.display.set_mode((640,480))
	pygame.display.set_caption('Space Game')
	background_image, background_rect = load_image('bg.jpg')
	screen.blit(background_image, (0,0))
	explode = load_sound("invaderkilled.wav")
	global shot
	shot = load_sound("shoot.wav")
	numberof_hits = 0
	numverof_shots = 0
	enemy_killed = 0
	ship = Ship()
	shots = ShotsFierd()

	shots_sprite = pygame.sprite.RenderClear(shots)
	playership_sprite = pygame.sprite.RenderClear(ship)
	bomb_sprites = pygame.sprite.RenderClear()
	enemy_sprites = pygame.sprite.RenderClear()
	#enemy_sprites.add(Enemy(212))
	#enemy_sprites.add(Enemy(320))
	#enemy_sprites.add(Enemy(428))
	global ebomb_sprites
	ebomb_sprites = pygame.sprite.RenderClear()
	spamSurface = pygame.font.SysFont('Arial', 20)
	
	running = 1
	counter = 0
	while running:
		pygame.time.delay(10)
		for event in pygame.event.get():
			if event.type == QUIT:
				running = 0
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = 0
				elif event.key == K_LEFT:
					ship.x_velocity = -4
				elif event.key == K_RIGHT:
					ship.x_velocity = 4
				elif event.key == K_UP:
					ship.y_velocity = -4
				elif event.key == K_DOWN:
					ship.y_velocity = 4
				elif event.key == K_SPACE:
					bomb_sprites.add(bomb(ship.rect.midtop))
					numverof_shots += 1
					shot.play()
					
			elif event.type == KEYUP:
				if event.key == K_LEFT:
					ship.x_velocity = 0
				elif event.key == K_RIGHT:
					ship.x_velocity = 0
				elif event.key == K_UP:
					ship.y_velocity = 0
				elif event.key == K_DOWN:
					ship.y_velocity = 0
		counter += 1
		if counter >= 200 and enemy_sprites.sprites():
			#enemy_sprites.add(Enemy(320))
			counter = 0
		
		ebomb_sprites.clear(screen,background_image)
		enemy_sprites.clear(screen,background_image)
		bomb_sprites.clear(screen,background_image)
		playership_sprite.clear(screen,background_image)
		shots_sprite.clear(screen,background_image)

		ebomb_sprites.update()
		enemy_sprites.update()
		bomb_sprites.update()
		playership_sprite.update()
		shots.update(numverof_shots)


		for hit in pygame.sprite.groupcollide(enemy_sprites, bomb_sprites,1,1):
			explode.play()
			enemy_killed += 1
			if enemy_sprites.sprites() == []:
				print "YOU WIN!!"
				printText("YOU WIN!", "Helvetica", 100, 150, 150)	
		
		for hit in pygame.sprite.groupcollide(ebomb_sprites, playership_sprite,1,0):
			explode.play()
			numberof_hits += 1
			if numberof_hits >= 3:
				print "You Lose..."

		ebomb_sprites.draw(screen)
		enemy_sprites.draw(screen)
		bomb_sprites.draw(screen)
		playership_sprite.draw(screen)



		
		eggsPixels = spamSurface.render(str(numverof_shots), True, (255, 255, 255))
		screen.blit(eggsPixels, (10, 10))
		
		pygame.display.update()
		


if __name__ == '__main__':
	main()


import pygame
import random
import os

pygame.init()

szer_okna = 600
wys_okna = 600

screen = pygame.display.set_mode((szer_okna, wys_okna))

class Biedronka():
	def __init__(self):
		self.x = random.randint (250,500)
		self.y = random.randint (250,500)
		self.vx = random.randint (-4,4)
		self.vy = random.randint (-4,4)
		self.grafika = pygame.image.load (os.path.join('123.png'))
		self.wielkosc = 20
	def rysuj(self):
		screen.blit(self.grafika,(self.x, self.y))
	def ruch (self):
		self.x = self.x + self.vx
		self.y = self.y + self.vy
		if self.x <= 0 or self.x >= szer_okna - self.wielkosc:
		    self.vx = self.vx * -1
		if self.y <=0 or self.y >= wys_okna - self.wielkosc:
		    self.vy = self.vy * -1
	def kolizja (self, player):
	    x_srodek = self.x+self.wielkosc/2
	    y_srodek = self.y+self.wielkosc/2
	    if player.collidepoint (x_srodek,y_srodek):
		    czcionka = pygame.font.SysFont ("Georgia",20)
		    napis = czcionka.render("KONIEC GRY", 1, (123, 213, 231))
		    screen.blit (napis, (100,130))
		    global gramy
		    gramy = False

przeciwnicy = []
for i in range (8):
	przeciwnicy.append(Biedronka())
x_gracz = 300
y_gracz = 300
v = 20
gracz = pygame.Rect(x_gracz, y_gracz, 20, 20)
punkty = 0

gramy = True

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if y_gracz - v > 0:
					y_gracz = y_gracz - v
			if event.key == pygame.K_DOWN:
				if y_gracz - v < wys_okna -20:
					y_gracz = y_gracz + v
			if event.key == pygame.K_RIGHT:
				if x_gracz + v < szer_okna - 20:
					x_gracz = x_gracz + v
			if event.key == pygame.K_LEFT:
				if x_gracz - v > 0:
					x_gracz = x_gracz -v
			gracz = pygame.Rect(x_gracz, y_gracz, 20, 20)
	if gramy == True:
		punkty = punkty + 1
		screen.fill ((50,50,100))
		for biedroneczka in przeciwnicy:
			biedroneczka.ruch()
			biedroneczka.rysuj()
			biedroneczka.kolizja(gracz)
		czcionka = pygame.font.SysFont ("Georgia", 20)
		napis = czcionka.render(str(punkty),1, (123, 213, 231))
		screen.blit(napis, (30,30))
		pygame.draw.rect(screen,(0,130,0),gracz,0)
		pygame.display.update()
		pygame.time.wait(10)

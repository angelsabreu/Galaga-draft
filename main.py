import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

ship = Actor("ship")
boss = Actor("boss")
bullet = Actor("bullet")

ship.pos = (WIDTH//2, HEIGHT-60)
boss.pos = (300, 250)
bullet.pos = (300, 320)

speed = 5

bullets = []
enemies = []

for x in range(8):
    for y in range(4):
        enemies.append(Actor("boss"))
        enemies[-1].x = 100 + 50*x
        enemies[-1].y = 80 + 50*y

score = 0
direction = 1
ship.dead = False

def draw():
    screen.fill("black")
    ship.draw()
    boss.draw()
    bullet.draw()
    

pgzrun.go()
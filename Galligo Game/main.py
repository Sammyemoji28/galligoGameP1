
import pgzrun
import random

HEIGHT = 600
WIDTH = 1200

WHITE = (255,255,255)
BLUE = (0,0,100)

bulletsL = []
speed = 5
player = Actor("player2")
player.pos = (WIDTH//2, HEIGHT - 55)

def draw():
    screen.clear()
    screen.fill(BLUE)
    player.draw()

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bulletsL.append(bullet)
        bulletsL[-1].x = player.x
        bulletsL[-1].y = player.y - 50

def update():
    if keyboard.left:
        player.x -= speed
        if player.x <= 25:
            player.x = 25
    if keyboard.right:
        player.x += speed
        if player.x > WIDTH - 25:
            player.x = WIDTH - 25
    '''if keyboard.space:
        bullet = Actor("bullet")
        bulletsL.append(bullet)
        bulletsL[-1].x = player.x
        bulletsL[-1].y = player.y
    '''

pgzrun.go()
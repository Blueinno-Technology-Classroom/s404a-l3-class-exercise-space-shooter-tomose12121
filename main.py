import pgzrun 
import random 
from pgzhelper import *  

WIDTH = 1024
HEIGHT = 768

player = Actor('playership2_blue')
player.pos = (WIDTH/2, HEIGHT/2)

enemy1 = 'enemygreen3'
enemy2 = 'enemyblue4'
enemy3 = 'enemyred5'

enemies = []
player_lasers = []

mouse_pos = (0,0)

def update():
    player.angle = player.angle_to(mouse_pos)


    if keyboard.w:
        player.y -= 5 
    player.top = max(0,player.top)
    if keyboard.s:
        player.y += 5 
    player.bottom = min(HEIGHT,player.bottom)
    if keyboard.a:
        player.x -= 5 
    player.left = max(0,player.left)
    if keyboard.d:
        player.x += 5 
    player.right = min(WIDTH,player.right)

    if keyboard.space:
        l = Actor('laserblue01')
        l.angle = player.angle
        l.pos = player.pos
        
        player_lasers.append(l)

    if random.randint(0,100) < 5:
        e = Actor(random.choice([enemy1,enemy2,enemy3]))
        direction = random.randint(0,3)
        if direction == 0: 
            e.x = random.randint(0,WIDTH)
        elif direction == 1:
            e.right = WIDTH
            e.y = random.randint(0,HEIGHT)
        elif direction == 2:
            e.x = random.randint(0,WIDTH)
            e.bottom = HEIGHT
        else:
            e.y= random.randint(0,HEIGHT)
    

        e.point_towards(player)

        enemies.append(e)

    for e in enemies:

        e.point_towards(player)
        e.move_forward(2)

    for l in player_lasers:
        l.move_forward(2)
        if l.top < 0  or l.bottom > HEIGHT  or l.left < 0  or l.right > WIDTH:
                player_lasers.remove(l)
                break
        for e in enemies:
            if l.collide_pixel(e):
                enemies.remove(e)
                player_lasers.remove(l)
                break

def draw():
    screen.clear()
    player.draw()
    for e in enemies:
        e.draw()
    for l in player_lasers:
        l.draw()

   



pgzrun.go() 


import pgzrun
from random import randint


TITLE="GOOD SHOT"

WIDTH=500
HEIGHT=500
message  =  ""
alien = Actor("alien")
alien.pos = 50,50

def draw():
    screen.clear
    screen.fill("Red")
    screen.draw.text(message,center=(150,150),fontsize=20)
    alien.draw()


def place_area():
    alien.x = randint(50,WIDTH -50)  
    alien.y = randint(50,WIDTH -50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "GOOD SHOT"
        place_area()
    else :
        message = "You missed it"

place_area()  

pgzrun.go()

import turtle
import random

# Fenêtre
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Constellation du Cancer")

# Tortue
etoile = turtle.Turtle()
etoile.hideturtle()
etoile.speed(0)

# Etoiles principales de la constellation
cancer = [
    (-160,-30),   # Altarf
    (-120,40),    # Asellus Borealis
    (-90,10),     # Asellus Australis
    (-40,0),      # Acubens
    (0,60),       # Iota Cancri
    (40,40),      # Chi Cancri
    (100,20),     # Xi Cancri
]

# Dessiner les étoiles
etoile.color("white")

for x,y in cancer:
    etoile.penup()
    etoile.goto(x,y)
    etoile.dot(random.randint(8,15))

# Relier les étoiles
etoile.penup()
etoile.goto(cancer[0])
etoile.pendown()

for x,y in cancer[1:]:
    etoile.goto(x,y)

# Dessiner l'amas de la Ruche (Praesepe)
for i in range(30):
    x = random.randint(-20,20)
    y = random.randint(-20,20)
    etoile.penup()
    etoile.goto(x,y)
    etoile.dot(4)

turtle.done()

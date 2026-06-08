import turtle

# Configuration de la fenêtre
ecran = turtle.Screen()
ecran.title("Constellation du Cancer")
ecran.bgcolor("black")

# Création de la tortue
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Coordonnées des étoiles
etoiles = {
    "Altarf": (-120, -80),
    "Asellus Borealis": (-40, 60),
    "Asellus Australis": (-20, 10),
    "Acubens": (80, -40),
    "Tegmine": (120, 50),
    "Lambda Cancri": (40, 100)
}

# Dessiner les étoiles
for x, y in etoiles.values():
    t.penup()
    t.goto(x, y)
    t.dot(15, "gold")

# Relier les étoiles
t.color("purple")
t.pensize(2)

liaisons = [
    ("Altarf", "Asellus Australis"),
    ("Asellus Australis", "Asellus Borealis"),
    ("Asellus Borealis", "Lambda Cancri"),
    ("Lambda Cancri", "Tegmine"),
    ("Tegmine", "Acubens")
]

for debut, fin in liaisons:
    x1, y1 = etoiles[debut]
    x2, y2 = etoiles[fin]

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Maintenir la fenêtre ouverte
turtle.done()
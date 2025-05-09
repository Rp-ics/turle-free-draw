import turtle

# Configurazione della finestra
window = turtle.Screen()
window.title("Paint con Turtle")
window.bgcolor("white")
window.setup(width=800, height=600)

# Creazione della penna
pen = turtle.Turtle()
pen.shape("classic")
pen.speed(0)
pen.penup()

# Variabili globali
current_color = "black"
pen_size = 3

# Funzione per iniziare a disegnare
def start_drawing(x, y):
    pen.goto(x, y)
    pen.pendown()

# Funzione per smettere di disegnare
def stop_drawing(_, __):
    pen.penup()

# Funzione per disegnare seguendo il mouse
def draw(x, y):
    pen.goto(x, y)

# Funzioni per cambiare colore
def set_color_black():
    global current_color
    current_color = "black"
    pen.color(current_color)

def set_color_red():
    global current_color
    current_color = "red"
    pen.color(current_color)

def set_color_blue():
    global current_color
    current_color = "blue"
    pen.color(current_color)

def set_color_green():
    global current_color
    current_color = "green"
    pen.color(current_color)

# Funzione per cambiare dimensione del pennello
def increase_pen_size():
    global pen_size
    pen_size += 1
    pen.pensize(pen_size)

def decrease_pen_size():
    global pen_size
    if pen_size > 1:
        pen_size -= 1
    pen.pensize(pen_size)

# Funzione per attivare la gomma
def activate_eraser():
    global current_color
    current_color = "white"
    pen.color(current_color)

# Collegamento degli eventi del mouse
window.listen()
window.onscreenclick(start_drawing, 1)  # Tasto sinistro del mouse per iniziare
window.onscreenclick(stop_drawing, 3)   # Tasto destro del mouse per fermare
pen.ondrag(draw)                        # Trascinamento per disegnare

# Collegamento dei tasti per cambiare colore
window.onkey(set_color_black, "k")  # Nero
window.onkey(set_color_red, "r")    # Rosso
window.onkey(set_color_blue, "b")   # Blu
window.onkey(set_color_green, "g")  # Verde

# Collegamento dei tasti per cambiare dimensione del pennello
window.onkey(increase_pen_size, "Up")    # Aumenta dimensione
window.onkey(decrease_pen_size, "Down") # Diminuisci dimensione

# Collegamento del tasto per la gomma
window.onkey(activate_eraser, "e")  # Gomma

# Avvio del programma
window.mainloop()
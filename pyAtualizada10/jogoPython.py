import turtle
import time

# Inicializa a tela do jogo
wn = turtle.Screen()
wn.title("Jogo da cobrinha")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cria a cobrinha
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Cria a comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)

# Função para mover a cobrinha
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Define as funções de controle de direção
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# Atribui as teclas de direção
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Loop principal do jogo
while True:
    wn.update()

    # Verifica se a cobrinha colidiu com a comida
    if head.distance(food) < 20:
        # Move a comida para uma nova posição
        x = turtle.random.randint(-290, 290)
        y = turtle.random.randint(-290, 290)
        food.goto(x,y)

    # Move a cobrinha
    move()

    # Verifica se a cobrinha colidiu com os limites da tela
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    # Verifica se a cobrinha colidiu consigo mesma
    for segment in segment:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)

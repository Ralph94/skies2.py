import turtle  # Our module's
import random

score = 0
lives = 3


# Screen
ms = turtle.Screen()
ms.title("Falling Piece's mini_game by Rafa94")
ms.bgcolor("light blue")
ms.bgpic("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/farm5.gif")
ms.setup(width=800, height=600)
ms.tracer(0.0)
#ms.exitonclick()

# we are uploading the our images the Screen using the register_shape function from our module
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/rooster.gif")# make sure when you upload images make sure your using the right sequence or Path // - C:
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/rooster_right.gif")
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/fireball2.gif")
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/egg3.gif")



# player
player = turtle.Turtle()
player.shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/rooster.gif")
player.color("blue")
player.penup()
player.goto(0, -250)  # y is postive in the up direction y is negative in the down direction
player.speed(0)
player.direction = "stop"

# make the pen
pen = turtle.Turtle() # also make the pen before any for _ loops or else it will write over its self
pen.hideturtle()
pen.speed(0)
pen.shape("turtle")
pen.color("blue")
pen.penup()
pen.goto(0, 260)  # y is postive in the up direction y is negative in the down direction
font = ("Courier", 24, "normal")
pen.clear()
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

# create a list of good players
goods = []  # Empty list

# Addgood players
for _ in range(20):  # we are making a set of 20 players
    good = turtle.Turtle()  # we want the other player basically across from each other thats we copyed the code one on -y and one on +y (first player in the bottom, second player on top of Screen)
    good.speed(0)
    good.shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/egg3.gif")
    good.color("red")
    good.penup()
    good.goto(-100, 250)  # y is postive in the up direction y is negative in the down direction
    good.speed = random.randint(1, 4)
    goods.append(good)


# create a list of bad players
bads = []  # Empty list

# Addbad players
for _ in range(20):  # we are making a set of 20 players
    bad = turtle.Turtle()  # we want the other player basically across from each other thats we copyed the code one on -y and one on +y (first player in the bottom, second player on top of Screen)
    bad.speed(0)
    bad.shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/fireball2.gif")
    bad.color("yellow")
    bad.penup()
    bad.goto(100, 250)  # y is postive in the up direction y is negative in the down direction
    bad.speed = random.randint(1, 4)
    bads.append(bad)



# Functions
def go_left():
    player.direction = "left"
    player.shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/rooster.gif")


def go_right():
    player.direction = "right"
    player.shape("C:/Users/Rafael Perez/PycharmProjects/turtle race/venv/rooster_right.gif")




# keyboard Binding
ms.listen()  # it is bascally saying listen for keyboard input < ^ >
ms.onkeypress(go_left, "Left")
ms.onkeypress(go_right, "Right")

# Main game loop # while something is true it will repeat
while True:
    # update screen
    ms.update()

    # Move player
    if player.direction == "left":
        x = player.xcor()
        x -= + 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += + 3
        player.setx(x)

    # Move Good Player
    for good in goods:
        y = good.ycor()
        y -= good.speed  # We want the ball to be falling at a smooth speed
        good.sety(y)
        # Check it off the Screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)

        # check for collision with player
        if good.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)



    # Move bad Player
    for bad in bads:
        y = bad.ycor()
        y -= bad.speed  # We want the ball to be falling at a slow speed
        bad.sety(y)
        # Check it off the Screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)

        # check for collision with player
        if bad.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font=font)

ms.mainloop()
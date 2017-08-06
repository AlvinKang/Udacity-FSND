import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    squareArtist = turtle.Turtle()
    squareArtist.speed(3)
    squareArtist.color("blue")
    squareArtist.shape("classic")
    
    for i in range(4):
        squareArtist.forward(100)
        squareArtist.right(90)

def draw_circle():
    circleArtist = turtle.Turtle()
    circleArtist.speed(3)
    circleArtist.color("yellow")
    circleArtist.shape("turtle")

    circleArtist.circle(100)

draw_square()
draw_circle()
window.exitonclick()

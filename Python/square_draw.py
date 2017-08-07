import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square(degrees):
    squareArtist = turtle.Turtle()
    squareArtist.speed(3)
    squareArtist.color("blue")
    squareArtist.shape("classic")

    # Draws a full-circle's number of squares
    num_times = 360 / degrees
    for i in range(num_times):
        for j in range(4):
            squareArtist.forward(100)
            squareArtist.right(90)
        squareArtist.right(degrees)

def draw_circle():
    circleArtist = turtle.Turtle()
    circleArtist.speed(3)
    circleArtist.color("yellow")
    circleArtist.shape("turtle")

    circleArtist.circle(100)

def draw_triangle():
    triangleArtist = turtle.Turtle()
    triangleArtist.speed(3)
    triangleArtist.color("white")
    triangleArtist.shape("arrow")

    for i in range(3):
        triangleArtist.forward(100)
        triangleArtist.right(120)
    

draw_square(10)
#draw_circle()
#draw_triangle()
window.exitonclick()

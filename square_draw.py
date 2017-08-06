import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    squareArtist = turtle.Turtle()
    squareArtist.speed(3)
    squareArtist.color("blue")
    squareArtist.shape("classic")
    
    for i in range(4):
        squareArtist.forward(100)
        squareArtist.right(90)

    window.exitonclick()

draw_square()

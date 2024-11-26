from turtle import *

def star_flower():
    speed(0)
    for i in range(36):
        for _ in range(5):
            forward(100)
            right(144)  # Angle to draw the star
        left(10)  # Overall rotation
star_flower()
done()

# This is a SOLID example
import turtle

class Shape:
    def __init__(self):
        self.turtle = turtle.Turtle
    def draw(self):
        pass

class octogon(Shape):
    def __init__(self):
        super.__init__
    def draw(self):
        myTurtle = turtle.Turtle()
        for i in range(8):
            myTurtle.forward(100)
            myTurtle.right(45)   

class triangle(Shape):
    def __init__(self):
        super.__init__
    def draw(self):
        myTurtle = turtle.Turtle()
        for i in range(3):
            myTurtle.forward(100)
            myTurtle.left(120)

class hexagon(Shape):
    def __init__(self):
        super.__init__
    def draw(self):
        myTurtle = turtle.Turtle()
        for i in range(6):
            myTurtle.forward(100)
            myTurtle.right(60)

drawOctogon = octogon()
drawOctogon.draw()

drawTriangle = triangle()
drawTriangle.draw()

drawHexagon = hexagon()
drawHexagon.draw()

# SRP: Each shape class is responisible for one shape and only that shape, this ensures lowers errors as if each piece of code is responible for one piece
# when something goes wrong we can quickly identify the piece of code that needs adjusting

# This piece of code is a great example of the open/close principal. The code is written so it's open to adding more shapes, but closed to changing any of the existing shapes 
# as well as the main parent class. This is great as the code is expandable without causing new errors to existing code

# LSP: Each shape class can be easily substituted with another shape, for example if you wanted to replace the triangle with a square this can be easily
# implemented without disruppting any of the other shapes or affecting the main code.

# ISR: All the shape classes are independent, so they do not relie on each other to run. What this means is that is a change happens to one shape
# this will not impact the others as they are seprate objects.

# DIP: Although each shape class does not reali on each other they do depend on the parent class, the parent class builds the foundation of 
# what we are building. Sure star, circle, triangle can exist on their known but the Shape parent classes pull them together and show we want to build
# different shapes not stars or triangles.
# Here we will be showing a KISS example, KISS standing for "Keeo it simple stupid". The main point is to not overly complicate
# that which does not need to be. Below is an example of code I wrote early in my coding journey and how I KISSed it.


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Area:
    def run(self):
        circle = Circle(5)
        circle_area = Circle.area(circle)
        print("The circle area is:", circle_area)

area= Area()
area.run()

# Although this piece of code works the same as the one below it, it is far more complicated and convoluted. There is no need for mulitple
# classes to calculate the area of a circle, we can achieve the same result with the code below.

def area():
    while True:
        radius = int(input("Radius of the circle: "))
        if radius == 0:
            break
        cic_area = 3.14159 * radius ** 2
        print("The circle area is:", cic_area)

area()

# This function does exatly what the piece of code above it does but better as instead of running it multiple times for different circles
# it just needs run once.
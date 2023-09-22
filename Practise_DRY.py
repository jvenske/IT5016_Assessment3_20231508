# DRY principle helps to save time while avoiding to have create same code repeatedly for a same result.
# Now although it may seem long writing the code like this, it means this function can be used over and over.

def area():
    while True:
        radius = int(input("Radius of the circle: "))
        if radius == 0:
            break
        cic_area = 3.14159 * radius ** 2
        print("The circle area is:", cic_area)

area()

# below is a example of not using DRY pricple, if you want area of 20 circles you can use DRY princple and get the result 
# at once intead having to write 20 lines. 

circle1= 3.14159 * 3 ** 2
print(circle1)

circle2= 3.14159 * 5 ** 2
print(circle2)

# This code may seem shorter now however in the long term saves time by calling one function instead of repeating code.

import math


# ---- Problem 1 ----
class Line():

    def __init__(self,coor1,coor2):
        
        self.coor1 = coor1
        self.coor2 = coor2
        self.x = coor2[0] - coor1[0]
        self.y = coor2[1] - coor1[1]

    def distance(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def slope(self):
        return (self.y / self.x)

li = Line([3,2],[8,10])

print(li.distance())
print(li.slope())


# ---- Problem 2 ----
class Cylinder():

    # Class Object Attribute
    pi = 3.14

    def __init__(self,height=1,radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return ((2 * self.pi * self.radius * self.height) + (2 * self.pi * (self.pi ** 2)))

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
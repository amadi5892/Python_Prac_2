mylist = [1,2,3]
myset = set()

# class Dog():

#     # CLASS OBJECT ATTRIBUTE
#     # SAME FOR ANY INSTANCE OF A CLASS
#     species = 'mammal'

#     def __init__(self,mybreed,name):
        
#         # Attributes
#         # We take in the argument
#         # Assign it using self.attribute_name
#         self.breed = mybreed
#         self.name = name

#     # OPERATIONS/Actions --> Methods
#     def bark(self,number):
#         print("Woof! My name is {} and the number is {}".format(self.name,number))

# my_dog = Dog('Lab','Frankie')

# print(my_dog)
# print(my_dog.species)
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.bark(45))


# class Circle():

#     # CLASS OBJECT ATTRIBUTE
#     pi = 3.14

#     def __init__(self,radius=1):

#         self.radius = radius
#         self.area = radius * radius * self.pi

#     # METHOD
#     def get_circumference(self):
#         return self.radius * self.pi * 2

# my_circle = Circle(30)

# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.area)
# print(my_circle.get_circumference())



# class Animal():

#     def __init__(self):
#         print("ANIMAL CREATED")

#     def who_am_i(self):
#         print("I am an animal")

#     def eat(self):
#         print('I am eating')

# myanimal = Animal()
# print(myanimal)

# class Dog(Animal):

#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")

#     def bark(self):
#         print('WoOf!!')

# mydog = Dog()

# print(mydog)





# ---- Polymorphism ----

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

niko = Dog("niko")
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))

def pet_speak(pet):
    print(pet.speak())

pet_speak(felix)
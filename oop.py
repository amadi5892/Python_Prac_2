mylist = [1,2,3]
myset = set()

class Dog():

    def __init__(self,mybreed,name,spots):
        
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = mybreed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(mybreed='Lab',name='Sammy',spots=False)

print(my_dog)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)